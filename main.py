from sre_constants import SUCCESS

from neo4j import Record
import boto3
import json

def handler(event, context):
    sns_client = boto3.client("sns")
    sns_arn ="arn:aws:sns:ca-central-1:020330999075:fanout" 
    print(event)

    for record in event["Records"]:
        product = json.loads(record["body"])
        print(product)
        print(SUCCESS)
        print(Record) 

    try:
        sns_client.publish(
            TopicArn=sns_arn,
            Subject=f"Your Order {product['id']} was placed",
            Message=f"Thank you for buying {product['name']}. Come back soon!!"
            )

        print("successfully sent notification")
    except Exception as exp:
        print(f"error occured, {exp}")