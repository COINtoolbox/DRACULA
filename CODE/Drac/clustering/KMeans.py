from sklearn.cluster import KMeans
from aux import ERROR


def clustering(data, params):

    # parse arguments

    possible_keys=['n_clusters','tol','init','n_jobs',]
    for item in params:
	if item not in possible_keys: ERROR(item)
        if isinstance(params[item], str):
            exec(item+'='+'"'+params[item]+'"')
        else:
            exec(item+'='+str(params[item]))

    # apply KMeans to reduced data

    clusters = KMeans(n_clusters=n_clusters, init=init, tol=tol)
    clusters.fit(data)

    return [clusters.cluster_centers_, clusters.labels_]
