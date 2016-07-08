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
path_kmeans_3g = '../../data/clustering_KMeans_label_4features_3groups.dat'
path_kmeans_2g = '../../data/clustering_KMeans_label_4features_2groups.dat'

# read kmeans result 4 groups
op5 = open(path_kmeans_4g, 'r')
lin5 = op5.readlines()
op5.close()

kmeans_classes = [float(elem.split()[0]) for elem in lin5]

# read result 3 groups
kmeans_classes_3g = np.loadtxt(path_kmeans_3g)

# read result 2 groups
kmeans_classes_2g = np.loadtxt(path_kmeans_2g)


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

data_max = np.array([data_spectra[i] for i in xrange(len(data_spectra)) if names_all[i][-1] == '1'])
spectra_mean = np.array([np.mean(data_max[:,j]) for j in xrange(len(data_max[0]))])
spectra_std = np.array([np.std(data_max[:,j]) for j in xrange(len(data_max[0]))])


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
for j in xrange(len(wang_spectra)):
    spectra_group.append([np.mean(wang_spectra[j][:,l]) for l in xrange(len(wang_spectra[j][0]))])

spectra_group = np.array(spectra_group)


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



# separate groups according to kmeans classification 3 groups
groups_kmeans_3g = []
for item in xrange(3):
    kmeans_temp = []
    cont = 0
    for j in xrange(len(data_spectra)):
        if names_all[j][-1] == '1':
            cont = cont + 1
            if kmeans_classes_3g[cont - 1] == item:
                kmeans_temp.append(data_spectra[j])

    groups_kmeans_3g.append(np.array(kmeans_temp))

group_kmeans_3g = np.array(groups_kmeans_3g)
kmeans_rep_3g = [np.array([np.mean(group_kmeans_3g[ll][:,jj]) for jj in xrange(len(data_spectra[0]))]) for ll in xrange(len(groups_kmeans_3g))]
kmeans_std_3g = [np.array([np.std(group_kmeans_3g[ll][:,jj]) for jj in xrange(len(data_spectra[0]))]) for ll in xrange(len(groups_kmeans_3g))]

# separate groups according to kmeans classification 2 groups
groups_kmeans_2g = []
for item in xrange(2):
    kmeans_temp = []
    cont = 0
    for j in xrange(len(data_spectra)):
        if names_all[j][-1] == '1':
            cont = cont + 1
            if kmeans_classes_2g[cont - 1] == item:
                kmeans_temp.append(data_spectra[j])

    groups_kmeans_2g.append(np.array(kmeans_temp))

group_kmeans_2g = np.array(groups_kmeans_2g)
kmeans_rep_2g = [np.array([np.mean(group_kmeans_2g[ll][:,jj]) for jj in xrange(len(data_spectra[0]))]) for ll in xrange(len(groups_kmeans_2g))]
kmeans_std_2g = [np.array([np.std(group_kmeans_2g[ll][:,jj]) for jj in xrange(len(data_spectra[0]))]) for ll in xrange(len(groups_kmeans_2g))]


# plot wang and kmeans results
fig2 = plt.figure(figsize=(20, 14))

chi2_HV_1g = round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('HV')][j]-spectra_mean[j])**2 for j in xrange(len(spectra_mean))])),2)
chi2_N_1g = round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('N')][j]-spectra_mean[j])**2 for j in xrange(len(spectra_mean))])),2)
chi2_91bg_1g = round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('91bg')][j]-spectra_mean[j])**2 for j in xrange(len(spectra_mean))])),2)
chi2_91T_1g = round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('91T')][j]-spectra_mean[j])**2 for j in xrange(len(spectra_mean))])),2)

