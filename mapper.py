#!/usr/bin/env python
"""mapper.py"""

__authors__ = "Hassan Elseoudy, Ziad Magdy"

import sys
from math import sqrt


# get initial centroids from a txt file and add them in an array
def getCentroids(filepath):
    centroids = []

    with open(filepath) as fp:
        line = fp.readline()
        while line:
            if line:
                try:
                    line = line.strip()
                    features = line.split(', ')
                    centroids.append([float(features[0]), float(features[1]), float(features[2]), float(features[3])])
                except:
                    break
            else:
                break
            line = fp.readline()

    fp.close()
    return centroids


# create clusters based on initial centroids
def createClusters(centroids):
    for line in sys.stdin:
        line = line.strip()
        features = line.split(',')
        min_dist = 1e9
        index = -1

        for centroid, i in zip(centroids, range(3)):
            try:
                features[0] = float(features[0])
                features[1] = float(features[1])
                features[2] = float(features[2])
                features[3] = float(features[3])
            except ValueError:
                continue

            # Euclidean distance from every point of data set to every centroid
            cur_dist = sqrt(pow(features[0] - centroid[0], 2) + pow(features[1] - centroid[1], 2) + pow(features[2] - centroid[2],2) + pow(features[3] - centroid[3], 2))

            # find the centroid which is closer to the point
            if cur_dist <= min_dist:
                min_dist = cur_dist
                index = i

        var = "%s\t%s\t%s\t%s\t%s" % (index, features[0], features[1], features[2], features[3])
        print(var)


if __name__ == "__main__":
    centroids = getCentroids('centroids.txt')
    createClusters(centroids)