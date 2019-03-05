# -*- coding = UTF-8 -*-
import numpy as np
import operator
from os import listdir
import scipy as sc
from sklearn.neighbors import KNeighborsClassifier  as KNN


def Test():
    X=[[0],[1],[2],[3],[4],[5],[6],[7],[8]]
    Y=[0,0,0,1,1,1,2,2,2]
    neigh=KNN(n_neighbors=3)
    neigh.fit(X,Y)
    print(neigh.predict([[6.1]]))

def trainingarray():
    trainMat=np.array([[1,2,3],[2,3,5],[55,33,66],[55,44,66]])
    label=np.array([0,0,1,1])
    neigh=KNN(n_neighbors=3,algorithm='auto',weights='distance',n_jobs=1 )
    neigh.fit(trainMat,label)
    testmat=np.array([[2,3,4],[55,33,66]])
    print(neigh.predict(testmat))


if __name__== "__main__":
    trainingarray()