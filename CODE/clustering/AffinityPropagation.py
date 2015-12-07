from sklearn.cluster import AffinityPropagation

def clustering(data, params):

    # parse arguments

    for item in params:
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
