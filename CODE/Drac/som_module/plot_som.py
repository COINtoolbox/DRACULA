from __future__ import print_function
import numpy as np
import pylab as plt
from scipy import stats

def func(spec_data,dict_som,out_name='som_res/som.pdf'):

	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument( '-nl'	, '--no_label'	, dest='do_label'	, default=True		, action='store_false'	, help='do not plot label' )
	parser.add_argument( '-w'	, '--window'	, dest='in_window'	, default=False		, action='store_true'	, help='keep plot in interactive window, this option will not save the output automaticaly' )
	parser.add_argument( '-hs'	, '--horiz_space', dest='hspace'	, default=0		, help='set horizontal spacing between the plots' )
	parser.add_argument( '-vs'	, '--vert_space', dest='vspace'		, default=0		, help='set vertical spacing between the plots' )
	for item in ['do_label','in_window','hspace','vspace']:
		exec(item+'=parser.parse_args().'+item)
	hspace	= float(hspace)
	vspace	= float(vspace)


	index = np.loadtxt('som_res/som_index.dat')
	nx = dict_som['nx']
	ny = dict_som['ny']

	som_ind = [[[] for j in xrange(ny)]for i in xrange(nx)]
	for ind,par in zip(range(len(index)),index):
		i,j=int(par[0]),int(par[1])
		som_ind[i][j].append(ind)
		
		
	fig,ax = plt.subplots(nx,ny)
	fig.subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=vspace,hspace=hspace)
		
	# make plots
	for i in xrange(nx):
		for j in xrange(ny):
			indices = som_ind[i][j]
			if len(indices) == 0:
				ax[i,j].set_xticks([])
				ax[i,j].set_yticks([])
			elif len(indices) == 1:
				#print indices
				f = spec_data[indices,:][0]
				n2 = f.shape[0]
		
				NORM = f[200:301].sum()
				f/=NORM
		
				ax[i,j].plot(f,'k-' )
				ax[i,j].set_xticks([])
				ax[i,j].set_yticks([])
			else:
		
				f = spec_data[indices]
				n1,n2 = f.shape

		
				for k in xrange(n1):
					NORM = f[k,200:301].sum()
					for kk in xrange(n2):
						f[k,kk]/=NORM
	

				ff=np.median(f,axis=0)

				CL68 = np.array( [ [ stats.scoreatpercentile(f[:,k],16), stats.scoreatpercentile(f[:,k],16+68)] for k in xrange(n2)] )
				CL95 = np.array( [ [ stats.scoreatpercentile(f[:,k],2.5), stats.scoreatpercentile(f[:,k],97.5)] for k in xrange(n2) ] )


				ax[i,j].plot(range(n2),ff,'k-' )
	
				ax[i,j].fill_between( range(n2) ,CL68[:,0], CL68[:,1],interpolate=True,facecolor = "red",alpha = 0.4)
				ax[i,j].fill_between( range(n2) , CL95[:,0], CL95[:,1],interpolate= True,facecolor = "blue",alpha = 0.3)
		

				ax[i,j].set_xticks([])
				ax[i,j].set_yticks([])
	
	if in_window	: plt.show()			
	else		: fig.savefig(out_name,dpi = 4000)
