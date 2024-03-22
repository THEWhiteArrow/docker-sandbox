from typing import List, Dict
from pyspark.sql.types import (
    StringType,
    LongType,
    StructType,
    StructField,
    ArrayType,
    MapType,
)

demo_people_spark_schema = StructType(
    [
        StructField("name", StringType(), False),
        StructField("age", LongType(), False),
        StructField(
            "address",
            StructType(
                [
                    StructField("street", StringType(), False),
                    StructField("city", StringType(), False),
                    StructField("state", StringType(), False),
                    StructField("zip", StringType(), False),
                ]
            ),
            False,
        ),
        StructField("email", StringType(), False),
        StructField("devices", ArrayType(StringType(), False), False),
    ]
)

demo_people_data: List[Dict] = [
    {
        "name": "John Doe",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "Springfield",
            "state": "IL",
            "zip": "62701",
        },
        "email": "to@ifca.mg",
        "devices": [
            "85892297-3680-5b6a-a527-a2062c5156c1",
            "748fb482-b282-54ab-9b9c-daf2f9a1162d",
        ],
    },
    {
        "name": "Mary Johnson",
        "age": 28,
        "address": {
            "street": "456 Maple Ave",
            "city": "Springfield",
            "state": "IL",
            "zip": "62702",
        },
        "email": "me@izciiti.gf",
        "devices": [
            "222d5379-9c91-5333-91c5-8f44890355dd",
            "648b89bb-8e98-54c4-af6d-68e33a35b580",
        ],
    },
    {
        "name": "Bob Smith",
        "age": 35,
        "address": {
            "street": "789 Oak St",
            "city": "Springfield",
            "state": "IL",
            "zip": "62703",
        },
        "email": "eceego@lav.us",
        "devices": [
            "0006529a-6226-53dc-a9da-8fbf10746c11",
            "e507c620-3a8f-54d5-a2cb-d0bb7b408a69",
        ],
    },
    {
        "name": "Alice Johnson",
        "age": 32,
        "address": {
            "street": "321 Elm St",
            "city": "Springfield",
            "state": "IL",
            "zip": "62704",
        },
        "email": "poduw@og.ga",
        "devices": [
            "a695db6e-84da-5cbd-95c0-ff64f124ab4f",
            "30edbfd5-9388-5fb1-afb6-a5404a896fbf",
        ],
    },
]
