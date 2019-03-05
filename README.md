# KNeighborsClassifier

K近邻分类器

class sklearn.neighbors.KNeighborsClassifier
(n_neighbors=5, weights=’uniform’, algorithm=’auto’, leaf_size=30, p=2, metric=’minkowski’, metric_params=None, n_jobs=None, **kwargs)[source]

fit(X, y)	                                      
Fit the model using X as training data and y as target values

get_params([deep])	                            
Get parameters for this estimator.

kneighbors([X, n_neighbors, return_distance])	  
Finds the K-neighbors of a point.

kneighbors_graph([X, n_neighbors, mode])	      
Computes the (weighted) graph of k-Neighbors for points in X

predict(X)	                                    
Predict the class labels for the provided data

predict_proba(X)	                             
Return probability estimates for the test data X.

score(X, y[, sample_weight])	                 
Returns the mean accuracy on the given test data and labels.

set_params(**params)	                          
Set the parameters of this estimator.
