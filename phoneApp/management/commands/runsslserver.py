import ssl
from django.core.management.commands.runserver import Command as RunServerCommand
from django.core.servers.basehttp import WSGIServer, WSGIRequestHandler

class SSLWSGIServer(WSGIServer):
    def __init__(self, *args, **kwargs):
        # Get the SSL context
        context = kwargs.pop('ssl_context', None)
        super().__init__(*args, **kwargs)
        # Wrap the socket with SSL
        if context:
            self.socket = context.wrap_socket(self.socket, server_side=True)

class Command(RunServerCommand):
    def get_handler(self, *args, **options):
        handler = super().get_handler(*args, **options)

        # Configure SSL context
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(
            certfile=r'C:\Users\azureuser\WebDev\spoofed\cert.crt', 
            keyfile=r'C:\Users\azureuser\WebDev\spoofed\cert.key'
        )

        # Ensure the server address and port are set correctly
        server_address = (self.addr, int(self.port))
        return SSLWSGIServer(server_address, handler, ssl_context=context)
