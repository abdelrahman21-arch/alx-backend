const kue = require('kue');




const queue = kue.createQueue({
    redis: {
	host: '127.0.0.1',
	port: 6379
    }
});



    function addJob(phoneNumber, message) {
    const jobData = {
        phoneNumber: phoneNumber,
        message: message
    };

    const job = queue.create('push_notification_code', jobData)
        .priority('normal')
        .attempts(5) // Retry up to 5 times if the job fails
        .save((err) => {
            if (err) {
                console.error('Failed to add job:', err);
            } else {
                console.log(`Notification job created: ${job.id}`);
            }
        });
}

addJob('+1234567890', 'hello this is your notification!');

    
