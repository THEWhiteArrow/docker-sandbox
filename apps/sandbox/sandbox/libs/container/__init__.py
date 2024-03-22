import injector 
from pyspark.sql import SparkSession


def create_default_container():
    container = injector.Injector()

    # --- SETUP DEPENDENCIES ---
    my_spark_session = SparkSession.Builder().appName("myApp").getOrCreate()

    # --- BIND DEPENDENCIES ---
    container.binder.bind(SparkSession, my_spark_session)
    return container 

container = create_default_container()
 

