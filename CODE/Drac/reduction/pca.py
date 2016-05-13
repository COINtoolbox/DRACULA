from sklearn.decomposition.pca import PCA
from aux import ERROR


def reduction(data, params):

    # parse parameters

    possible_keys=['components',]
    for item in params:
	if item not in possible_keys: ERROR(item)
        if isinstance(params[item], str):
            exec(item+'='+'"'+params[item]+'"')
        else:
            exec(item+'='+str(params[item]))

    # apply PCA

    pca = PCA(n_components=n_components)
    pca.fit(data)
    X = pca.transform(data)

    return X
