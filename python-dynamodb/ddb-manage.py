import sys
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cafe_order_transactions')

def ddb_read(oid):
    response = table.query (
        KeyConditionExpression=Key('order_id').eq(oid)
    )
    print (response['Items'])


def ddb_write(oid):
    response = table.put_item(
        Item={
            'order_id': oid,
            'timestamp' : 20202102233028 ,
            'isCurrent': 'true',
            'status': 'ready',
        }
    )
    print(response)

def ddb_handle(oid):

    #response = table.query (
    #    KeyConditionExpression=Key('coffeeType').eq('Americano')& Key('isCurrent').eq('true')
    #)
    #print '--------'
    #print response['Items']
    #if response['Items']['order_id']:
    #    response = table.put_item(
    #        Item={
    #            'order_id':  response['Items']['order_id'],
    #            'timestamp' :  response['Items']['timestamp'] ,
    #            'isCurrent': 'false',
    #            'status': 'complete',
    #        }
    #   )
    response = table.query (
        KeyConditionExpression=Key('order_id').eq(oid)
    )
    print '--------'
    print response['Items'][0]['order_id']

    if response['Items'][0]['order_id']:
        response = table.put_item(
            Item={
                'order_id':  response['Items'][0]['order_id'],
                'coffeeSize' :  response['Items'][0]['coffeeSize'] ,
                'coffeeType' :  response['Items'][0]['coffeeType'] ,
                'beanOrigin' :  response['Items'][0]['beanOrigin'] ,
                'timestamp' :  response['Items'][0]['timestamp'] ,
                'isCurrent': 'true',
                'status': 'complete',
            }
        )

    else:
        print 'error : no true'


if __name__ == "__main__" :
    if len(sys.argv) < 2:
        print("type mode(r|w|h) key")
        exit(0)
    else:
        if sys.argv[1] == 'r':
            ddb_read(sys.argv[2].strip())
        elif sys.argv[1] == 'w':
            ddb_write(sys.argv[2].strip())
        elif sys.argv[1] == 'h':
            ddb_handle(sys.argv[2].strip())
        else:
            print "input error" + sys.argv[1]