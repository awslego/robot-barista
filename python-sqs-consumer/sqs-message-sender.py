import boto3
import sys

def main(queue):
    sqs = boto3.resource('sqs')

    # Retrieving a queue by its name
    queue = sqs.get_queue_by_name(QueueName='cafe-menu-' + queue)

    # Create a new message
    response = queue.send_message(MessageBody='world')

    # The response is not a resource, but gives you a message ID and MD5
    print("MessageId created: {0}".format(response.get('MessageId')))
    print("MD5 created: {0}".format(response.get('MD5OfMessageBody')))


if __name__ == "__main__" :
    if len(sys.argv) < 2:
        print("type queue number [1/2/3]")
        exit(0)
    else:
        main(sys.argv[1])