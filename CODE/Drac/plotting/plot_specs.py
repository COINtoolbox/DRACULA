from __future__ import print_function


import numpy as np
from config import REDUCTION_METHOD, CLUSTERING_METHOD 

import argparse
parser = argparse.ArgumentParser()
parser.add_argument( '-w'	, '--window'	, dest='in_window'	, default=False		, action='store_true'	, help='keep plot in interactive window, this option will not save the output automaticaly' )
parser.add_argument( '-a'	, '--all_spec'	, dest='all_spec'	, default=False		, action='store_true'	, help='plot all spectra')
#for item in ['use_diag','fit_all','do_colors','do_label','in_window','plot_pars','hspace','vspace']:
for item in ['in_window','all_spec']:
	exec(item+'=parser.parse_args().'+item)


import matplotlib
if in_window==False: matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def plot_spectra(spec_data,label_data,out_name='plots/specs.pdf'):
	if len(spec_data)!=len(label_data): print("**ERROR** : len(spec_data) =/= len(labels) \n\t probably the data for the plotting is masked but the data input for clustering is not\n");exit()
	do_pdf=False
	if out_name[len(out_name)-3:]=='pdf': do_pdf=True

	if do_pdf: pdf	= PdfPages(out_name)
	ymin,ymax	= np.amin(spec_data) , np.amax(spec_data)
	xvec		= [4000 + 10*xx for xx in range(len(spec_data[0]))]
	data_split	= [spec_data[label_data==n] for n in set(label_data)] 

	colors		= ['r', 'g', 'b', 'y','c', 'm','k','.8']
	for n in range(len(set(label_data))/8): colors+=colors

	plt.figure(figsize=(16,12))
	plt.xlabel('wavelength', fontsize=26)
	plt.ylabel('flux (arbitrart units)', fontsize=26)
	plt.xticks(size=20)
	plt.yticks(size=20)
	plt.xlim(min(xvec),max(xvec))
	plt.ylim(ymin,ymax)
	ind=0
	for data in data_split:
		ind+=1
		mdata=np.mean(data,axis=0)
		plt.plot(xvec,mdata,color=colors[ind-1],lw=3,label='Group '+str(ind))
	plt.legend(fontsize=20)
	plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.15)
	if in_window	: plt.show(block=True)
	else		: 
		if do_pdf: pdf.savefig()
		else	 : plt.savefig(out_name)

	if all_spec:
		ind=0
		for data in data_split:
			ind+=1
			plt.clf()
			plt.figure(figsize=(16,12))
			plt.title('Group '+str(ind))
			plt.xlim(min(xvec),max(xvec))
			plt.ylim(ymin,ymax)
			for dat in data: plt.plot(xvec,dat,color=colors[ind-1],lw=.5)
			mdata=np.mean(data,axis=0)
			plt.plot(xvec,mdata,color='.0',lw=3)
			plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.15)
			if in_window	: plt.show(block=True)
			else		: 
				if do_pdf: pdf.savefig()
				else	 : plt.savefig(out_name[:len(out_name)-4]+'_group_'+str(ind)+out_name[len(out_name)-4:])

	if do_pdf: pdf.close()
