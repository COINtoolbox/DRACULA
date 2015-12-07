from sklearn.cluster import MeanShift, estimate_bandwidth


def clustering(data, params):

    # parse arguments

    for item in params:
        if isinstance(params[item], str):
            exec(item+'='+'"'+params[item]+'"')
        else:
            exec(item+'='+str(params[item]))

    # apply Mean Shift to reduced data

    bandwidth = estimate_bandwidth(data, quantile=quantile)
    clusters = MeanShift(bandwidth, cluster_all=cluster_all)
    clusters.fit(data)

    return [clusters.cluster_centers_, clusters.labels_]
