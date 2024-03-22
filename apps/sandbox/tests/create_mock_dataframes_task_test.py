import pytest
from typing import Iterable, cast
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    DecimalType,
    ArrayType,
    FloatType,
    DoubleType,
    NumericType,
    LongType,
)
from pyspark.sql import SparkSession, Row
from sandbox.libs.utils import df2list
from sandbox.libs.container import container
from sandbox.generated.sandbox import Sandbox

spark = container.get(SparkSession)
spark_context = spark.sparkContext


@pytest.mark.skip(
    reason="Has decimal type and should not be mixed with different types"
)
def task_2_test():
    data = [
        {"arr": [1.2, 2.2, 3, 4.0]},
    ]

    schema = StructType(
        [
            StructField("arr", ArrayType(DecimalType(5, 2)), True),
        ]
    )
    df = spark.createDataFrame(
        data=cast(Iterable[Row], spark_context.parallelize(data)), schema=schema
    )

    print(df.toPandas().to_dict(orient="records"))


def task_1_test():
    obj = [
        {"z": None, "a": 1, "b": 2, "c": {"d": 3, "e": 4}, "g": ["a", "b", "c"]},
        {"z": None, "a": 3, "b": 4},
        {"z": None, "a": 5, "b": 6},
        {"z": None, "a": 5, "g": ["a", "b", "c"]},
        {"z": None, "a": 5, "b": 6, "c": {"e": 6, "f": 6}},
    ]

    # --- ACTION 1 ---
    print("ACTION 1 - STARTING")
    sandbox_list = [Sandbox.from_dict(el) for el in obj]
    sandbox_dict_list = [el.to_dict() for el in sandbox_list]
    df = spark.createDataFrame(
        cast(Iterable[Row], spark_context.parallelize(sandbox_dict_list))
    )
    print("ACTION 1 - FINISHED")

    # --- ACTION 2 ---
    print("ACTION 2 - STARTING")
    # The following line will NOT produce any None or nan values
    output_dict_list_1 = df2list(df)
    # The following line will produce None or nan values
    output_dict_list_2 = df.toPandas().to_dict(orient="records")
    print("ACTION 2 - FINISHED")

    # --- NOTICE ---
    # It would make sense to cast the input and output to the generated classes
    # so that the user has access to all the fields including those that are empty
