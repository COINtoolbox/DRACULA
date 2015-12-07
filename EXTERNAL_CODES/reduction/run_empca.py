import os
import tarfile
from numpy import loadtxt, mean,ones, var
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim
import sys

data_dir='../../data_all_types/'
out_dir='./plots/'

nvec=25
niter=100

url_empca = "https://raw.githubusercontent.com/sbailey/empca/master/empca.py"


# Download empca.py file


if "empca.py" not in os.listdir("./"):
	
	os.system(  "wget %s"%url_empca )

from empca import empca	
	

derivatives = loadtxt(os.path.join(data_dir,'derivatives.dat') )



errors = ones(derivatives.shape)

labels = loadtxt(data_dir+'labels.dat')


centered_der = derivatives-mean(derivatives,0)

#m = empca(centered_der, 1./(errors)**2, nvec=5,smooth=0, niter=50)
m = empca(centered_der, 1./(errors)**2, nvec=nvec,smooth=0, niter=niter)

X = m.coeff

## plot the results
colors_vec=[]
for i in labels:
    if i ==1:
        colors_vec.append('r')
    if i ==0:
        colors_vec.append('w')

for indexes in [[0,i] for i in range(25)]:
    figure()
    scatter(X[:, indexes[0]], X[:, indexes[1]], c=colors_vec, marker='.',linewidth=.1)
    xlabel('PC %d' % (indexes[0]+1))
    ylabel('PC %d' % (indexes[1]+1))
    axis('equal')
    savefig(out_dir+'scatter_plot_%d_%d.png' % (indexes[0]+1,indexes[1]+1))

figure();plot(var(X,0),'o')
savefig(out_dir+'variances.png')

