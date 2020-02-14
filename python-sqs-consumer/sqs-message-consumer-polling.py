import boto3
import sys

def main(queue):
    sqs = boto3.resource('sqs')

    queue = sqs.get_queue_by_name(QueueName='cafe-menu-' + queue)

    while 1:
        messages = queue.receive_messages(WaitTimeSeconds=5)
        for message in messages:
            print("Message received: {0}".format(message.body))
            message.delete()


if __name__ == "__main__" :
    if len(sys.argv) < 2:
        print("type queue number [1/2/3]")
        exit(0)
    else:
        main(sys.argv[1])