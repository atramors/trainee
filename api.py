import asyncio
import boto3
import json
import decimal
import logging
import requests
from flask import Flask, request
from flask_restful import Resource, Api
from funct import cwmatrix, crmatrix_norm, matrixmult, matrixmult3d
from functools import reduce
from profilehooks import profile
from random import randint


logging.getLogger("boto3").setLevel(logging.WARNING)
logging.getLogger("botocore").setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")
logger = logging.getLogger(__file__)

app = Flask(__name__)
api = Api(app)
lambda_client = boto3.client("lambda")
sqs_client = boto3.client("sqs")


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


class DataList(Resource):
    def __init__(self):
        super().__init__()
        dynamodb = boto3.resource("dynamodb")
        sqs = boto3.resource("sqs")
        self.table = dynamodb.Table("Table")

    # @profile(sort="cumtime")
    def post(self):
        try:
            matrix = request.get_json()["data"]

        except KeyError:
            logger.error(
                f"'data' key not found in json request. Original request\
                     payload: {request.data}."
            )
        event = {"matrix": matrix}
        # SQS message
        sqs_queue_url = sqs_client.get_queue_url(
            QueueName="my-queue")["QueueUrl"]
        response = sqs_client.send_message(
            QueueUrl=sqs_queue_url, MessageBody=json.dumps(event)
        )
        return response

    # @profile(immediate=True)
    def get(self):
        try:
            db_response = self.table.scan()
            list_matrix = db_response["Items"]
        except KeyError:
            logger.error(
                f"\n'Items' key not found or another db error occured.\
                     Original response payload: {db_response.data}."
            )
        stringified = json.dumps(list_matrix, cls=DecimalEncoder)
        logger.info(f"\nStringified list of all matrices:\n{stringified}")
        return json.loads(stringified)


class DataDetail(Resource):
    def __init__(self):
        super().__init__()
        dynamodb = boto3.resource("dynamodb")
        self.table = dynamodb.Table("Table")

    # @profile(immediate=True)
    def get(self, id):
        try:
            specific_dict = self.table.get_item(Key={"id": id})
            specific_matrix = specific_dict["Item"]["matrix"]
        except KeyError:
            logger.error(
                f"'id', 'Item' or 'matrix' key not found. Original dictionary\
                     payload: {specific_dict.data}."
            )
        result = json.dumps(specific_matrix, cls=DecimalEncoder)
        return result

    def delete(self, id):
        self.table.delete_item(Key={"id": id})
        return "", 204


class DataCW(Resource):
    def __init__(self):
        super().__init__()
        dynamodb = boto3.resource("dynamodb")
        self.table = dynamodb.Table("Table")

    # @profile(immediate=True)
    def get(self):
        try:
            db_response = self.table.scan()
            list_matrix = db_response["Items"]
        except KeyError:
            logger.error(
                f"\n'Items' key not found or another db error occured. Original\
                     response payload: {db_response.data}."
            )
        stringified = json.dumps(list_matrix, cls=DecimalEncoder)
        matrixlist = json.loads(stringified)
        sumatrix = []
        for item in range(len(matrixlist)):
            sumatrix.append(matrixlist[item]["matrix"])
        mult_matrices = reduce(lambda x, y: matrixmult(x, y), sumatrix)

        logger.info(
            f"\nThe result of all matrices multiplication:\
            \n{mult_matrices}"
        )
        return mult_matrices


api.add_resource(DataList, "/")
api.add_resource(DataDetail, "/<int:id>")
api.add_resource(DataCW, "/cw")


if __name__ == "__main__":
    app.run(debug=True)
