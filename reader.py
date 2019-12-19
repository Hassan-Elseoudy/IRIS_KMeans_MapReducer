from mapper import getCentroids

#Check if distance of centroids and centroids1 is less than tolerance
def checkCentroidsDistance(centroids, centroids1):
    tol = 1e-4
    C1a = abs(centroids[0][0] - centroids1[0][0]) < tol
    C1b = abs(centroids[0][1] - centroids1[0][1]) < tol
    C1c = abs(centroids[0][2] - centroids1[0][2]) < tol
    C1d = abs(centroids[0][3] - centroids1[0][3]) < tol
    C2a = abs(centroids[1][0] - centroids1[1][0]) < tol
    C2b = abs(centroids[1][1] - centroids1[1][1]) < tol
    C2c = abs(centroids[1][2] - centroids1[1][2]) < tol
    C2d = abs(centroids[1][3] - centroids1[1][3]) < tol
    C3a = abs(centroids[2][0] - centroids1[2][0]) < tol
    C3b = abs(centroids[2][1] - centroids1[2][1]) < tol
    C3c = abs(centroids[2][2] - centroids1[2][2]) < tol
    C3d = abs(centroids[2][3] - centroids1[2][3]) < tol


    if C1a and C1b and C1c and C1d and C2a and C2b and C2c and C2d and C3a and C3b and C3c and C3d:
        print(1) # So the runner script ends.
    else:
        print(0)

if __name__ == "__main__":
    centroids = getCentroids('Dataset_Centroids/centroids.txt')
    centroids1 = getCentroids('Dataset_Centroids/centroids1.txt')
    
    checkCentroidsDistance(centroids, centroids1)
