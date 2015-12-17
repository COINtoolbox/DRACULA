from __future__ import print_function

import numpy as np
from config import REDUCTION_METHOD, CLUSTERING_METHOD 

import argparse
parser = argparse.ArgumentParser()
parser.add_argument( '-w'	, '--window'	, dest='in_window'	, default=False		, action='store_true'	, help='keep plot in interactive window, this option will not save the output automaticaly' )
#for item in ['use_diag','fit_all','do_colors','do_label','in_window','plot_pars','hspace','vspace']:
for item in ['in_window']:
	exec(item+'=parser.parse_args().'+item)


import matplotlib
if in_window==False: matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def plot_quality(QUALITY_METHODS,out_name='plots/quality.pdf'):
	do_pdf=False
	if out_name[len(out_name)-3:]=='pdf': do_pdf=True
	if do_pdf: pdf	= PdfPages(out_name)

	data		= np.loadtxt('quality_comparison.dat').T
	colors_base	= ['r', 'g', 'b', 'y','c', 'm','k','.8']
	for n in range(8): colors_base+=colors_base
	xl,yl	= .8,.9

	col_ind	= [ int(n) for n in set(data[0])]

	for Q,ind in zip(QUALITY_METHODS,range(1,1+len(QUALITY_METHODS))):
		print(ind,Q)

		nan_mask= (data[ind]==data[ind])
		xdat	= data[0][nan_mask]
		ydat	= data[ind][nan_mask]

		xvec	= range(len(xdat))
		xint	= [int(x) for x in xvec]
		ncls	= set(xdat)
		ncll	= [int(n) for n in ncls]
		colors	= [colors_base[col_ind.index(dat)] for dat in xdat]
		colors_used = [c for c in colors_base if c in colors]

		
		hspace	= '10 clusters'
		for n in range(1,len(ncls)): hspace+='\n10 clusters'

		plt.clf()
		plt.figure(figsize=(16,12))
		plt.ylabel(Q)
		plt.xticks(xint,['case '+str(i+1) for i in xint])
		plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.15)

		##################### plot the data  ########################		
		plt.plot(xvec,ydat,color='.0',lw=3)
		if len(ncls)>1:
			for i in xint:
				y=ydat
				if i==xint[0]	  : xv,yv=[i,i+.5],[ y[i] , y[i]+.5*(y[i+1]-y[i]) ]
				elif i==xint[-1]  : xv,yv=[i-.5,i],[ y[i]-.5*(y[i]-y[i-1]) , y[i] ]
				else		  : xv,yv=[i-.5,i,i+.5],[ y[i]-.5*(y[i]-y[i-1]),y[i] , y[i]+.5*(y[i+1]-y[i]) ]
				plt.fill_between(xv,0,yv,color=colors[i])
			##################### make the label ########################		
			fig	= plt.gcf()
			t	= plt.axes().transAxes
			text	= plt.text(xl,yl,hspace,color='1.',bbox={'facecolor':'1.', 'alpha':1., 'pad':20},transform=plt.axes().transAxes)
			text.draw(fig.canvas.get_renderer())
			ex	= text.get_window_extent()
			t	= matplotlib.transforms.offset_copy(text._transform, y=ex.height/(1.+1./(len(ncls)-1.)), units='dots')
			for s,c in zip([str(int(n))+' clusters' for n in ncls],colors_used):
				if s[:2]=='1 ': s=s[:len(s)-1]
				text = plt.text(xl,yl," "+s+" ",color=c, transform=t)
			        text.draw(fig.canvas.get_renderer())
			        ex = text.get_window_extent()
			        t = matplotlib.transforms.offset_copy(text._transform, y=-ex.height, units='dots')

		##################### put plot in file/window  ########################		
		if in_window	: plt.show(block=True)
		else		: 
			if do_pdf: pdf.savefig()
			else	 : plt.savefig(out_name[:len(out_name)-4]+'_'+Q+out_name[len(out_name)-4:])

	if do_pdf: pdf.close()
