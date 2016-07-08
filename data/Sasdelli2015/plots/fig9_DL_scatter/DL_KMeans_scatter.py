import pylab as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# path to DL results
path_small_space = '../../data/DL_4features_all_epochs.dat'

# path to spectra ID
path_id = '../../data/spectra_data_id.dat'

# path to kmeans result
path_kmeans = '../../data/clustering_KMeans_label_4features_4groups.dat'

# color for plotting
c = [ 'green', 'red', 'blue', 'orange']

# markers for ploting
mark =  ['^','o',  's', 'd', '*']

# marker size
ss = [60, 40, 40, 60]

# read spectra ID
op2 = open(path_id, 'r')
lin2 = op2.readlines()
op2.close()

names_all = [elem.split() for elem in lin2[1:]]

# read DL results
op1 = open(path_small_space, 'r')
lin1 = op1.readlines()
op1.close()

data1 = [elem.split() for elem in lin1]

matrix = np.array([[float(item) for item in data1[i]] for i in xrange(len(data1)) if names_all[i][-1]=='1'])

# read kmeans results
op3 = open(path_kmeans, 'r')
lin3 = op3.readlines()
op3.close()

classes = np.array([float(elem.split()[0]) for elem in lin3])
group1 = classes == 0.0
group2 = classes == 1.0
group3 = classes == 2.0
group4 = classes == 3.0

# plot only DL results
fig = plt.figure(figsize=(20,14))
plt.subplot(4,4,1)
panels = []
panels.append(plt.scatter(matrix[group1,0], matrix[group1,0], lw='0',marker=mark[0],s=ss[0], color=c[0]))
panels.append(plt.scatter(matrix[group2,0], matrix[group2,0], lw='0',marker=mark[1],s=ss[1], color=c[1]))
panels.append(plt.scatter(matrix[group3,0], matrix[group3,0], lw='0',marker=mark[2],s=ss[2], color=c[2]))
panels.append(plt.scatter(matrix[group4,0], matrix[group4,0], lw='0',marker=mark[3],s=ss[3], color=c[3]))
plt.ylabel('feature 1', fontsize=26)
plt.xticks([])
plt.yticks(fontsize=22)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)


plt.subplot(4,4,5)
plt.scatter(matrix[group1,0], matrix[group1,1], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,0], matrix[group2,1], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.scatter(matrix[group3,0], matrix[group3,1], lw='0',marker=mark[2],s=ss[2], color=c[2])
plt.scatter(matrix[group4,0], matrix[group4,1], lw='0',marker=mark[3],s=ss[3], color=c[3])
plt.ylabel('feature 2', fontsize=26)
plt.xticks([])
plt.yticks(fontsize=22)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)


plt.subplot(4,4,6)
plt.scatter(matrix[group1,1], matrix[group1,1], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,1], matrix[group2,1], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.scatter(matrix[group3,1], matrix[group3,1], lw='0',marker=mark[2],s=ss[2], color=c[2])
plt.scatter(matrix[group4,1], matrix[group4,1], lw='0',marker=mark[3],s=ss[3], color=c[3])
plt.xticks([])
plt.yticks([])

plt.subplot(4,4,9)
plt.scatter(matrix[group1,0], matrix[group1,2], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,0], matrix[group2,2], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.scatter(matrix[group3,0], matrix[group3,2], lw='0',marker=mark[2],s=ss[2], color=c[2])
plt.scatter(matrix[group4,0], matrix[group4,2], lw='0',marker=mark[3],s=ss[3], color=c[3])
plt.ylabel('feature 3', fontsize=26)
plt.xticks([])
plt.yticks(fontsize=22)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)


plt.subplot(4,4,10)
plt.scatter(matrix[group1,1], matrix[group1,2], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,1], matrix[group2,2], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.scatter(matrix[group3,1], matrix[group3,2], lw='0',marker=mark[2],s=ss[2], color=c[2])
plt.scatter(matrix[group4,1], matrix[group4,2], lw='0',marker=mark[3],s=ss[3], color=c[3])
plt.xticks([])
plt.yticks([])

plt.subplot(4,4,11)
plt.scatter(matrix[group1,2], matrix[group1,2], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,2], matrix[group2,2], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.scatter(matrix[group3,2], matrix[group3,2], lw='0',marker=mark[2],s=ss[2], color=c[2])
plt.scatter(matrix[group4,2], matrix[group4,2], lw='0',marker=mark[3],s=ss[3], color=c[3])
plt.xticks([])
plt.yticks([])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)


plt.subplot(4,4,13)
plt.scatter(matrix[group1,0], matrix[group1,3], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,0], matrix[group2,3], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.scatter(matrix[group3,0], matrix[group3,3], lw='0',marker=mark[2],s=ss[2], color=c[2])
plt.scatter(matrix[group4,0], matrix[group4,3], lw='0',marker=mark[3],s=ss[3], color=c[3])
plt.ylabel('feature 4', fontsize=26)
plt.xlabel('feature 1', fontsize=26)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)


plt.subplot(4,4,14)
plt.scatter(matrix[group1,1], matrix[group1,3], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,1], matrix[group2,3], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.scatter(matrix[group3,1], matrix[group3,3], lw='0',marker=mark[2],s=ss[2], color=c[2])
plt.scatter(matrix[group4,1], matrix[group4,3], lw='0',marker=mark[3],s=ss[3], color=c[3])
plt.xlabel('feature 2', fontsize=26)
plt.yticks([])
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xticks(fontsize=22)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)


plt.subplot(4,4,15)
plt.scatter(matrix[group1,2], matrix[group1,3], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,2], matrix[group2,3], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.scatter(matrix[group3,2], matrix[group3,3], lw='0',marker=mark[2],s=ss[2], color=c[2])
plt.scatter(matrix[group4,2], matrix[group4,3], lw='0',marker=mark[3],s=ss[3], color=c[3])
plt.xlabel('feature 3',fontsize=26)
plt.yticks([])
plt.xticks(fontsize=22)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)


plt.subplot(4,4,16)
plt.scatter(matrix[group1,3], matrix[group1,3], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,3], matrix[group2,3], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.scatter(matrix[group3,3], matrix[group3,3], lw='0',marker=mark[2],s=ss[2], color=c[2])
plt.scatter(matrix[group4,3], matrix[group4,3], lw='0',marker=mark[3],s=ss[3], color=c[3])
plt.xlabel('feature 4', fontsize=26)
plt.yticks([])
plt.xticks(fontsize=22)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplots_adjust(left=0.075, right=0.975, top=0.975, bottom=0.075,hspace=0.0,wspace=0.0)
legs=fig.legend(panels, ['Group 1', 'Group 2', 'Group 3', 'Group 4'], loc = (0.770, 0.778), title='Kmeans classfication', fontsize=26)
plt.setp(legs.get_title(),fontsize=26)
plt.savefig("DL_KMeans_scatter_4g.pdf", format='pdf',dpi=1000)

