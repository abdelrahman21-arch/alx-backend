import { createClient } from 'redis';
const redis = require('redis');
const { promisify } = require('util');


const client = createClient({
  url: 'redis://127.0.0.1:6379' // Adjust URL if necessary
});

const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName)
{
    try {
	const reply = await getAsync(schoolName);
	console.log(`The value for key "${schoolName} is: ${reply}`);
} catch (err)
{
    console.error('Error fetching value:', err);
}
  }



displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');


