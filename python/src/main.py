from typing import Any, Dict, List, Iterable, cast
from pyspark.sql import SparkSession, Row
from lib.utils import df2list
from generated.sandbox import Sandbox

print("Hello World")

# --- JOB 0 ---
spark = SparkSession.Builder().appName("sandbox").getOrCreate()
spark_context = spark.sparkContext
obj = [
    {"z": None, "a": 1, "b": 2, "c": {"d": 3, "e": 4}, "g": ["a", "b", "c"]},
    {"z": None, "a": 3, "b": 4},
    {"z": None, "a": 5, "b": 6},
    {"z": None, "a": 5, "g": ["a", "b", "c"]},
    {"z": None, "a": 5, "b": 6, "c": {"e": 6, "f": 6}},
]

# --- JOB 1 ---
print("JOB 1 - STARTING")
sandbox_list = [Sandbox.from_dict(el) for el in obj]
sandbox_dict_list = [el.to_dict() for el in sandbox_list]
df = spark.createDataFrame(
    cast(Iterable[Row], spark_context.parallelize(sandbox_dict_list))
)
print("JOB 1 - FINISHED")

# --- JOB 2 ---
print("JOB 2 - STARTING")
# The following line will NOT produce any None or nan values
output_dict_list_1 = df2list(df)
# The following line will produce None or nan values
output_dict_list_2 = df.toPandas().to_dict(orient="records")
print("JOB 2 - FINISHED")
