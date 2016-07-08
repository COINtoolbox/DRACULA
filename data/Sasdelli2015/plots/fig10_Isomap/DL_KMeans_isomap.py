import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from sklearn import manifold
import matplotlib.gridspec as gridspec

def load_colors(sne_list,type='Wang'):

    import urllib
    import numpy
    
    #path1 = 'https://iopscience.iop.org/1538-3881/143/5/126/suppdata/aj427309t4_mrt.txt'
    #op1 = urllib.urlopen(path1, 'r')
    op1=open('aj427309t4_mrt.txt','r')
    lin1 = op1.readlines()
    op1.close()
    #data1 = [elem[17:].split() for elem in lin1[51:]]
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

# path to kmeans result
path_kmeans = '../../data/clustering_KMeans_label_4features_4groups.dat'

# path to spectra
path_spectra = '../../data/fluxes_atmax.dat'

# color for plotting
c = [ 'blue', 'red', 'green', 'orange', 'black']

# markers for ploting
mark =  ['^','o',  's', 'd', '*']

# markers size
size = [75, 65, 65, 70, 75]

# read spectra ID
op2 = open(path_id, 'r')
lin2 = op2.readlines()
op2.close()

names_all = [elem.split() for elem in lin2[1:]]
names_max = [names_all[i][0] for i in xrange(len(names_all)) if names_all[i][-1] == '1']


# separate interesting spectra
indx_list0 = [i for i in range(len(names_max)) if names_max[i] == 'sn1998aq']
indx_list = [12, 112,81,20]
# sn2007hj
# sn2007on   near 2006bt
# sn2004dt
# sn1998aq
# sn1999ac  very good

# read fluxes
op2x = open(path_spectra, 'r')
lin2x = op2x.readlines()
op2x.close()

data2x = [elem.split() for elem in lin2x]
flux1999ac = [float(data2x[indx_list[0]][i]) for i in range(len(data2x[0]))]
xplot = [4000 + i*10 for i in range(len(data2x[0]))]
flux2006bt = [float(data2x[indx_list[1]][i]) for i in range(len(data2x[0]))]
flux2001ex = [float(data2x[indx_list[2]][i]) for i in range(len(data2x[0]))]
flux1998aq = [float(data2x[indx_list[3]][i]) for i in range(len(data2x[0]))]

# build wang color code 
color_wang = load_colors(names_max)

# separate groups accorging to wang classification
wang_code = []
for kk in [0,1,2,3,4]:
    temp_code = np.array(color_wang[0]) == color_wang[2]['color'][kk]
    wang_code.append(temp_code)


# read DL results
op1 = open(path_small_space, 'r')
lin1 = op1.readlines()
op1.close()

data1 = [elem.split() for elem in lin1]

matrix = np.array([[float(item) for item in data1[i]] for i in xrange(len(data1)) if names_all[i][-1]=='1'])


# do isomap reduction
n_neighbors = 10
n_components = 2
Y = manifold.Isomap(n_neighbors, n_components).fit_transform(matrix)

# get weird
data_weird = []
for line in indx_list:
    data_weird.append(Y[line])

data_w = np.array(data_weird)

# read kmeans results
op3 = open(path_kmeans, 'r')
lin3 = op3.readlines()
op3.close()

classes = np.array([float(elem.split()[0]) for elem in lin3])
group1 = classes == 0.0
group2 = classes == 1.0
group3 = classes == 2.0
group4 = classes == 3.0

