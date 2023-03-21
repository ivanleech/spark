import os 
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
os.environ["SPARK_HOME"] = "/home/ivanleech/apps/github_new/spark/spark-3.1.1-bin-hadoop3.2"
import findspark
findspark.init()

import sys
from pyspark.sql import *
from lib.logger import Log4j
from lib.utils import *

if __name__ == "__main__":
    conf = get_spark_app_config()

    spark = SparkSession \
        .builder \
        .config(conf=conf)\
        .getOrCreate()
        # .appName("HelloSpark") \
        # .master("local[2]") \

    # sc = spark.sparkContext
    # sc.setLogLevel("INFO")

    logger = Log4j(spark)
    print(logger.logger.getEffectiveLevel())

    if len(sys.argv) != 2:
        logger.error("Usage: HelloSpark <filename>")
        sys.exit(-1)

    logger.info("Starting HelloSpark")

    survey_raw_df = load_survey_df(spark, sys.argv[1])
    partitioned_survey_df = survey_raw_df.repartition(2)
    count_df = count_by_country(partitioned_survey_df)
    count_df.show()

    logger.info("Finished HelloSpark")
    spark.stop()
