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



