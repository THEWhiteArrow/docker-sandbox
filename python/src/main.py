import json
from typing import Any, Dict, List, Iterable, cast
from pyspark.sql import SparkSession, Row
from lib.utils import df2list


print("Hello World")
spark = SparkSession.Builder().appName("sandbox").getOrCreate()
spark_context = spark.sparkContext
obj = [
    {"a": 1, "b": 2, "c": {"d": 3, "e": 4}, "g": Row("a", "b", "c")},
    {"a": 3, "b": 4},
    {"a": 5, "b": 6},
    {"a": 5, "g": Row("a", "b", "c")},
    {"a": 5, "b": 6, "c": {"e": 6, "f": 6}},
]

df = spark.createDataFrame(cast(Iterable[Any], spark_context.parallelize(obj)))

# o1 = df.toPandas().to_dict(orient="records")
# --- NOTICE ----
# The above line may produce NaN values in the dictionary and None values in the list

o2 = df2list(df)
# --- NOTICE ----
# The above line will NOT produce Nan and None values in the dictionary and list


# print(json.dumps(o1, indent=2))
print(json.dumps(o2, indent=2))
