from sklearn.cluster import KMeans


def clustering(data, params):

    # parse arguments

    for item in params:
        if isinstance(params[item], str):
            exec(item+'='+'"'+params[item]+'"')
        else:
            exec(item+'='+str(params[item]))

    # apply KMeans to reduced data

    clusters = KMeans(n_clusters=n_clusters, init=init, tol=tol)
    clusters.fit(data)

    return [clusters.cluster_centers_, clusters.labels_]
