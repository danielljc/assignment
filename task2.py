from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]")
sc = SparkContext(conf=conf)

dataRdd = sc.textFile("/Users/Daniel/Downloads/data.txt")

rdd2 = dataRdd.map(lambda str: (str.split(",")[0], float(str.split(",")[1])))

rdd3 = rdd2.reduceByKey(lambda a, b: a + b).map(lambda t: (t[1], t[0]))

topK = rdd3.sortByKey(False).map(lambda t: str(t[1])).take(int(5))

print(topK)
