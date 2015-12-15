from __future__ import print_function


import numpy as np
from config import REDUCTION_METHOD, CLUSTERING_METHOD 

import argparse
parser = argparse.ArgumentParser()
parser.add_argument( '-nd'	, '--no_diag'	, dest='use_diag'	, default=True		, action='store_false'	, help='do not plot diagonal' )
parser.add_argument( '-nf'	, '--no_fit'	, dest='fit_all'	, default=True		, action='store_false'	, help='do not fit in all dimensions simultanniously' )
parser.add_argument( '-nc'	, '--no_colors'	, dest='do_colors'	, default=True		, action='store_false'	, help='do not use colors' )
parser.add_argument( '-nl'	, '--no_label'	, dest='do_label'	, default=True		, action='store_false'	, help='do not plot label' )
parser.add_argument( '-w'	, '--window'	, dest='in_window'	, default=False		, action='store_true'	, help='keep plot in interactive window, this option will not save the output automaticaly' )
parser.add_argument( '-pp'	, '--plot_pars'	, dest='plot_pars'	, default='ALL'		, help='plot specified pars, takes a string as input (ex: "1 2")' )
parser.add_argument( '-hs'	, '--horiz_space', dest='hspace'	, default=0		, help='set horizontal spacing between the plots' )
parser.add_argument( '-vs'	, '--vert_space', dest='vspace'		, default=0		, help='set vertical spacing between the plots' )
for item in ['use_diag','fit_all','do_colors','do_label','in_window','plot_pars','hspace','vspace']:
	exec(item+'=parser.parse_args().'+item)
if plot_pars!='ALL': plot_pars= [int(v) for v in plot_pars.split()]
hspace	= float(hspace)
vspace	= float(vspace)


import matplotlib
if in_window==False: matplotlib.use('Agg')
import matplotlib.pyplot as plt

color_base	= ['r', 'g', 'b', 'y','c', 'm','k','.8']
for n in range(5): color_base+=color_base

def ind(i):
	if use_diag: return i
	else:	return i+1
def TAM(vec):
	if use_diag	: return len(vec)
	else		: return len(vec)-1
def crop(data,i,j,plt_inds):
	iplt,jplt=plt_inds[ind(i)],plt_inds[j]
	return np.array([data[jplt],data[iplt]])
def add_labels(plts,Nplt,ls,lc):
	PLT,xl,yl = plts, .67, .8
	if Nplt>1:	PLT,xl,yl = plts[0][Nplt-1], .1,.4
	G_space='\n-----------------------------\n'
	for g in ls: G_space+='\n'
	Ng=len(ls)

	dy	= 1.5
	fig	= plt.gcf()
	t	= PLT.transAxes
	text	= PLT.text(xl,yl,'REDUCTION_METHOD:  '+REDUCTION_METHOD+'\nCLUSTERING_METHOD:  '+CLUSTERING_METHOD+G_space, fontsize=18,bbox={'facecolor':'1.', 'alpha':0.5, 'pad':20},transform=PLT.transAxes)
	text.draw(fig.canvas.get_renderer())
	ex = text.get_window_extent()
	t	= matplotlib.transforms.offset_copy(text._transform, y=ex.height*(3/(Ng+3.)), units='dots')
	for s,c in zip(ls,lc):
		text = PLT.text(xl,yl," "+s+" ",color=c, transform=t, fontsize=22)
	        text.draw(fig.canvas.get_renderer())
	        ex = text.get_window_extent()
	        t = matplotlib.transforms.offset_copy(text._transform, y=-ex.height*dy, units='dots')
def plot_data(red_data,cl_data,label_data,out_name='plots/plot.png'):
	colors	= 'r'
	if do_colors and fit_all: colors = [color_base[int(i)] for i in label_data.astype(np.float)]
	group_text=['Group '+str(int(i)+1) for i in set(label_data)]

	Nplt=TAM(red_data)
	if Nplt!=TAM(cl_data): print('**ERROR** - # of rows in reducted file is different from # of rows in cluster centers file!\n\n\t-- please rerun either REDUCTION of CLUSTERING --\n'); exit()
	plt_inds=range(Nplt+1)

	if plot_pars!='ALL':
		for v in plot_pars:
			if v>Nplt: print('**ERROR** - there is no PC_'+str(v));exit()
		plt_inds=[v-1 for v in plot_pars]
		Nplt=TAM(plot_pars)

	f,plts  = plt.subplots(Nplt,Nplt,sharex=True,sharey=True,figsize=(20,14))
	for i in range(Nplt):
		for j in range(Nplt):
			PLT,ax=plt,plt.gca()
			if Nplt>1:
				PLT,ax= plts[i][j],plts[i][j]
				plt.setp( ax.get_xticklabels()[ 0], visible=False)
				plt.setp( ax.get_xticklabels()[-1], visible=False)
				plt.setp( ax.yaxis.get_major_ticks()[ 0], visible=False)
				if i>0: plt.setp( ax.yaxis.get_major_ticks()[ -1], visible=False)
			print(Nplt,i,j)
			plt.setp( ax.get_xticklabels(), rotation=45, fontsize=18)
			plt.setp( ax.get_yticklabels(), rotation=45, fontsize=18)
#			PLT.locator_params('x',nbins=4)
#			PLT.locator_params('y',nbins=4)
			dat	= crop(red_data,i,j,plt_inds)
			cl_dat	= crop(cl_data,i,j,plt_inds)
			if j>i: PLT.axis('off')
			else:
				PLT.scatter(dat[0],dat[1],c=colors,edgecolor=colors,marker='o',label='data',lw=0,s=40)
				if fit_all:
					PLT.scatter(cl_dat[0],cl_dat[1],c='.0',linewidth='2',marker='x',label='cluster centers')
					PLT.scatter(cl_dat[0],cl_dat[1],c='.5',linewidth='.7',marker='x',s=10)
	if do_label:	add_labels(plts,Nplt,group_text,color_base[:len(group_text)])
	for i in range(Nplt):	
		PLTX,PLTY=plts,plts
		if Nplt>1: 
			PLTX,PLTY=plts[ Nplt-1 ][ i ],plts[ i      ][ 0 ]
			if REDUCTION_METHOD == 'DeepLearning':         
				PLTX.set_xlabel('feature '+ str(plt_inds[i]+1), fontsize=26)
				PLTY.set_ylabel('feature '+ str(plt_inds[ind(i)]+1), fontsize=26)				
			else:
				PLTX.set_xlabel('PC'+ str(plt_inds[i]+1), fontsize=26)
				PLTY.set_ylabel('PC'+ str(plt_inds[ind(i)]+1), fontsize=26)

	plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.15,hspace=hspace,wspace=vspace)
	if in_window	: plt.show(block=True)
	else		: plt.savefig(out_name)
