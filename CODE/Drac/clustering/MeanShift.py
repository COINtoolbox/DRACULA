from sklearn.cluster import MeanShift, estimate_bandwidth
from aux import ERROR


def clustering(data, params):

    # parse arguments

    possible_keys=['quantile','cluster_all',]
    for item in params:
	if item not in possible_keys: ERROR(item)
        if isinstance(params[item], str):
            exec(item+'='+'"'+params[item]+'"')
        else:
            exec(item+'='+str(params[item]))

    # apply Mean Shift to reduced data

    bandwidth = estimate_bandwidth(data, quantile=quantile)
    clusters = MeanShift(bandwidth, cluster_all=cluster_all)
    clusters.fit(data)

    return [clusters.cluster_centers_, clusters.labels_]
