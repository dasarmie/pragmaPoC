from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("pragma_PoC").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