# plot isomap reduction results
panels = [[] for i in xrange(4)]
gs = gridspec.GridSpec(3,3)
f = plt.figure(figsize=(22,14))
fig1 = plt.subplot2grid((2,3), (0,0), rowspan=2)
panels[0] = plt.scatter(Y[group1, 0], Y[group1, 1], color=c[0], marker=mark[0], s=75)
panels[1] = plt.scatter(Y[group2, 0], Y[group2, 1], color=c[1], marker=mark[1], s=65)
panels[2] = plt.scatter(Y[group3, 0], Y[group3, 1], color=c[2], marker=mark[2], s=65)
panels[3] = plt.scatter(Y[group4, 0], Y[group4, 1], color=c[3], marker=mark[3], s=70)
legs=fig1.legend(panels, ['Group 1', 'Group 2', 'Group 3', 'Group 4'], loc = (0.0, 0.835), title='Kmeans', fontsize=20)
plt.setp(legs.get_title(),fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.xlim(-2.0, 2.0)
plt.xlabel('isomap 1', fontsize=22)
plt.ylabel('isomap 2', fontsize=22)



panels2 = [[] for i in xrange(5)]
names = []
fig2 = plt.subplot2grid((2,3), (0,1), rowspan=2, colspan=2)
for j in xrange(5):
    panels2[j] = plt.scatter(Y[wang_code[j],0], Y[wang_code[j],1], marker=mark[j], color=c[j], s=size[j])
    if color_wang[2]['name'][j] != 'nan':
        names.append(color_wang[2]['name'][j])
    else:
        names.append('peculiar')
#plt.scatter(data_w[:,0],  data_w[:,1], marker='s', color='purple', s=200)
legs2=fig2.legend(panels2, names, loc = (0.0, 0.804), title='Wang', fontsize=20)

fig2.arrow(Y[indx_list[0]][0], Y[indx_list[0]][1], 1.2, -0.85, head_width=0.05, head_length=0.1, fc='k', ec='k')

fig2.plot([Y[indx_list[1]][0],1.5],[Y[indx_list[1]][1],0.8], color='black')
fig2.arrow(1.5, 0.8,0.7, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')

fig2.plot([Y[indx_list[2]][0],0.55],[Y[indx_list[2]][1],1.65], color='black')
fig2.arrow(0.55, 1.65, 1.6, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')

fig2.plot([Y[indx_list[3]][0],0.9],[Y[indx_list[3]][1],0.25], color='black')
fig2.arrow(0.9, 0.25, 1.2, -0.4, head_width=0.05, head_length=0.1, fc='k', ec='k')

plt.setp(legs2.get_title(),fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.tight_layout()
plt.xlim(-2.0, 6.0)
plt.xlabel('isomap 1', fontsize=22)
plt.ylabel('isomap 2', fontsize=22)

rect = [0.6,0.06,0.35,0.15]
axisbg='w'
box = fig2.get_position()
width = box.width
height = box.height
inax_position  = fig2.transAxes.transform(rect[0:2])
transFigure = f.transFigure.inverted()
infig_position = transFigure.transform(inax_position)    
x = infig_position[0]
y = infig_position[1]
width *= rect[2]
height *= rect[3]  # <= Typo was here
subax = f.add_axes([x,y,width,height],axisbg=axisbg)
x_labelsize = subax.get_xticklabels()[0].get_size()
y_labelsize = subax.get_yticklabels()[0].get_size()
subax.plot(xplot, flux1999ac)
subax.text(6250, 0.85, 'SN1999ac')
subax.set_xlabel('wavelength (angs)')
subax.set_ylabel('flux')

rect = [0.6,0.55,0.35,0.15]
axisbg='w'
box = fig2.get_position()
width = box.width
height = box.height
inax_position  = fig2.transAxes.transform(rect[0:2])
transFigure = f.transFigure.inverted()
infig_position = transFigure.transform(inax_position)    
x = infig_position[0]
y = infig_position[1]
width *= rect[2]
height *= rect[3]  # <= Typo was here
subax2 = f.add_axes([x,y,width,height],axisbg=axisbg)
x_labelsize = subax2.get_xticklabels()[0].get_size()
y_labelsize = subax2.get_yticklabels()[0].get_size()
subax2.plot(xplot, flux2006bt)
subax2.text(6250, 0.75, 'SN2006bt')
subax2.set_xlabel('wavelength (angs)')
subax2.set_ylabel('flux')

rect = [0.6,0.8,0.35,0.15]
axisbg='w'
box = fig2.get_position()
width = box.width
height = box.height
inax_position  = fig2.transAxes.transform(rect[0:2])
transFigure = f.transFigure.inverted()
infig_position = transFigure.transform(inax_position)    
x = infig_position[0]
y = infig_position[1]
width *= rect[2]
height *= rect[3]  # <= Typo was here
subax2 = f.add_axes([x,y,width,height],axisbg=axisbg)
x_labelsize = subax2.get_xticklabels()[0].get_size()
y_labelsize = subax2.get_yticklabels()[0].get_size()
subax2.plot(xplot, flux2001ex)
subax2.text(6250, 0.75, 'SN2001ex')
subax2.set_xlabel('wavelength (angs)')
subax2.set_ylabel('flux')

rect = [0.6,0.3,0.35,0.15]
axisbg='w'
box = fig2.get_position()
width = box.width
height = box.height
inax_position  = fig2.transAxes.transform(rect[0:2])
transFigure = f.transFigure.inverted()
infig_position = transFigure.transform(inax_position)    
x = infig_position[0]
y = infig_position[1]
width *= rect[2]
height *= rect[3]  # <= Typo was here
subax2 = f.add_axes([x,y,width,height],axisbg=axisbg)
x_labelsize = subax2.get_xticklabels()[0].get_size()
y_labelsize = subax2.get_yticklabels()[0].get_size()
subax2.plot(xplot, flux1998aq)
subax2.text(6250, 0.85, 'SN1998aq')
subax2.set_xlabel('wavelength (angs)')
subax2.set_ylabel('flux')




#plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.tight_layout()
plt.savefig("kmeans_wang_isomap_4g.pdf", format='pdf',dpi=1000)
plt.close()
