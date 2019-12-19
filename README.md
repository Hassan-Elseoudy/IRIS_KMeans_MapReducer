# IRIS_KMeans_MapReducer
Implementation of KMeans Algorithm on IRIS dataset using Hadoop MapReducer Programming Framework 3.1.2

The goal of the project is to determine the 3 centroids of the IRIS dataset. 
First you have to run the follwoing command:
`bin/hadoop dfs -copyFromLocal /home/smsm/Documents/Hadoop/IRIS_KMeans_MapReducer/Dataset_Centroids /user/smsm/`

In my case `/home/smsm/Documents/Hadoop/IRIS_KMeans_MapReducer/Dataset_Centroids` was the directory where it contained the dataset.txt, centroids.txt and centroids1.txt) and `/user/smsm/` was the defauld hdfs location.

you have to make sure that you gave permissions to mapper and reducer files.

```
chmod +x /home/smsm/Documents/Hadoop/IRIS_KMeans_MapReducer/mapper.py
chmod +x /home/smsm/Documents/Hadoop/IRIS_KMeans_MapReducer/reducer.py
```

Then you have to run `./run.sh` command 

Explanation for `./run.sh` 

``` bash
#!/bin/bash
i=1
while :
do
	hadoop jar /home/smsm/Documents/Hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar \
	-file /home/smsm/Documents/Hadoop/IRIS_KMeans_MapReducer/Dataset_Centroids/centroids.txt \
	-file /home/smsm/Documents/Hadoop/IRIS_KMeans_MapReducer/mapper.py -mapper /home/smsm/Documents/Hadoop/IRIS_KMeans_MapReducer/mapper.py \
	-file /home/smsm/Documents/Hadoop/IRIS_KMeans_MapReducer/reducer.py -reducer /home/smsm/Documents/Hadoop/IRIS_KMeans_MapReducer/reducer.py\
	-input /user/smsm/Dataset_Centroids/dataset.txt -output /user/smsm/SZ$i
	rm -f Dataset_Centroids/centroids1.txt
	hadoop fs -copyToLocal /user/smsm/SZ$i/part-00000 Dataset_Centroids/centroids1.txt
	seeiftrue=`python /home/smsm/Documents/Hadoop/IRIS_KMeans_MapReducer/reader.py`
	if [ $seeiftrue = 1 ]
	then
		rm Dataset_Centroids/centroids.txt
		hadoop fs -copyToLocal /user/smsm/SZ$i/part-00000 Dataset_Centroids/centroids.txt
		break
	else
		rm Dataset_Centroids/centroids.txt
		hadoop fs -copyToLocal /user/smsm/SZ$i/part-00000 Dataset_Centroids/centroids.txt
	fi
	i=$((i+1))
done

```
Script keeps comparing between `centroids.txt` and `centroids1.txt` file (Which is copied from the output of Reducer), and if there's almost no change, it prints out the result, it runs for `i` times, till it satifies the tolerance found in `reader.py`

`/home/smsm/Documents/Hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar` : The path of hadoop-streaming jar file.


<img src="https://i.ibb.co/GWF7xbQ/image.png" alt="image" border="0">

Output:

C1: [5.006 		3.418 			1.464 			0.24400000000]

C2: [5.90161290323 	2.74838709677 	4.3935483871		1.43387096774]	

C3: [6.85 		3.07368421053 	5.74210526316 	2.07105263158]	
