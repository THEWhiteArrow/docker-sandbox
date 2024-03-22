from typing import List, Dict, Type, cast, Iterable
from typedspark import (
    Column,
    DataSet,
    Schema,
    MapType,
    ArrayType,
    StructType,
    register_schema_to_dataset,
    transform_to_schema,
)
from pyspark.sql import SparkSession, DataFrame, Row
import pyspark.sql.functions as sf
from pyspark.sql.types import (
    StringType,
    LongType,
)

from sandbox.libs.container import container
from sandbox.libs.data import demo_people_data, demo_people_spark_schema
from sandbox.generated.person import Person as PersonJson, Address as AddressJson

print("--- SETUP ---")

spark = container.get(SparkSession)
spark_context = spark.sparkContext


def create_people_df() -> DataFrame:
    return spark.createDataFrame(
        cast(Iterable[Row], spark_context.parallelize(demo_people_data)),
        schema=demo_people_spark_schema,
    )


class Address(Schema):
    street: Column[StringType]
    city: Column[StringType]
    state: Column[StringType]
    zip: Column[StringType]


class Person(Schema):
    name: Column[StringType]
    age: Column[LongType]
    address: Column[StructType[Address]]  # Specify keyType and valueType
    email: Column[StringType]
    devices: Column[ArrayType[StringType]]


print("--- RUN ---")

df = create_people_df()
ds = DataSet[Person](df)

print("--- DISPLAY ---")

ds.show()

print("--- TRANSFORM ---")


class ConformedAddress(Schema):
    name2: Column[StringType]
    street: Column[StringType]
    city: Column[StringType]


df.select(
    Person.name,
    f"{Person.address.str}.{Address.street.str}",
    f"{Person.address.str}.{Address.city.str}",
).show()

ds.transform(
    lambda ds: ds.select(
        Person.name,
        f"{Person.address.str}.{Address.street.str}",
        f"{Person.address.str}.{Address.city.str}",
    )
).show()

# df.select(
#     Person.name,
#     PersonJson.address.street,
#     PersonJson.address.city,
# )

# throws error
try:
    tds = transform_to_schema(
        ds.select(*Person.all_column_names()),
        ConformedAddress,
        {
            ConformedAddress.name2: Person.name,
            ConformedAddress.street: Person.address,
        },
    )
    tds.show()

except Exception as e:
    print(e)


df.select(Person.name, "address.street", "address.city").show()


""" --- CONCLUSION ---
(-)
1. The current implementation of typedspark does not support nested schema transformation or selection.
2. It is possible to select nested schema using string path or dot notation.
3. Additional schemas would be requried on each step of transformation, however those schemas could replace all JSON quicktype schemas.

(+)
1. It is easy to transform not nested schema.
2. No need to cast it to Json objects.

"""
