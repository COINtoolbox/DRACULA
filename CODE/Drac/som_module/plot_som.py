from __future__ import print_function
import numpy as np
import pylab as plt
from scipy import stats

def func(spec_data,dict_som,out_name='som_res/som.pdf'):
	index = np.loadtxt('som_res/som_index.dat')
	nx = dict_som['nx']
	ny = dict_som['ny']

	som_ind = [[[] for j in xrange(ny)]for i in xrange(nx)]
	for ind,par in zip(range(len(index)),index):
		i,j=int(par[0]),int(par[1])
		som_ind[i][j].append(ind)
		
		
	fig,ax = plt.subplots(nx,ny)
	fig.subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=0.0,hspace=0.0)
		
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


				print(range(n2),ff,'k-' )
				ax[i,j].plot(range(n2),ff,'k-' )
	
				ax[i,j].fill_between( range(n2) ,CL68[:,0], CL68[:,1],interpolate=True,facecolor = "red",alpha = 0.4)
				ax[i,j].fill_between( range(n2) , CL95[:,0], CL95[:,1],interpolate= True,facecolor = "blue",alpha = 0.3)
		

				ax[i,j].set_xticks([])
				ax[i,j].set_yticks([])
	
				
	fig.savefig(out_name,format = "pdf",dpi = 4000)
	
	pass
