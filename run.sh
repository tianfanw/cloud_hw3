#!/bin/bash

TOPIC_WORDCOUNT_MAPPER=topic-wordcount/mapper.py
TOPIC_WORDCOUNT_REDUCER=topic-wordcount/reducer.py
SORT_MAPPER=sort/mapper.py
SORT_REDUCER=sort/reducer.py

hdfs dfs -rm -r -f topic-wordcount-input
hdfs dfs -mkdir topic-wordcount-input
for f in split-tweets/*; do
    hdfs dfs -rm -f topic-wordcount-input/*
    hdfs dfs -rm -r -f topic-wordcount-output
    hdfs dfs -rm -r -f topic-sort-output
    hdfs dfs -put $f topic-wordcount-input/
    echo "Start running first job"
    hadoop jar hadoop-streaming-2.6.0.jar -file $TOPIC_WORDCOUNT_MAPPER -mapper $TOPIC_WORDCOUNT_MAPPER -file $TOPIC_WORDCOUNT_REDUCER -reducer $TOPIC_WORDCOUNT_REDUCER -input topic-wordcount-input -output topic-wordcount-output
    echo "Start running second job"
    hadoop jar hadoop-streaming-2.6.0.jar -file $SORT_MAPPER -mapper $SORT_MAPPER -file $SORT_REDUCER -reducer $SORT_REDUCER -input topic-wordcount-output -output topic-sort-output
    echo "Done!"
    mkdir topic-sort-result/$(basename $f)
    hdfs dfs -get topic-sort-output/* topic-sort-result/$(basename $f)
done