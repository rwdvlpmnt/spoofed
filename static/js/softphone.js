document.getElementById('phoneForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const numberToCall = document.getElementById('number_to_call').value;
    const myNumber = document.getElementById('my_number').value;

    const userAgent = new SIP.UA({
        uri: 'sip:' + myNumber + '@spff.3cx.agency', // replace with your 3CX server domain or IP
        wsServers: 'wss://spff.3cx.agency:5060/ws', // WebSocket URL of your 3CX server
        traceSip: true,
        displayName: myNumber,
        authorizationUser: myNumber,
        password: 'FPZrwx51He', // replace with the actual extension password
        transportOptions: {
            wsServers: ['wss://spff.3cx.agency:5060/ws'],
            traceSip: true
        }
    });

    userAgent.on('registered', function() {
        console.log('Registered with 3CX server');

        const session = userAgent.invite('sip:' + numberToCall + '@spff.3cx.agency', {
            media: {
                constraints: {
                    audio: true,
                    video: false
                },
                render: {
                    remote: document.getElementById('remoteAudio')
                }
            }
        });

        session.on('accepted', function() {
            console.log('Call accepted');
        });

        session.on('terminated', function() {
            console.log('Call terminated');
        });
    });

    userAgent.on('registrationFailed', function() {
        console.log('Registration failed');
    });
});
