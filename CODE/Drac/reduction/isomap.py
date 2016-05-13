from sklearn import manifold
from aux import ERROR


def reduction(data, params):

    # parse parameters

    possible_keys=['n_neighbors','n_components','eigen_solver','tol','max_iter','path_method','neighbors_algorithm',]
    for item in params:
	if item not in possible_keys: ERROR(item)
        if isinstance(params[item], str):
            exec(item+'='+'"'+params[item]+'"')
        else:
            exec(item+'='+str(params[item]))

    # apply ISOMAP

    X = manifold.Isomap(n_neighbors=n_neighbors, n_components=n_components, eigen_solver=eigen_solver, tol=tol, max_iter = max_iter, path_method=path_method,neighbors_algorithm=neighbors_algorithm).fit_transform(data)
    
    return X
