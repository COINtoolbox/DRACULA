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

# read spectra ID
op2 = open(path_id, 'r')
lin2 = op2.readlines()
op2.close()

names_all = [elem.split() for elem in lin2[1:]]
names_max = [names_all[i][0] for i in xrange(len(names_all)) if names_all[i][-1] == '1']


# build wang color code 
color_wang = load_colors(names_max)

# separate groups accorging to wang classification
wang_code = []
for cor in color_wang[2]['color'][:-1]:
    temp_code = np.array(color_wang[0]) == cor
    wang_code.append(temp_code)

# read DL results
op1 = open(path_small_space, 'r')
lin1 = op1.readlines()
op1.close()

data1 = [elem.split() for elem in lin1]

matrix = np.array([[float(item) for item in data1[i]] for i in xrange(len(data1)) if names_all[i][-1]=='1'])

my_colors = ['green', 'red', 'blue', 'orange']
my_marks = ['^','o',  's', 'd', '*']

# marker size
ss = [60, 40, 40, 60]

# plot only DL results
fig = plt.figure(figsize=(20,14))
plt.subplot(4,4,1)
legs = [[] for k in xrange(len(wang_code))]
names = []
for j in [1,0,2,3]:
    legs[j] = plt.scatter(matrix[wang_code[j],0], matrix[wang_code[j],0], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
    names.append(color_wang[2]['name'][j])
plt.ylabel('feature 1', fontsize=26)
plt.xticks([])
plt.yticks(fontsize=22)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,5)
for j in [1,0,2,3]:
    plt.scatter(matrix[wang_code[j],0], matrix[wang_code[j],1], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.ylabel('feature 2', fontsize=26)
plt.xticks([])
plt.yticks(fontsize=22)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,6)
for j in [1,0,2,3]:
    plt.scatter(matrix[wang_code[j],1], matrix[wang_code[j],1], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.xticks([])
plt.yticks([])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,9)
for j in [1,0,2,3]:
    plt.scatter(matrix[wang_code[j],0], matrix[wang_code[j],2], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.ylabel('feature 3', fontsize=26)
plt.xticks([])
plt.yticks(fontsize=22)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,10)
for j in [1,0,2,3]:
    plt.scatter(matrix[wang_code[j],1], matrix[wang_code[j],2], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.xticks([])
plt.yticks([])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,11)
for j in [1,0,2,3]:
    plt.scatter(matrix[wang_code[j],2], matrix[wang_code[j],2], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.xticks([])
plt.yticks([])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,13)
for j in [1,0,2,3]:
    plt.scatter(matrix[wang_code[j],0], matrix[wang_code[j],3], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.ylabel('feature 4', fontsize=26)
plt.xlabel('feature 1', fontsize=26)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,14)
for j in [1,0,2,3]:
    plt.scatter(matrix[wang_code[j],1], matrix[wang_code[j],3], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.xlabel('feature 2', fontsize=26)
plt.yticks([])
plt.xticks(fontsize=22)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,15)
for j in [1,0,2,3]:
    plt.scatter(matrix[wang_code[j],2], matrix[wang_code[j],3], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.xlabel('feature 3',fontsize=26)
plt.yticks([])
plt.xticks(fontsize=22)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,16)
for j in [1,0,2,3]:
    plt.scatter(matrix[wang_code[j],3], matrix[wang_code[j],3], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.xlabel('feature 4', fontsize=26)
plt.yticks([])
plt.xticks(fontsize=22)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)



plt.subplots_adjust(left=0.075, right=0.975, top=0.975, bottom=0.075,hspace=0.0,wspace=0.0)
legend = fig.legend(legs, names, loc = (0.786, 0.778), title='Wang classification', fontsize=26)
plt.setp(legend.get_title(),fontsize=26)
plt.savefig("wang_DL_scatter.pdf", format='pdf',dpi=1000)


