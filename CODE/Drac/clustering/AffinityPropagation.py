from sklearn.cluster import AffinityPropagation
from aux import ERROR

def clustering(data, params):

    # parse arguments

    possible_keys=['preference','convergence_iter','max_iter','damping','affinity',]
    for item in params:
	if item not in possible_keys: ERROR(item)
        if isinstance(params[item], str):
            exec(item+'='+'"'+params[item]+'"')
        else:
            exec(item+'='+str(params[item]))
    
    # apply Affinity Propagation to reduced data

    AP = AffinityPropagation(preference=preference,damping=damping,max_iter=max_iter,convergence_iter=convergence_iter,affinity=affinity).fit(data)
    cluster_centers_indices =  AP.cluster_centers_indices_
    cluster_centers = AP.cluster_centers_
    labels = AP.labels_

    n_clusters = len(cluster_centers_indices)
    return [cluster_centers, labels]
