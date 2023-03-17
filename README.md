cp $SPARK_HOME/conf/spark-defaults.conf.template $SPARK_HOME/conf/spark-defaults.conf

./sbin/start-master.sh
./sbin/start-worker.sh spark://ubuntu1:7077

./sbin/stop-master.sh
./sbin/stop-worker.sh