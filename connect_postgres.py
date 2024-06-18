import psycopg2

try:
    connection = psycopg2.connect(
        user="lojpqrcenx",
        password="Sp808MLLfKTniy$q",
        host="spoofed-server.postgres.database.azure.com",
        port=5432,
        database="spoofed-database",
        sslmode="require"
    )
    print("Connection successful")
except Exception as error:
    print(f"Error: {error}")

