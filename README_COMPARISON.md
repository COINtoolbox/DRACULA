# Use of Pipeline for the use of data reduction and clustering for mehtods comparison
It is  strongly recomended that you learn how to use the pipeline in the Normal approach before using this.
This new module was introduced to run the pipeline variating one of the set of parameters and comparing the results.
Here a similar configuration file (`config.py`) but with extra keys.
See the advanced section of the README file in HOW_TO_USE_CONFIG to the the possibilities of this configuration file.

* For data reduction:
	* PCA
	* empca
	* DeepLearning (requires `R`, `h2o` for `R` and `rpy2`)
* For clustering:
	* MeanShift
	* KMeans
	* AffinityPropagation
	* AgglomerativeClustering
	* DBSCAN
* For cluster quality testing:
	* silhouette_index
	* Dunn_index
	* DavisBouldin_index
	* vrc

## Requirements
To run fully this pipeline, you will need:

	numpy
	matplotlib
	sklearn

## Basic use
The idea of the code is to get the function of the pipeline and run the code in a outside dir.
You should first prepare your environment with two simple steps.

### Prepare environment
It is very easy to prepare your environment to run the pipeline.
It can be done in 2 steps:

Get the nice functions we prepared. In the pipeline dir, do the command:

	source SOURCE_ME

Create your own dir (preferably outside the pipeline dir) to run the code and copy the `config.py` file there:

	mkdir your_dir
	cd your_dir
	cp PIPELINE_DIR/example_configs/config.py config.py

Now you are ready to run the pipeline functions!

### Pipeline function
Inside your own working dir with the `config.py` file you can use any of these functions:

To run the whole comparison pipeline execute:

	DRAC_COMPARISON

## Outputs
The outputs of reduction methods are placed in `red_data/`.
They will be input for clustering and plotting unless stated otherwise.

The outputs of clustering methods are placed in `cl_data/`.
They will be input for plotting unless stated otherwise.

The outputs of plotting are placed in `plots/`.

All modules also print the information used and resulting in `info/`.
