from sklearn.decomposition import KernelPCA
from aux import ERROR


def reduction(data, params):

    # parse parameters

    possible_keys=['n_components','kernel',]
    for item in params:
	if item not in possible_keys: ERROR(item)
        if isinstance(params[item], str):
            exec(item+'='+'"'+params[item]+'"')
        else:
            exec(item+'='+str(params[item]))

    # apply PCA

    kpca = KernelPCA(n_components=n_components, kernel=kernel)
    kpca.fit(data)
    X = kpca.transform(data)

    return X
