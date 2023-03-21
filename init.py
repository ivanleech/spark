import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
os.environ["SPARK_HOME"] = "/home/ivanleech/apps/github_new/spark/spark-3.1.1-bin-hadoop3.2"

import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate() 

print(spark)

mydata = spark.read.format("csv").option("header", "true").load("original.csv")

from pyspark.sql.functions import *
mydata2 = mydata.withColumn("clean_city", when(mydata.City.isNull(), "unkonwn").otherwise(mydata.City))
mydata2.show()

mydata2 = mydata2.filter(mydata2.JobTitle.isNotNull())
mydata2.show()

mydata2 = mydata2.withColumn("clean_salary", mydata2.Salary.substr(2, 100).cast("float"))
mydata2.show()

mean = mydata2.groupBy().avg("clean_salary").take(1)[0][0]
print(mean)

from pyspark.sql.functions import lit
mydata2 = mydata2.withColumn('new_salary', when(mydata2.clean_salary.isNull(), lit(mean)).otherwise(mydata2.clean_salary))
mydata2.show()
