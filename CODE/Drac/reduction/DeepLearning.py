from rpy2.robjects import r
import numpy as np
import os,sys

def reduction(data, params):

	in_param	= ''
    # parse parameters

	for item in params:
	    if isinstance(params[item], str):
	        in_param += ', '+item+' = '+params[item]
	    else:
	        exec(item+'='+str(params[item]))

    # apply PCA

	
	size_data 	= np.shape(data)[1]
	in_param	= 'x=1:%d'%(size_data) + ''.join([ ', '+item+' = '+params[item] for item in params if isinstance(params[item], str)])

#	print('')
#	print(in_param[9:])
#	print(in_param)
#	print('\n')
	
	
	current_path	= os.path.abspath('')
	in_file_cvs	= current_path+'/.temp_file.cvs'
	np.savetxt(in_file_cvs, data, delimiter=',', fmt='%.18f')
	os.system('ls -lhtr')
	
#	print('******************* define libraries *********************')
	## define libraries
	r('library(h2o)')
	  
#	print('******************* Read data *********************')
	## Read data
	r('h2oServer <- h2o.init(nthreads=-1)')
	r('TRAIN = "%s" '% (in_file_cvs))
	r('train.hex <- h2o.importFile(path = TRAIN, header = F, parse = TRUE, col.names=NULL, col.types=NULL, sep = ",", destination_frame="train.hex")')
	
#	print('******************* Construct deep learning model *********************')
	## Construct deep learning model
#	print('dlmodel <- h2o.deeplearning( %s ) ' % (in_param))
	r('dlmodel <- h2o.deeplearning( %s ) ' % (in_param))
	
#	print('******************* Generate new features *********************')
	## Generate new features
	r('features_dl <- h2o.deepfeatures(dlmodel, train.hex, layer=%d)' % (n_layers))
	r('head(features_dl)')
	
#	print('******************* Store new features in file *********************')
	## Store new features in file
	X = r('as.matrix(features_dl)')

	return X
