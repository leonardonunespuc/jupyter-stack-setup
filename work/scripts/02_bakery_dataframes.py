#!/usr/bin/python

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession \
    .builder \
    .appName('pyspark_demo_app') \
    .getOrCreate()

bakery_schema = StructType([
    StructField('date', StringType(), True),
    StructField('time', StringType(), True),
    StructField('transaction', IntegerType(), True),
    StructField('item', StringType(), True)
])

df3 = spark.read \
    .format('csv') \
    .option('header', 'true') \
    .load('../datasets/BreadBasket_DMS.csv', schema=bakery_schema)

df3.show(10)
df3.count()