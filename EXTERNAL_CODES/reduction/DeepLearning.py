from rpy2.robjects import r
import numpy as np

## this is the training sample
#in_file = "../data_all_types/derivatives_train.dat"
in_file = "../data_all_types/derivatives.dat"

run_dir='./'

# layers
input_string = '120,100,90,50,30,20,2,20,30,50,90,100,120'
# the output layer is the 7th, the central one
n_layers = 7
# random seed
seed = 1

in_param = 'training_frame = train2.hex, activation = "Tanh", autoencoder=T, hidden = c(%s), epochs=100, ignore_const_cols = F, seed = %d, reproducible = TRUE '  % (input_string,seed)

in_data = np.loadtxt(in_file)
size_in_data = np.shape(in_data)[1]

in_param = 'x=1:%d,' % (size_in_data) + in_param

#temp input file
in_file_cvs=run_dir+'.temp_file.cvs'
np.savetxt(in_file_cvs, in_data, delimiter=',', fmt='%.18f')

## define libraries
r('library(h2o)')
  
## Read data
r('h2oServer <- h2o.init(nthreads=-1)')

r('TRAIN = "%s" '% (in_file_cvs))

r('train2.hex <- h2o.importFile(h2oServer, path = TRAIN, header = F, sep = ",", destination_frame="train2.hex")')

## Construct deep learning model
r('dlmodel <- h2o.deeplearning( %s ) ' % (in_param))

## Generate new features
r('features_dl <- h2o.deepfeatures(dlmodel, train2.hex, layer=%d)' % (n_layers))
r('head(features_dl)')

## Store new features in file
X = r('as.matrix(features_dl)')
np.savetxt(run_dir+'out_DeepLearning/out_%s_seed%d_dl.dat' % (input_string,seed)  ,X)



# this is the test sample 
in_file = "../data_all_types/derivatives.dat"
#in_file = "../data_all_types/derivatives_test.dat"

in_data = np.loadtxt(in_file)

in_file_cvs=run_dir+'.temp_file.cvs'
np.savetxt(in_file_cvs, in_data, delimiter=',', fmt='%.18f')

## Read data
r('h2oServer <- h2o.init(nthreads=-1)')

r('TEST = "%s" '% (in_file_cvs))

r('test.hex <- h2o.importFile(h2oServer, path = TEST, header = F, sep = ",", destination_frame="test.hex")')

## Generate predictions
r('predictions_dl <- h2o.predict(dlmodel, test.hex)')
r('head(predictions_dl)')

## Store new predictions in file
pred = r('as.matrix(predictions_dl)')
np.savetxt(run_dir+'out_DeepLearning/predictions_%s_seed%d_dl.dat' % (input_string,seed) ,pred)

# close h2o server
r('h2o.shutdown(prompt=F)')

  
