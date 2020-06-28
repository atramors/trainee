import boto3
import json
import decimal
import logging
from flask import Flask, request
from flask_restful import Resource, Api
from funct import cwmatrix
from functools import reduce
from random import randint

logging.getLogger("boto3").setLevel(logging.WARNING)
logging.getLogger("botocore").setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")
logger = logging.getLogger(__file__)

app = Flask(__name__)
api = Api(app)


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


class DataList(Resource):
    def __init__(self):
        super().__init__()
        dynamodb = boto3.resource("dynamodb")
        self.table = dynamodb.Table("Table")

    def post(self):
        id_ = randint(1, 1000000)
        try:
            matrix = request.get_json()["data"]
        except KeyError:
            logger.error(
                f"'data' key not found in json request. Original request payload: {request.data}."
            )
        new_matrix = cwmatrix(matrix)
        logger.info(
            f"Created new matrix with 'id':\n{id_}\nIt is look like this after transformation:\n{new_matrix}\nNow it is ready to be upload to our db."
        )
        try:
            result = self.table.put_item(Item={"id": id_, "matrix": new_matrix})
            if result["ResponseMetadata"]["HTTPStatusCode"] == 200:
                return {"result": result}
            return result, 500
        except KeyError:
            logger.error(
                f"'ResponseMetadata' or 'HTTPStatusCode' key not found in result. Original result: {result.data}."
            )

    def get(self):
        try:
            db_response = self.table.scan()
            list_matrix = db_response["Items"]
        except KeyError:
            logger.error(
                f"'Items' key not found or another db error occured. Original response payload: {db_response.data}."
            )
        stringified = json.dumps(list_matrix, cls=DecimalEncoder)
        logger.info(f"Stringified list of all matrices:\n{stringified}")
        return json.loads(stringified)


class DataDetail(Resource):
    def __init__(self):
        super().__init__()
        dynamodb = boto3.resource("dynamodb")
        self.table = dynamodb.Table("Table")

    def get(self, id):
        try:
            specific_dict = self.table.get_item(Key={"id": id})
            specific_matrix = specific_dict["Item"]["matrix"]
        except KeyError:
            logger.error(
                f"'id', 'Item' or 'matrix' key not found. Original dictionary payload: {specific_dict.data}."
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

    def get(self):
        try:
            db_response = self.table.scan()
            list_matrix = db_response["Items"]
        except KeyError:
            logger.error(
                f"'Items' key not found or another db error occured. Original response payload: {db_response.data}."
            )
        stringified = json.dumps(list_matrix, cls=DecimalEncoder)
        matrixlist = json.loads(stringified)
        sumatrix = []
        for item in range(len(matrixlist)):
            sumatrix.append(matrixlist[item]["matrix"])

        # return json.loads(stringified)
        # return stringified
        return sumatrix
        

        # return reduce(mult, sumatrix)


api.add_resource(DataList, "/")
api.add_resource(DataDetail, "/<int:id>")
api.add_resource(DataCW, "/cw")


if __name__ == "__main__":
    app.run(debug=True)
