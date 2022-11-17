# Apache Spark
A multi-language engine for executing data engineering, data science, and machine learning on single-node machines or clusters.
- Batch/streaming data
- SQL analytics
- Data science at scale
- Machine learning

# PySpark
PySpark is an interface for Apache Spark in Python. It not only allows you to write Spark applications using Python APIs, but also provides the PySpark shell for interactively analyzing your data in a distributed environment. PySpark supports most of Spark’s features such as - 
- Spark SQL - structured data processing. It provides a programming abstraction called DataFrame and can also act as distributed SQL query engine.
- DataFrame
  - Pandas API on Spark
  - Have a single codebase that works both with pandas (tests, smaller datasets) and with Spark (distributed datasets).
  - Switch to pandas API and PySpark API contexts easily without any overhead.
- Streaming - the streaming feature in Apache Spark enables powerful interactive and analytical applications across both streaming and historical data
- MLlib - scalable machine learning library
- Spark Core - 
  - Underlying general execution engine for the Spark platform
  - Provides an RDD (Resilient Distributed Dataset) and in-memory computing capabilities.

## Resilient Distributed Datasets
Spark revolves around the concept of a resilient distributed dataset (RDD), which is a fault-tolerant collection of elements that can be **operated on in parallel**. There are two ways to create RDDs: 
- Parallelizing an existing collection in your driver program, or
- Referencing a dataset in an external storage system, such as a shared filesystem, `HDFS`, `HBase`, or any data source offering a `Hadoop InputFormat`.
- RDDs are created by starting with a file in the Hadoop file system (or any other Hadoop-supported file system)
- A second abstraction in Spark is shared variables that can be used in parallel operations

## PySpark DataFrames
They are lazily evaluated. They are implemented on top of RDDs. When Spark transforms data, it does not immediately compute the transformation but plans how to compute later. When actions such as `collect()` are explicitly called, the computation starts.