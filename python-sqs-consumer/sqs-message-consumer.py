import boto3
import sys

def main(queue):
    # Choosing the resource from boto3 module
    sqs = boto3.resource('sqs')

    # Get the queue named test
    queue = sqs.get_queue_by_name(QueueName='cafe-menu-' + queue)

    # Process messages by printing out body from test Amazon SQS Queue
    for message in queue.receive_messages():
        print('Hello, {0}'.format(message.body))
        message.delete()

if __name__ == "__main__" :
    if len(sys.argv) < 2:
        print("type queue number [1/2/3]")
        exit(0)
    else:
        main(sys.argv[1])