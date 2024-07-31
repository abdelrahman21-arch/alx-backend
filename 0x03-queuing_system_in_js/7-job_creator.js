const kue = require('kue');

// Create a Kue queue
const queue = kue.createQueue({
    redis: {
        host: '127.0.0.1',
        port: 6379
    }
});
const jobs = [
 {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
{
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

jobs.forEach((jobData, index) => {
    const job = queue.create('push_notification_code_2', jobData)
        .priority('normal')
        .attempts(3) // Retry up to 3 times if the job fails
        .save((err) => {
            if (!err) {
                console.log(`Notification job created: ${job.id}`);
            }
        });

    // Event listener for job completion
    job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
    });

    // Event listener for job failure
    job.on('failed', (errorMessage) => {
        console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });

    // Event listener for job progress
    job.on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
    });
});
