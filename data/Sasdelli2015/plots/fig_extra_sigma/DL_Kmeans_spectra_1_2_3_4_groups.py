import pylab as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

def load_colors(sne_list,type='Wang'):

    import urllib
    import numpy
    
    op1=open('../../data/wang_data.txt','r')
    lin1 = op1.readlines()
    op1.close()
    data1 = [elem[:16].split()[0] for elem in lin1[51:]]
    data2 = [elem[41:].split() for elem in lin1[51:]]
    
    for i in range(numpy.shape(data2)[0]):
        if numpy.size(data2[i])==1:
            data2[i]= [ data2[i][0],'nan']
    
    if type=='Wang':
        name_dict={'name':['HV','N','91bg','91T','nan'],
                   'color':['y','g','c','r','b'],
                   'mark':[u"s",u"o",u"2",u"D",u"*"]}

        index=1
    if type=='Branch':
        name_dict={'name':['BL','CN','CL','SS'],
                   'color':['y','g','r','b'],
                   'mark':[u"s",u"o",u"2",u"D"]}
        index=0

    col_=[name_dict['name'],name_dict['color']]
    mark_=[name_dict['name'],name_dict['mark']]
    color_list=[]
    shape_list=[]
    for i in sne_list:
        if i[2:] in data1:
            color_list.append( col_[1][col_[0].index(data2[data1.index(i[2:])][index])])
            shape_list.append(mark_[1][mark_[0].index(data2[data1.index(i[2:])][index])])
        else:
            color_list.append('k')
            shape_list.append(u'x')
    return color_list,shape_list,name_dict
###############################################################################################

# path to DL results
path_small_space = '../../data/DL_4features_all_epochs.dat'

# path to spectra ID
path_id = '../../data/spectra_data_id.dat'

# path to original spectra
path_spectra = '../../data/fluxes_all_epochs.dat'

# path to kmeans result 
path_kmeans_4g = '../../data/clustering_KMeans_label_4features_4groups.dat'

# read kmeans result 4 groups
op5 = open(path_kmeans_4g, 'r')
lin5 = op5.readlines()
op5.close()

kmeans_classes = [float(elem.split()[0]) for elem in lin5]

# read spectra ID
op2 = open(path_id, 'r')
lin2 = op2.readlines()
op2.close()

names_all = [elem.split() for elem in lin2[1:]]
names_max = [names_all[i][0] for i in xrange(len(names_all)) if names_all[i][-1] == '1']


# read original spectra
op4 = open(path_spectra, 'r')
lin4 = op4.readlines()
op4.close()

data4 = [elem.split() for elem in lin4]

data_spectra = np.array([[float(item) for item in line] for line in data4])

# build wang color code 
color_wang = load_colors(names_max)

# separate groups accorging to wang classification
wang_spectra = []
for cor in color_wang[2]['color'][:-1]:
    spectra_temp = []
    cont = 0
    for j in xrange(len(data_spectra)):
        if names_all[j][-1] == '1':
            cont = cont + 1
            if color_wang[0][cont - 1] == cor:
                spectra_temp.append(data_spectra[j])
            
    spectra_temp = np.array(spectra_temp)
    wang_spectra.append(spectra_temp)

wang_spectra = np.array(wang_spectra)

spectra_group = []
std_group = []
for j in xrange(len(wang_spectra)):
    spectra_group.append([np.mean(wang_spectra[j][:,l]) for l in xrange(len(wang_spectra[j][0]))])
    std_group.append([np.std(wang_spectra[j][:,l]) for l in xrange(len(wang_spectra[j][0]))])

spectra_group = np.array(spectra_group)
std_group = np.array(std_group)


# separate groups according to kmeans classification 4 groups
groups_kmeans = []
for item in xrange(4):
    kmeans_temp = []
    cont = 0
    for j in xrange(len(data_spectra)):
        if names_all[j][-1] == '1':
            cont = cont + 1
            if kmeans_classes[cont - 1] == item:
                kmeans_temp.append(data_spectra[j])

    groups_kmeans.append(np.array(kmeans_temp))

group_kmeans = np.array(groups_kmeans)
kmeans_rep = [np.array([np.mean(group_kmeans[ll][:,jj]) for jj in xrange(len(data_spectra[0]))]) for ll in xrange(len(groups_kmeans))]
kmeans_std = [np.array([np.std(group_kmeans[ll][:,jj]) for jj in xrange(len(data_spectra[0]))]) for ll in xrange(len(groups_kmeans))]
xaxes = [4000 + 10*ll for ll in xrange(len(data_spectra[0]))]


plt.figure()
plt.plot(xaxes, kmeans_rep[0], label='k g1', color='red')
plt.plot(xaxes, spectra_group[0], label='w HV', color='red', ls='--')

plt.plot(xaxes, kmeans_rep[1] + 1.0, label='k g2', color='blue')
plt.plot(xaxes, spectra_group[1] + 1.0, label='w N', color='blue', ls='--')

plt.plot(xaxes, kmeans_rep[2] + 2.0, label='k g3', color='green')
plt.plot(xaxes, spectra_group[2]+2.0, label='w 91bg', color='green', ls='--')

plt.plot(xaxes, kmeans_rep[3]+3.0, label='k g4', color='orange')
plt.plot(xaxes, spectra_group[3]+3.0, label='w 91T', color='orange', ls='--')
plt.show()

plt.figure()
plt.subplot(1,4,1)
plt.hist(kmeans_std[0], color='blue', label='kmeans g1')
plt.hist(std_group[0], color='green', label='wang HV')
plt.legend()

plt.subplot(1,4,2)
plt.hist(kmeans_std[1], color='blue', label='kmeans g2')
plt.hist(std_group[1], color='green',label='wang N')
plt.legend()

plt.subplot(1,4,3)
plt.hist(kmeans_std[2], color='blue')
plt.hist(std_group[2], color='green', label='wang 91bg')
plt.legend()

plt.subplot(1,4,4)
plt.hist(kmeans_std[3], color='blue', label='kmeans g4')
plt.hist(std_group[3], color='green', label='wang 91T')
plt.legend()

plt.show()
