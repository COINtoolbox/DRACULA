import pylab as plt
from numpy import loadtxt, genfromtxt, savetxt, var, random
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim, ylim, legend

data_to_plot = loadtxt('../../data/residuals.dat').T

plt.figure()
plt.scatter(data_to_plot[0], data_to_plot[3],marker='*', label='DL at max', color='gray',s=50)
plt.scatter(data_to_plot[0], data_to_plot[4],marker='o', label='DL with TL', color='black', s=40)
plt.ylabel('fractional variance', fontsize=22)
plt.xlabel('features', fontsize=22)
plt.ylim(0,1)
plt.legend(fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.tight_layout()
plt.savefig('FV_TL_DL.pdf', format='pdf', dpi=1000)


data_to_plot = loadtxt('../../data/residuals_all_matrix.dat').T
plt.figure()
plt.scatter(data_to_plot[0], data_to_plot[1],marker='o', color='red', label='PCA with TL', s=40)
plt.scatter(data_to_plot[0], data_to_plot[2],marker='s', color='black', label='DL with TL', s=40)
plt.ylabel('fractional variance', fontsize=22)
plt.xlabel('features/PCs', fontsize=22)
plt.ylim(0,1)
plt.legend(fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.tight_layout()
plt.savefig('FV_PCA_vs_DL.pdf', format='pdf', dpi=1000)

