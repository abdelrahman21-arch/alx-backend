const redis = require('redis');
const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log('Redis client not connected to the server: ' + err);
});

// subscribee
const channel = 'holberton school channel'
client.subscribe(channel, (err, response) => {
    if (err) {
	console.error('Subscription error:', err);
    } else {
	console.log(`subscribed to channel: ${channel}`);
    }
});

// Handle message published

client.on('message',(channel, message) => {
    console.log(`Recieved message from channel ${channel}: ${message}`);

    if (message === "KILL_SERVER") {
	console.log('Quitting....');
        client.quit();
    }

});

