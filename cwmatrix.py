import json
import boto3
from random import randint


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Table")


def lambda_handler(event, context=0):
    id_ = randint(1, 1000000)
    for record in event['Records']:
        matrix = json.loads(record['body'])["matrix"]
        length = range(len(matrix))
        row = column = range(4)
        new_matrix = [[[matrix[l][c][r] for c in column]
                       for r in row] for l in length]
        try:
            result = table.put_item(Item={"id": id_, "matrix": new_matrix})
            if result["ResponseMetadata"]["HTTPStatusCode"] == 200:
                return {"statusCode": 200, "data": result}
            return result, 500
        except KeyError:
            print("Failed")
