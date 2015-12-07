from time import time
import numpy as np
import os, sys

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter

from sklearn import metrics
from sklearn import cluster,neighbors
from sklearn import manifold, datasets
from empca import empca


def reduce_dim(drname, X,niter=2000,nfriends=5,ndim=2,weight=None):
    
    n_neighbors = nfriends
    n_components = ndim #dimension
    
    
    #get dimension Reduced data
    if drname=='Isomap': Y = manifold.Isomap(n_neighbors, n_components).fit_transform(X)
    if drname=='MDS': Y = manifold.MDS(n_components, max_iter=niter, n_init=1).fit_transform(X)
    if drname=='TSNE': Y = manifold.TSNE(n_components=n_components, learning_rate=100,n_iter=niter,perplexity=5,random_state=0).fit_transform(X)
    if drname=='empca':
        # load the data and run PCA
        centered_der = X-mean(X,0)
        m = empca(centered_der, weight, nvec=5,smooth=0, niter=50)
        Y = m.coeff

        
    return Y

#-----------------

def put_ax_onfig(ndim, ax,Y,color=None,legtxt=None,mytit=None):

    if ndim==3:
        ax.scatter(Y[:, 0], Y[:, 1], Y[:, 2], c=color)
    if ndim==2:
        ax.scatter(Y[:, 0], Y[:, 1], c=color)

            
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    plt.axis('tight')
    ax.set_xlabel('I1')
    ax.set_ylabel('I2')
    
    if ndim==3:
        ax.zaxis.set_major_formatter(NullFormatter())
        ax.set_zlabel('I3')

    if mytit: ax.set_title(mytit)    
    if legtxt: ax.set_legend(legtxt,loc='best') 

    return ax
#----------------

def find_cluster(cname,X,ncluster=5,niter=2000):

    n_clusters=ncluster
    #estimate centers and number of clusters
    if cname=='KMeans':
        est=cluster.KMeans(n_clusters=n_clusters, n_init=1,init='random').fit(X)
        labels = est.labels_
        nout_clusters_=n_clusters
    if cname=='AffinityPropagation':
        est=cluster.AffinityPropagation(preference=-50).fit(X)
        cluster_centers_indices = est.cluster_centers_indices_
        nout_clusters_ = len(cluster_centers_indices)
        labels = est.labels_
    if cname=='DBSCAN':
        # Compute DBSCAN
        est = cluster.DBSCAN(eps=0.3, min_samples=3,algorithm='kd_tree').fit(X)
        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        core_samples_mask = np.zeros_like(est.labels_, dtype=bool)
        core_samples_mask[est.core_sample_indices_] = True
        labels = est.labels_
        # Number of clusters in labels, ignoring noise if present.
        nout_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    if cname=='AggC':
        # Create a graph capturing local connectivity. Larger number of neighbors
        # will give more homogeneous clusters to the cost of computation
        # time. A very large number of neighbors gives more evenly distributed
        # cluster sizes, but may not impose the local manifold structure of
        # the data        
        knn_graph = neighbors.kneighbors_graph(X, 30, include_self=False)        
        est=cluster.AgglomerativeClustering(connectivity=knn_graph,n_clusters=n_clusters, affinity='euclidean').fit(X)
        labels = est.labels_
        nout_clusters_=n_clusters

    print('Method Clustering method: %s' % cname)
    print('Estimated number of clusters: %d' % nout_clusters_)
    # print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
    # print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
    # print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
    # print("Adjusted Rand Index: %0.3f"
    #       % metrics.adjusted_rand_score(labels_true, labels))
    # print("Adjusted Mutual Information: %0.3f"
    #       % metrics.adjusted_mutual_info_score(labels_true, labels))
    # print("Silhouette Coefficient: %0.3f"
    #       % metrics.silhouette_score(X, labels))


    return est, labels,nout_clusters_

#-------------------



