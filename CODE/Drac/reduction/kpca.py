from sklearn.decomposition import KernelPCA


def reduction(data, params):

    # parse parameters

    for item in params:
        if isinstance(params[item], str):
            exec(item+'='+'"'+params[item]+'"')
        else:
            exec(item+'='+str(params[item]))

    # apply PCA

    kpca = KernelPCA(n_components=n_components, kernel=kernel)
    kpca.fit(data)
    X = kpca.transform(data)

    return X
