cp $SPARK_HOME/conf/spark-defaults.conf.template $SPARK_HOME/conf/spark-defaults.conf

./sbin/start-master.sh
./sbin/start-worker.sh spark://ubuntu1:7077

./sbin/stop-master.sh
./sbin/stop-worker.sh


# client mode
--deploy-mode client

# cluster mode
--master yarn

# debug
YARN -> app ID -> app master on Spark UI

# Spark Dataframes -> immutable
Transformations
    Narrow - Transformations that operate on a single partition (groupby only)
    Wide - Transformations that requires other partitions (groupby + count)
Actions -> Lazy Evaluation. Only when an action is called, the transformations are executed.
    read
    write
    collect
    show