ax2 = plt.subplot(2,2,1)
line,  = ax2.plot(xaxes, spectra_group[color_wang[2]['name'].index('HV')]+1.3, lw=2.0,ls='--', color='green', label='HV - Wang')
line,  = ax2.plot(xaxes, spectra_group[color_wang[2]['name'].index('N')]+1.3, lw=2.0,ls='--', color='red', label='N - Wang')
line,  = ax2.plot(xaxes, spectra_group[color_wang[2]['name'].index('91bg')]+1.3, lw=2.0,ls='--', color='blue', label='91bg - Wang')
line,  = ax2.plot(xaxes, spectra_group[color_wang[2]['name'].index('91T')]+1.3, lw=2.0,ls='--', color='orange', label='91T - Wang')
line, = ax2.plot(xaxes, spectra_mean + 1.3, color='red',lw=2.0, label='mean spectra')
ax2.fill_between(xaxes, spectra_mean - spectra_std[0] + 1.3, spectra_mean + spectra_std[0] + 1.3, facecolor='gray', alpha=0.3, label='DL+KM 1$\sigma$')
ax2.text(6660, 2.5, '$\chi^2 = $' + str(chi2_HV_1g), fontsize=14, color='green')
ax2.text(6660, 2.3, '$\chi^2 = $' + str(chi2_N_1g), fontsize=14, color='red')
ax2.text(6660, 2.1, '$\chi^2 = $' + str(chi2_91bg_1g), fontsize=14, color='blue')
ax2.text(6660, 1.9, '$\chi^2 = $' + str(chi2_91T_1g), fontsize=14, color='orange')
plt.ylabel('flux (arbitrary units)', fontsize=16)
plt.xticks([])
plt.yticks(fontsize=14)
plt.ylim(0, 3.75)
ax2.legend(loc='upper center', bbox_to_anchor=(0.89, 1.0155), ncol=1, fontsize=14)

chi2_HV_2g = [round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('HV')][j]-kmeans_rep_2g[k][j])**2 for j in xrange(len(kmeans_rep_2g[0]))])),2) for k in xrange(2)]
chi2_N_2g = [round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('N')][j]-kmeans_rep_2g[k][j])**2 for j in xrange(len(kmeans_rep_2g[0]))])),2) for k in xrange(2)]
chi2_91bg_2g = [round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('91bg')][j]-kmeans_rep_2g[k][j])**2 for j in xrange(len(kmeans_rep_2g[0]))])),2) for k in xrange(2)]
chi2_91T_2g = [round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('91T')][j]-kmeans_rep_2g[k][j])**2 for j in xrange(len(kmeans_rep_2g[0]))])),2) for k in xrange(2)]


ax3 = plt.subplot(2,2,2)
line, = ax3.plot(xaxes, spectra_group[color_wang[2]['name'].index('HV')]+2.1, lw=2.0, ls='--', color='green', label='HV - Wang')
line,  = ax3.plot(xaxes, spectra_group[color_wang[2]['name'].index('N')]+0.5, lw=2.0,ls='--', color='red', label='N - Wang')
line,  = ax3.plot(xaxes, spectra_group[color_wang[2]['name'].index('91bg')]+2.1, lw=2.0,ls='--', color='blue', label='91bg - Wang')
line,  = ax3.plot(xaxes, spectra_group[color_wang[2]['name'].index('91T')]+0.5, lw=2.0,ls='--', color='orange', label='91T - Wang')
line, = ax3.plot(xaxes, kmeans_rep_2g[0]+2.1, color='green',lw=2.0, label='DL+KM G1')
line, = ax3.plot(xaxes, kmeans_rep_2g[1]+0.5, lw=2.0, color='red', label='DL+KM G2')
ax3.fill_between(xaxes, kmeans_rep_2g[0] - kmeans_std_2g[0] + 2.1, kmeans_rep_2g[0] + kmeans_std_2g[0] + 2.1, facecolor='gray', alpha=0.3, label='DL+KM 1$\sigma$')
ax3.fill_between(xaxes, kmeans_rep_2g[1] - kmeans_std_2g[1]+0.5, kmeans_rep_2g[1] + kmeans_std_2g[1]+0.5, facecolor='gray', alpha=0.3)
ax3.text(6660, 2.9, '$\chi^2 = $' + str(chi2_HV_2g[0]), fontsize=14, color='green')
ax3.text(6660, 1.4, '$\chi^2 = $' + str(chi2_N_2g[1]), fontsize=14, color='red')
ax3.text(6660, 2.7, '$\chi^2 = $' + str(chi2_91bg_2g[0]), fontsize=14, color='blue')
ax3.text(6660, 1.2, '$\chi^2 = $' + str(chi2_91T_2g[1]), fontsize=14, color='orange')
plt.xticks([])
plt.yticks([])
plt.ylim(0, 3.75)
ax3.legend(loc='upper center', bbox_to_anchor=(0.788, 1.014), ncol=2, fontsize=14)

