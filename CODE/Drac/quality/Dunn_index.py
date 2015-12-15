from sklearn.metrics import *
import numpy as np


def quality(X, cluster_centers, cluster_labels, params):

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
                # raise ValueError('Number of clusters should be > 1 for computing Dunn index')
                print('\tERROR: Number of clusters should be > 1 for computing Dunn index')
                return np.nan
        else:

                # intra-cluster mean distance

                distances = pairwise_distances(X, metric=metric)
                dX = np.array([_intra_cluster_distance(distances[i],
                               cluster_labels, i) for i in range(n_clusters)])

                # distance between cluster centers

                dist_centers = pairwise_distances(cluster_centers, metric=metric)

                # S[i][j] = d(ci,cj)/max(dX)

                np.fill_diagonal(dist_centers, np.inf)  # guarantee Sii bigger enough
                S = dist_centers / np.amax(dX)

                # return min of S

                return np.amin(S)
    

def _intra_cluster_distance(distances_row, labels, i):

        """Calculate the mean intra-cluster distance for sample i.
        Parameters
        ----------
        
        distances_row : array, shape = [n_samples]
        Pairwise distance matrix between sample i and each sample.
        labels : array, shape = [n_samples]
        label values for each sample
        
        i : int
        Sample index being calculated. It is excluded from calculation and
        used to determine the current labels
        
        Returns
        -------
        
        a : float
        Mean intra-cluster distance for sample i
        """
    
        mask = labels == labels[i]
        mask[i] = False
        a = np.mean(distances_row[mask])
        
        return a
