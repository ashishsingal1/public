# Hadoop Notes
From course: https://classroom.udacity.com/courses/ud617

Three V's:
 - Velocity
 - Volume
 - Variety
 
When to use big data? When it is too big for a single machine.

Hadoop ecosystem:
 - HDFS - Distributed file system
 - Map Reduce - Querying tool
 - Pig / Hive - Turns queries into MR
 - Impala - Directly query HDFS using SQL-like

HDFS:
 - 64MB blocks by default
 - DataNode runs on each machine
 - NameNode has metadata. Replicated by NameNode standby
 - 3 replications per block

MapReduce:
 - Mappers process blocks - key, value
 - Send to reducers to glue together - shuffle and sort

Jobs:
 - Job tracker - keeps up with the tasks
 - Task tracker - runs on each DN machine
 
MRCode:
 - Mapper - moves it to key->value
 - Hadoop Streaming - Can write in any language
 - Reducer - add everything up
 
Patterns
 - Filtering - simple, random sampling, bloom
 - Summarizing
 - Structural
 - Top N - each mapper selects the local top 10, then reducer selects global top 10
 - inverted index - 
 - combiners - pre-reduction
 - RMDBS > Hadoop
