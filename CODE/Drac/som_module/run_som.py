import minisom
import numpy as np


def func(data, params):

    # parse parameters
    for item in params:
        if isinstance(params[item], str):
            exec(item+'='+'"'+params[item]+'"')
        else:
            exec(item+'='+str(params[item]))

    # set som
    som = minisom.MiniSom(nx, ny, data.shape[1], sigma=sigma,
                          learning_rate=learn_rate, random_seed=random_seed)

    # run som
    if som_type == 'random':
        som.train_random(data, int(Niter))
    elif som_type == 'batch':
        som.train_batch(data, int(Niter))

    # get and save som output
    w = np.array([som.winner(item) for item in data])
    np.savetxt('som_res/som_index.dat', w, fmt="%d %d")

    return
