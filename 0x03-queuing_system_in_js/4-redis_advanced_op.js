const redis = require('redis');
const client = redis.createClient();

client.on('connect', () => {
    console.log('Connected to Redis');
});

client.on('error', (err) => {
    console.log('Redis error: ' + err);
});

const hashKey = 'HolbertonSchools';

client.hset(hashKey, 'Portland', 50, redis.print);
client.hset(hashKey, 'Seattle', 80, redis.print);
client.hset(hashKey, 'New York', 20, redis.print);
client.hset(hashKey, 'Bogota', 20, redis.print);
client.hset(hashKey, 'Cali', 40, redis.print);
client.hset(hashKey, 'Paris', 2, redis.print);

client.hgetall(hashKey, (err, reply) => {
    if (err) {
	console.error('Error fetching hash:', err);
    } else
    {

	console.log('HolbertonSchools:', reply);
    }
    client.quit();
});