chi2_HV_3g = [round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('HV')][j]-kmeans_rep_3g[k][j])**2 for j in xrange(len(kmeans_rep_3g[0]))])),2) for k in xrange(3)]
chi2_N_3g = [round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('N')][j]-kmeans_rep_3g[k][j])**2 for j in xrange(len(kmeans_rep_3g[0]))])),2) for k in xrange(3)]
chi2_91T_3g = [round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('91T')][j]-kmeans_rep_3g[k][j])**2 for j in xrange(len(kmeans_rep_3g[0]))])),2) for k in xrange(3)]
chi2_91bg_3g = [round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('91bg')][j]-kmeans_rep_3g[k][j])**2 for j in xrange(len(kmeans_rep_3g[0]))])),2) for k in xrange(3)]

ax2 = plt.subplot(2,2,3)
line, = ax2.plot(xaxes, spectra_group[color_wang[2]['name'].index('HV')] + 2.2, lw=2.0, ls='--', color='green', label='HV - Wang')
line,  = ax2.plot(xaxes, spectra_group[color_wang[2]['name'].index('N')] + 1.1, lw=2.0,ls='--', color='red', label='N - Wang')
line, = ax2.plot(xaxes, spectra_group[color_wang[2]['name'].index('91bg')] + 0.1, lw=2.0, ls='--', color='blue', label='91bg - Wang')
line, = ax2.plot(xaxes, spectra_group[color_wang[2]['name'].index('91T')]+1.1, lw=2.0, ls='--', color='orange', label='91T - Wang')
line, = ax2.plot(xaxes, kmeans_rep_3g[0]+2.2, color='green',lw=2.0, label='DL+KM G1')
line, = ax2.plot(xaxes, kmeans_rep_3g[1]+1.1, lw=2.0, color='red', label='DL+KM G2')
line, = ax2.plot(xaxes, kmeans_rep_3g[2]+0.1, lw=2.0, color='blue', label='DL+KM G3')
ax2.fill_between(xaxes, kmeans_rep_3g[0] - kmeans_std_3g[0] + 2.2, kmeans_rep_3g[0] + kmeans_std_3g[0] + 2.2, facecolor='gray', alpha=0.3, label='DL+KM 1$\sigma$')
ax2.fill_between(xaxes, kmeans_rep_3g[1] - kmeans_std_3g[1] + 1.1, kmeans_rep_3g[1] + kmeans_std_3g[1] + 1.1, facecolor='gray', alpha=0.3)
ax2.fill_between(xaxes, kmeans_rep_3g[2] - kmeans_std_3g[2] + 0.1, kmeans_rep_3g[2] + kmeans_std_3g[2] + 0.1, facecolor='gray', alpha=0.3)
ax2.text(6660, 2.8, '$\chi^2 = $' + str(chi2_HV_3g[0]), fontsize=14, color='green')
ax2.text(6660, 1.8, '$\chi^2 = $' + str(chi2_N_3g[1]), fontsize=14, color='red')
ax2.text(6660, 1.65, '$\chi^2 = $' + str(chi2_91T_3g[1]), fontsize=14, color='orange')
ax2.text(6660, 0.8, '$\chi^2 = $' + str(chi2_91bg_3g[2]), fontsize=14, color='blue')
plt.ylabel('flux (arbitrary units)', fontsize=16)
plt.xlabel('wavelength ($\AA$)', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(0, 3.75)
ax2.yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
ax2.xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
ax2.legend(loc='upper center', bbox_to_anchor=(0.788, 1.014), ncol=2, fontsize=14)


chi2_HV = [round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('HV')][j]-kmeans_rep[k][j])**2 for j in xrange(len(kmeans_rep[0]))])),2) for k in xrange(4)]
chi2_N = [round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('N')][j]-kmeans_rep[k][j])**2 for j in xrange(len(kmeans_rep[1]))])),2)  for k in xrange(4)]
chi2_91bg = [round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('91bg')][j]-kmeans_rep[k][j])**2 for j in xrange(len(kmeans_rep[2]))])),2)  for k in xrange(4)]
chi2_91T = [round(np.sqrt(sum([(spectra_group[color_wang[2]['name'].index('91T')][j]-kmeans_rep[k][j])**2 for j in xrange(len(kmeans_rep[3]))])),2)  for k in xrange(4)]

