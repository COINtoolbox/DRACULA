#####################################################################################
'''
Original data:
	Used for the reduction,
	not needed if doing clusreing only
'''
ORG_DATA			= '../../../Dropbox/shared/coin_br/test_data/fake_2clust_2pcacomp.dat'

#####################################################################################
'''
Mask of data:
	Used for the masking of the reducted data.
	This way the PCs can be computed with the whole data sample,
	but only the unmasked data will be analysed.
	This mask will also be used in plotting the spectra.
	If you want to use the data from the pipeline leave it commented.
'''
#MASK_DATA		= '../../../Dropbox/shared/coin_br/test_data/fake_2clust_2pca_mask.dat'

#####################################################################################
'''
REDUCTION METHOD
	possibilities:
		-pca
	The aditional parameters must be added with the same name
	as in the original function plus the prefix REDUCTION_METHOD'_'.
	Example:
		if REDUCTION_METHOD is 'pca', the parameter
		n_components must be declared as 
			pca_n_components= ...
		if REDUCTION_METHOD is 'empca', the parameter
		error_file can be declared as 
			empca_errors_file= ...
                in order to run with weights=1/errors^2. Its default value is
                None, so empca runs without weights
'''
REDUCTION_METHOD	= 'pca'

#####################################################################################
'''
CLUSTERING METHOD
	possibilities:
		-MeanShift
		-KMeans
		-AffinityPropagation
		-AgglomerativeClustering
		-DBSCAN

	The aditional parameters must be added with the same name
	as in the original function plus the prefix CLUSTERING_METHOD'_'
	Example:
		if CLUSTERING_METHOD is 'MeanShift', the parameter 
		quantile must be declared as 
			MeanShift_quantile= ...

'''
CLUSTERING_METHOD	= 'MeanShift'

#####################################################################################
'''
CLUSTERING OUTPUT EXTENSIONS
	extension of plots of result and spectra produced by pylab
'''
PLOT_EXT	= '.png'
PLOT_SPEC_EXT	= '.pdf'

#####################################################################################
'''
QUALITY TEST METHODS
	put one or more (as a vector) quality checks for clustering. possibilities are:
		-silhouette_index
		-Dunn_index
		-DavisBouldin_index
		-vrc

'''
QUALITY_METHODS=['silhouette_index','Dunn_index','DavisBouldin_index','vrc']

#####################################################################################
'''
CLUSTERING INPUT DATA
	add this ONLY if you want to use a external data source for the clustering,
	if you want to use the data from the pipeline leave it commented.
	Be aware that this data will also go into the plotting.
'''
#REDUCED_DATA_EXTERNAL		= '../empca_trained_coeff/coefficients.dat'

#####################################################################################
'''
PLOTTING INPUT DATA
	add this ONLY if you want to use a external data source of the clusters for the plotting,
	if you want to use the data from the pipeline leave it commented.
	You can also add an external file with different label to set different colors
	to the reduced data. The default color scheme is according to each parent cluster.
'''
#CLUSTERS_DATA_EXTERNAL		= '../empca_trained_coeff/coefficients.dat'
#LABELS_DATA_EXTERNAL		= '../empca_trained_coeff/coefficients.dat'
#SPECTRAL_DATA_EXTERNAL		= '../empca_trained_coeff/coefficients.dat'

#####################################################################################
'''
COMPARISON PART !!!
'''

VAR_TYPE	= 'CLUSTERING' # 'REDUCTION'
VAR_PAR		= 'CLUSTERING_METHOD' #MeanShift_quantile
VAR_VALS	= ['MeanShift','KMeans']
PLOT_QUA_EXT	= '.pdf'

