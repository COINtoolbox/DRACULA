# Explicit configurations of the config file
## Original data:
Used for the reduction, not needed if doing clusreing only

	ORG_DATA	= 'path/data.dat'

## Data Mask
Used for the masking of the reducted data.
This way the PCs can be computed with the whole data sample,
but only the unmasked data will be analysed.
This mask will also be used in plotting the spectra.
If you want to use the data from the pipeline leave it commented.

	MASK_DATA	= 'path/mask.dat'

## Reduction Method
The key `REDUCTION_METHOD` should be a string with the method name.
For each method you can add extra keys already defined by the method
with the original key name plus the prefix `REDUCTION_METHOD'_'`.

Below are the possibilities:

### pca
This uses the pca method and the possible extra keys are

	pca_n_components = int (default=6)

### empca
This uses the empca method and the possible extra keys are

	empca_data_errors_file = [to be completed] (default=None)
	empca_n_components = int (default=6)	
	empca_smooth = int (default=0)	
	empca_n_iter	        = int (default=50)	

### DeepLearning
This uses the DeepLearning method. It requires `R`, the `h2o` package for `R` and `rpy2`.
The possible extra keys are

	DeepLearning_n_layers = int (default=7)
	DeepLearning_training_frame = [ to be completed ]  (default='train.hex')
	DeepLearning_activation = [ to be completed ]  (default='"Tanh"')
	DeepLearning_autoencoder = [ to be completed ]  (default='T')
	DeepLearning_hidden = [ to be completed ]  (default='c(120,100,90,50,30,20,2,20,30,50,90,100,120)')
	DeepLearning_epochs = [ to be completed ]  (default='100')
	DeepLearning_ignore_const_cols' = [ to be completed ]  (default='F')

## Clustering Method
The key `CLUSTERING_METHOD` should be a string with the method name.
For each method you can add extra keys already defined by the method
with the original key name plus the prefix `CLUSTERING_METHOD'_'`.

Below are the possibilities:

### MeanShift
This uses the MeanShift method and the possible extra keys are

	MeanShift_quantile = float (default=.25)
	MeanShift_cluster_all = [ to be completed ] (default=True)

### KMeans
This uses the KMeans method and the possible extra keys are

	KMeans_n_clusters = [ to be completed ] (default=4)
	KMeans_tol = [ to be completed ] (default=1e-4)
	KMeans_init = [ to be completed ] (default='k-means++')
	KMeans_n_jobs = [ to be completed ] (default=1)

### AgglomerativeClustering
This uses the AgglomerativeClustering method and the possible extra keys are

	AgglomerativeClustering_n_clusters = [ to be completed ] (default=6)
	AgglomerativeClustering_affinity = [ to be completed ] (default='euclidean')
	AgglomerativeClustering_linkage = [ to be completed ] (default='ward')

### AffinityPropagation
This uses the AffinityPropagation method and the possible extra keys are

	AffinityPropagation_preference = [ to be completed ] (default=None)
	AffinityPropagation_convergence_iter = [ to be completed ] (default=15)
	AffinityPropagation_max_iter = [ to be completed ] (default=200)
	AffinityPropagation_damping = [ to be completed ] (default=0.5)
	AffinityPropagation_affinity = [ to be completed ] (default='euclidean')

### DBSCAN
This uses the DBSCAN method and the possible extra keys are

	DBSCAN_eps		= [ to be completed ] (default=0.5)
	DBSCAN_min_samples	= [ to be completed ] (default=5)
	DBSCAN_metric	= [ to be completed ] (default='euclidean')
	DBSCAN_algorithm	= [ to be completed ] (default='auto')
	DBSCAN_leaf_size	= [ to be completed ] (default=30)

## Quality test methods
The key	`QUALITY_METHODS` should be a vector of strings of quality method checks for clustering.
An example of this key, could be:

	QUALITY_METHODS=['method1','method2','method3']

Below are the possibilities:

### silhouette

	silhouette_metric	= [to be completed] (default='euclidean')


### DavisBouldin

	DavisBouldin_metric	= [to be completed] (default='euclidean')


### Dunn

	Dunn_metric	= [to be completed] (default='euclidean')


### vrc

	vrc_metric	= [to be completed] (default='euclidean')



## Clustering output extension
Extension of output plots produced by pylab, should be a string.

## Using Externa data
If you want to use external data with reductions, clusters and labels you just have to add the keys below.
If they are not set, the default will come from the pipeline.

### External data for clustering
Add this ONLY if you want to use a external data source for the clustering,
if you want to use the data from the pipeline leave it commented.
Be aware that this data will also go into the plotting.

	REDUCED_DATA_EXTERNAL		= 'path/reduced_data.dat'

### External data for plotting results
Add this ONLY if you want to use a external data source of the clusters for the plotting,
if you want to use the data from the pipeline leave it commented.

	CLUSTERS_DATA_EXTERNAL		= 'path/external_clusters.dat'

You can also add an external file with different label to set different colors
to the reduced data. The default color scheme is according to each parent cluster.

	LABELS_DATA_EXTERNAL		= 'path/external_labels.dat'

### External data for plotting spectra
Add this ONLY if you want to use a external data source of the sprectra for the plotting,
if you want to use the data from the pipeline leave it commented.

	SPECTRAL_DATA_EXTERNAL		= 'path/external_spectra.dat'

## Advanced plotting
If you want other options, there are a few available using keys in the terminal when executing the `PLOT` and `PLOT_SPECS` commands.
Check the main README for more information.

# Advanced Use
This part is of interest only if you want to make comparisons among different configurations.
It concerns the config_comparison.py file.

This config file should contail all the information necessary for the config.py file,
plus these extra keys:

## Var Type
This key says if the variation of parameter is on the reduction part or on the clustering part.

	VAR_TYPE	= 'CLUSTERING' or 'REDUCTION'

## Var Par
This key must have the name of the parameter that is being variated.
It can be the reduction/clustering method or one of the reduction/clustering parameters.

	VAR_PAR	= 'REDUCTION_METHOD' or 'CLUSTERING_METHOD' or 'MeanShift_quantile' or ...

## Var Values
This key must have an array with the values of the parameter that is being variated.
If the parameter is a number it must be a list of numbers,
if the parameter is a string it must be a list of string,
if the parameter is a vector it must be a list of vector.

	VAR_VALS	= [1,2,3] or ['name1','name2','name2'] or [vec1,vec2,vec3]
