import pylab as plt
import numpy as np

# path to PCA reduced data
path_pca = '../../data/reduced_data_pca_7PC.dat'

# path to mask identifying spectra at max
path_mask = '../../data/mask.dat'

# read reduced PCA data
op1 = open(path_pca, 'r')
lin1 = op1.readlines()
op1.close()

data1 = [elem.split() for elem in lin1]

# construct data matrix
matrix = np.array([[float(item) for item in line] for line in data1])

# read mask
op2 = open(path_mask, 'r')
lin2 = op2.readlines()
op2.close()

labels = np.array([float(elem.split()[0]) for elem in lin2])

at_max = labels == 1.0
all_spec = labels == 0.0

# plot PC1 and PC5
plt.figure()
plt.scatter(matrix[all_spec, 0], matrix[all_spec, 4], color='gray', alpha=0.6, marker='x', s=16, label='other epochs')
plt.scatter(matrix[at_max,0], matrix[at_max,4], color='red', marker='o', s=16, label='at max')
plt.xlabel('PC1', fontsize=18)
plt.ylabel('PC5', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14, loc='lower left')
plt.tight_layout()
plt.savefig('transfer_learning_scatter.pdf', format='pdf', dpi=1000)
