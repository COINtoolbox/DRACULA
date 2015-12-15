from __future__ import print_function
from sklearn.metrics import silhouette_score
import numpy as np


def quality(data_red, cluster_centers, cluster_labels, params):

    # parse arguments
    for item in params:
        if isinstance(params[item], str):
            exec(item+'='+'"'+params[item]+'"')
        else:
            exec(item+'='+str(params[item]))

    # numbers of clusters and samples
    
    n_clusters = len(np.unique(cluster_labels))

    # check n_clusters > 1

    if n_clusters <= 1:
        # raise ValueError('Number of clusters should be > 1 for computing silhouette index')
        print('\tERROR: Number of clusters should be > 1 for computing silhouette index')
        q = np.nan
    else:
        q = silhouette_score(data_red, cluster_labels, metric=metric)

    return q
