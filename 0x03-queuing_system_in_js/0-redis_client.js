import { createClient } from 'redis';

console.log('Starting Redis client...');

const client = createClient({
  url: 'redis://127.0.0.1:6379' // Adjust URL if necessary
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});
