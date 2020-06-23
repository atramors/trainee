import boto3
import json
import decimal
import logging
from flask import Flask, request
from flask_restful import Resource, Api
from random import randint

logging.basicConfig(
    filename="api.log", level=logging.DEBUG, format="%(asctime)s %(message)s"
)

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
        matrix = request.get_json()["data"]
        new_matrix = [
            [[matrix[k][i][j] for i in range(4)] for j in range(4)] for k in range(4)
        ]
        result = self.table.put_item(Item={"id": id_, "matrix": new_matrix})
        if result["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return {"result": result}
        return result, 500

    def get(self):
        ugly_list_of_matrix = self.table.scan()
        list_of_matrix = ugly_list_of_matrix["Items"]
        list_of_matrix = json.dumps(list_of_matrix, cls=DecimalEncoder)
        return json.loads(list_of_matrix)


class DataDetail(Resource):
    def __init__(self):
        super().__init__()
        dynamodb = boto3.resource("dynamodb")
        self.table = dynamodb.Table("Table")

    def get(self, id):
        result1 = self.table.get_item(Key={"id": id})
        result = result1["Item"]["matrix"]
        result = json.dumps(result, cls=DecimalEncoder)
        return result

    def delete(self, id):
        self.table.delete_item(Key={"id": id})
        return "", 204


api.add_resource(DataList, "/")
api.add_resource(DataDetail, "/<int:id>")


if __name__ == "__main__":
    app.run(debug=True)
