from sklearn import manifold


def reduction(data, params):

    # parse parameters

    for item in params:
        if isinstance(params[item], str):
            exec(item+'='+'"'+params[item]+'"')
        else:
            exec(item+'='+str(params[item]))

    # apply ISOMAP

    X = manifold.Isomap(n_neighbors=n_neighbors, n_components=n_components, eigen_solver=eigen_solver, tol=tol, max_iter = max_iter, path_method=path_method,neighbors_algorithm=neighbors_algorithm).fit_transform(data)
    
    return X