ax = plt.subplot(2,2,4)
line, = ax.plot(xaxes, spectra_group[color_wang[2]['name'].index('HV')]+2.2, lw=2.0, ls='--', color='green', label='HV - Wang')
line,  = ax.plot(xaxes, spectra_group[color_wang[2]['name'].index('N')]+1.5, lw=2.0,ls='--', color='red', label='N - Wang')
line, = ax.plot(xaxes, spectra_group[color_wang[2]['name'].index('91bg')]+0.8, lw=2.0, ls='--', color='blue', label='91bg - Wang')
line, = ax.plot(xaxes, spectra_group[color_wang[2]['name'].index('91T')], lw=2.0, ls='--', color='orange', label='91T - Wang')
line, = ax.plot(xaxes, kmeans_rep[0]+2.2, color='green',lw=2.0, label='DL+KM G1')
line, = ax.plot(xaxes, kmeans_rep[1]+1.5, lw=2.0, color='red', label='DL+KM G2')
line, = ax.plot(xaxes, kmeans_rep[2]+0.8, lw=2.0, color='blue', label='DL+KM G3')
line, = ax.plot(xaxes, kmeans_rep[3], lw=2.0, color='orange', label='DL+KM G4')
ax.fill_between(xaxes, kmeans_rep[0] - kmeans_std[0] + 2.2, kmeans_rep[0] + kmeans_std[0] + 2.2, facecolor='gray', alpha=0.3, label='DL+KM 1$\sigma$')
ax.fill_between(xaxes, kmeans_rep[1] - kmeans_std[1] + 1.5, kmeans_rep[1] + kmeans_std[1] + 1.5, facecolor='gray', alpha=0.3)
ax.fill_between(xaxes, kmeans_rep[2] - kmeans_std[2] + 0.8, kmeans_rep[2] + kmeans_std[2] + 0.8, facecolor='gray', alpha=0.3)
ax.fill_between(xaxes, kmeans_rep[3] - kmeans_std[3], kmeans_rep[3] + kmeans_std[3], facecolor='gray', alpha=0.3)
ax.text(6660, 2.8, '$\chi^2 = $' + str(chi2_HV[0]), fontsize=14, color='green')
ax.text(6660, 2.8-0.7, '$\chi^2 = $' + str(chi2_N[1]), fontsize=14, color='red')
ax.text(6660, 2.8-1.4, '$\chi^2 = $' + str(chi2_91bg[2]), fontsize=14, color='blue')
ax.text(6660, 2.8-2.2, '$\chi^2 = $' + str(chi2_91T[3]), fontsize=14, color='orange')
plt.xlabel('wavelength ($\AA$)', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks([])
plt.ylim(0, 3.75)
ax.legend(loc='upper center', bbox_to_anchor=(0.6765, 1.015), ncol=3, fontsize=14)

plt.subplots_adjust(left=0.05, right=0.975, top=0.99, bottom=0.075,hspace=0.0,wspace=0.0)
plt.savefig("wang_DL_kmeans_spectra_C2.pdf", format='pdf',dpi=1000)


