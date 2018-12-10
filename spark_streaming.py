from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: network_wordcount.py <hostname> <port>", file=sys.stderr)
        exit(-1)
    # Create a local StreamingContext with two working thread and batch interval of 1 second
    sc = SparkContext(appName="TweetsStreaming")
    ssc = StreamingContext(sc, 1)

    # Create a DStream that will connect to hostname:port, like localhost:9999
    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    # Count each word in each batch
    counts = lines.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)
    # Print the first ten elements of each RDD generated in this DStream to the console
    counts.pprint()

    # Start the computation
    ssc.start()
    # Wait for the computation to terminate
    ssc.awaitTermination()
