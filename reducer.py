#!/usr/bin/env python
"""reducer.py"""

import sys

def calculateNewCentroids():
    global centroid_index
    current_centroid = None
    sum_a = 0
    sum_b = 0
    sum_c = 0
    sum_d = 0
    count = 0

    # input comes from STDIN
    for line in sys.stdin:
        # Get (Centroid Index) and (Features)
        centroid_index, a, b, c, d = line.split('\t')

        # Floating the features
        try:
            a = float(a)
            b = float(b)
            c = float(c)
            d = float(d)
        except ValueError:
            # Just handling the ValueError
            continue

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: centroid_index) before it is passed to the reducer
        if current_centroid == centroid_index:
            count += 1
            sum_a += a
            sum_b += b
            sum_c += c
            sum_d += d
        else:
            if count != 0:
                # Cluster Features Mean
                print(str(sum_a / count) + ", " + str(sum_b / count) + ", " + str(sum_c / count) + ", " + str(
                    sum_d / count))

            current_centroid = centroid_index
            sum_a = a
            sum_b = b
            sum_c = c
            sum_d = d
            count = 1

    # Cluster #3
    if current_centroid == centroid_index and count != 0:
        print(str(sum_a / count) + ", " + str(sum_b / count) + ", " + str(sum_c / count) + ", " + str(sum_d / count))


if __name__ == "__main__":
    calculateNewCentroids()
