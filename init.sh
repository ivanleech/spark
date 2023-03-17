#/bin/bash

apt-get update
apt-get install openjdk-8-jdk-headless -qq > /dev/null
wget -q http://archive.apache.org/dist/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz
tar xf spark-2.3.1-bin-hadoop2.7.tgz
pip install -q findspark

