import boto3
import sys

def main(queue):
    # Get the service resource, in this case SQS Resource from boto3 module
    sqs = boto3.resource('sqs')

    # Create a new queue named test passing a few attributes, in this case just DelaySeconds
    queue = sqs.create_queue(QueueName='cafe-menu-' + queue, Attributes={'DelaySeconds': '0'})

    # We can now access identifiers and attributes
    print(queue.url)
    print(queue.attributes.get('DelaySeconds'))


if __name__ == "__main__" :
    if len(sys.argv) < 2:
        print("type queue number [1/2/3]")
        exit(0)
    else:
        main(sys.argv[1])