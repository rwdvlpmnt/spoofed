document.getElementById('phoneForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const numberToCall = document.getElementById('number_to_call').value;
    const myNumber = document.getElementById('my_number').value;
    const hostNumber = document.getElementById('host_number').value;

    const userAgent = new SIP.UA({
        uri: 'sip:' + myNumber + '@your-3cx-domain.com',
        wsServers: 'wss://your-3cx-domain.com:5060/ws',
        traceSip: true,
        displayName: myNumber,
        authorizationUser: myNumber,
        password: 'your-3cx-password',
        transportOptions: {
            wsServers: ['wss://your-3cx-domain.com:5060/ws'],
            traceSip: true
        }
    });

    userAgent.on('registered', function () {
        console.log('Registered with 3CX server');

        const session = userAgent.invite('sip:' + numberToCall + '@your-3cx-domain.com', {
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

        session.on('accepted', function () {
            console.log('Call accepted');
        });

        session.on('terminated', function () {
            console.log('Call terminated');
        });
    });

    userAgent.on('registrationFailed', function () {
        console.log('Registration failed');
    });
});
