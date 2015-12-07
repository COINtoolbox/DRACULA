from time import time

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
import numpy as np
import os, sys

import numpy as np
from sklearn import metrics
from sklearn import cluster,neighbors
from sklearn import manifold, datasets

import sncolor as myc
from docluster import *


# Next line to silence pyflakes. This import is needed.
Axes3D

#n_points = 1000
#X, color = datasets.samples_generator.make_s_curve(n_points, random_state=0)


path1 = '../../empca_trained_coeff/sne.dat'
path2='../../empca_trained_coeff/coefficients.dat'

# read data
X = np.loadtxt(path2)
n_points=len(X[:,0])


#'Branch'
sne_name = np.loadtxt(path1,dtype=str)
leg_type='Branch'
color,marks,cm_name = myc.load_colors(sne_name,type=leg_type)

n_clusters = len(cm_name['name'])

y=color

figdir='figures/' #'plots_' + case + '/'
if not os.path.isdir(figdir):
    os.makedirs(figdir)


# drmethods=['Isomap','MDS','TSNE']
# cmethods=['KMeans','AffinityPropagation','DBSCAN','AggC']

drmethods=['Isomap']
cmethods=['AggC']

niter=2000
sniter='2e3'
n_neighbors = 5 #nfriends
n_components = 2#ndim #dimension
    
for drname in drmethods:
    for cname in cmethods:

        case = drname+'_vs_'+cname+'_D'+str(n_components)

        Y = reduce_dim(drname,X,ndim=2)        
        #plot dimension reduced data
        fig = plt.figure(figsize=(15, 8))
        if n_components==3:
            ax = fig.add_subplot(121, projection='3d', elev=48, azim=134)
        if n_components==2:
            ax = fig.add_subplot(121)
        put_ax_onfig(n_components,ax,Y,color,mytit=drname)

        
        est, labels,nout_clusters_ = find_cluster(cname, X,ncluster=5,niter=2000)
        #second plot from clustering
        if n_components==3:
            ax = fig.add_subplot(122, projection='3d', elev=48, azim=134)
            ax.scatter(Y[:, 0], Y[:, 1], Y[:, 2], c=labels.astype(np.float))
        if n_components==2:
            ax = fig.add_subplot(122)
            ax.scatter(Y[:, 0], Y[:, 1], c=labels.astype(np.float))
        put_ax_onfig(n_components,ax,Y,labels,mytit=cname)            

        #plt.show()
        plt.savefig(figdir+'/plot_'+case+'_'+leg_type+'_niter'+sniter+'.png')



#tt2 = np.hstack( (gc.Y, tt.transpose()))
#tt=np.vstack( (zz,gc.labels.astype(np.float) ) )
#mm2=['y', 'g', 'r', 'b', 'k']
#zz=[1.0*mm2.index(a) for a in gc.color]
