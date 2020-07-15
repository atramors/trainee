import requests
import boto3
import json
import decimal
from api import DecimalEncoder


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Table")
db_response = table.scan()
list_matrix = db_response["Items"]
stringified = json.dumps(list_matrix, cls=DecimalEncoder)
matrixlist = json.loads(stringified)
sumatrix = []
for item in range(len(matrixlist)):
    sumatrix.append(matrixlist[item]["id"])

for i in sumatrix:
    if i != 1:
        requests.delete(f"http://127.0.0.1:5000/{i}", json={"data": "matrix"})
