import unittest
import json
from flask import request
from api import app
from unittest import mock
from decimal import Decimal


@mock.patch("boto3.resource")
class BasicTestCase(unittest.TestCase):
    maxDiff = None
    matrix_asset = {
        "data": [
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]],
            [[33, 34, 35, 36], [37, 38, 39, 40], [41, 42, 43, 44], [45, 46, 47, 48]],
            [[49, 50, 51, 52], [53, 54, 55, 56], [57, 58, 59, 60], [61, 62, 63, 64]],
        ]
    }

#    def test_post(self, resource):
#        with app.test_client() as client:
#            resource().Table().put_item.return_value = {
#                "ResponseMetadata": {"HTTPStatusCode": 200}
#            }
#            response = client.post("/", json=self.matrix_asset)
#            self.assertEqual(response.status_code, 200)
#            resource().Table().put_item.assert_called_with(
#                Item={
#                    "id": mock.ANY,
#                    "matrix": [
#                        [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]],
#                        [
#                            [17, 21, 25, 29],
#                            [18, 22, 26, 30],
#                            [19, 23, 27, 31],
#                            [20, 24, 28, 32],
#                        ],
#                        [
#                            [33, 37, 41, 45],
#                            [34, 38, 42, 46],
#                            [35, 39, 43, 47],
#                            [36, 40, 44, 48],
#                        ],
#                        [
#                            [49, 53, 57, 61],
#                            [50, 54, 58, 62],
#                            [51, 55, 59, 63],
#                            [52, 56, 60, 64],
#                        ],
#                    ],
#                }
#            )

    def test_get(self, resource):
        with app.test_client() as client:
            resource().Table().get_item.return_value = {
                "Item": {
                    "id": Decimal("322594"),
                    "matrix": [
                        [
                            [Decimal("1"), Decimal("5"), Decimal("9"), Decimal("13")],
                            [Decimal("2"), Decimal("6"), Decimal("10"), Decimal("14")],
                            [Decimal("3"), Decimal("7"), Decimal("11"), Decimal("15")],
                            [Decimal("4"), Decimal("8"), Decimal("12"), Decimal("16")],
                        ],
                        [
                            [
                                Decimal("17"),
                                Decimal("21"),
                                Decimal("25"),
                                Decimal("29"),
                            ],
                            [
                                Decimal("18"),
                                Decimal("22"),
                                Decimal("26"),
                                Decimal("30"),
                            ],
                            [
                                Decimal("19"),
                                Decimal("23"),
                                Decimal("27"),
                                Decimal("31"),
                            ],
                            [
                                Decimal("20"),
                                Decimal("24"),
                                Decimal("28"),
                                Decimal("32"),
                            ],
                        ],
                        [
                            [
                                Decimal("33"),
                                Decimal("37"),
                                Decimal("41"),
                                Decimal("45"),
                            ],
                            [
                                Decimal("34"),
                                Decimal("38"),
                                Decimal("42"),
                                Decimal("46"),
                            ],
                            [
                                Decimal("35"),
                                Decimal("39"),
                                Decimal("43"),
                                Decimal("47"),
                            ],
                            [
                                Decimal("36"),
                                Decimal("40"),
                                Decimal("44"),
                                Decimal("48"),
                            ],
                        ],
                        [
                            [
                                Decimal("49"),
                                Decimal("53"),
                                Decimal("57"),
                                Decimal("61"),
                            ],
                            [
                                Decimal("50"),
                                Decimal("54"),
                                Decimal("58"),
                                Decimal("62"),
                            ],
                            [
                                Decimal("51"),
                                Decimal("55"),
                                Decimal("59"),
                                Decimal("63"),
                            ],
                            [
                                Decimal("52"),
                                Decimal("56"),
                                Decimal("60"),
                                Decimal("64"),
                            ],
                        ],
                    ],
                },
                "ResponseMetadata": {
                    "RequestId": "38KTL3GB0GIUNLAU529BSKVV23VV4KQNSO5AEMVJF66Q9ASUAAJG",
                    "HTTPStatusCode": 200,
                    "HTTPHeaders": {
                        "server": "Server",
                        "date": "Mon, 22 Jun 2020 12:51:35 GMT",
                        "content-type": "application/x-amz-json-1.0",
                        "content-length": "902",
                        "connection": "keep-alive",
                        "x-amzn-requestid": "38KTL3GB0GIUNLAU529BSKVV23VV4KQNSO5AEMVJF66Q9ASUAAJG",
                        "x-amz-crc32": "4113669886",
                    },
                    "RetryAttempts": 0,
                },
            }

            response = client.get("/322594")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.get_json(),
                "[[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15],"
                " [4, 8, 12, 16]], [[17, 21, 25, 29], [18, 22, 26, 30],"
                " [19, 23, 27, 31], [20, 24, 28, 32]], [[33, 37, 41, 45],"
                " [34, 38, 42, 46], [35, 39, 43, 47], [36, 40, 44, 48]],"
                " [[49, 53, 57, 61], [50, 54, 58, 62], [51, 55, 59, 63],"
                " [52, 56, 60, 64]]]",
            )

    def test_delete(self, resource):
        with app.test_client() as client:
            response = client.delete(f"/{666}")
            self.assertEqual(response.status_code, 204)
            resource().Table().delete_item.assert_called_with(Key={"id": 666})


if __name__ == "__main__":
    unittest.main()
