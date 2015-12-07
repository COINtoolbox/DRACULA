# Pipeline for the use of data reduction and clustering
Pipeline to use all methods of data reduction and clustering.
Some cluster quality methods were also implemented.
So far we have implemented:

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


There are two approaches for using the pipeline
* Normal Use:

	In this way all the settings of the pipeline are set by a configuration file (`config.py`).
	It only produces results for one specific configuration in each run.
	See the README file in HOW_TO_USE_CONFIG to the the possibilities of the configuration file.
* Advanced Use:

	It is  strongly recomended that you learn how to use the pipeline in the Normal approach before using this.
	This new module was introduced to run the pipeline variating one of the set of parameters and comparing the results.
	Here a similar configuration file (`config_comparison.py`) but with extra keys.
	See the advanced section of the README file in HOW_TO_USE_CONFIG to the the possibilities of this configuration file.


### Prepare environment
It is very easy to prepare your environment to run the pipeline.
It can be done in 2 steps:

Get the nice functions we prepared. In the pipeline dir, do the command:

	source SOURCE_ME

Create your own dir (preferably outside the pipeline dir) to run the code and copy the config.py file there:

	mkdir your_dir
	cd your_dir
	cp PIPELINE_DIR/example_config.py config.py

Now you are ready to run the pipeline functions!

### Pipeline function
Inside your own working dir with the config.py file you can use any of these functions:

To run the whole pipeline execute:

	ALL

To run just the reduction part execute:

	REDUCTION

To run just the clustering execute:

	CLUSTERING

To run just the clustering quality execute:

	QUALITY

To run just the plotting execute:

	PLOT

To run just the plotting of the spectra by gorups execute:

	PLOT_SPECS

Remeber, all cases are configured by:

	config.py

If you are running the pipeline for comparison (see Advanced Use),
the command is:

	COMPARISON

and the configuration file is:

	config_comparison.py

## Outputs
The outputs of reduction methods are placed in `red_data/`.
They will be input for clustering and plotting unless stated otherwise.

The outputs of clustering methods are placed in `cl_data/`.
They will be input for plotting unless stated otherwise.

The outputs of plotting are placed in `plots/`.

All modules also print the information used and resulting in `info/`.

## Adding your code
If you want to add your code to the pipeline, put it in the one of the following dirs inside the pipeline and we will format it for you:

	EXTERNAL_CODES/clustering/
	EXTERNAL_CODES/reduction/

## Sharing plots
If you want to share plots done with (or without) the pipeline,
put them in

	share_plots/

Please mind the name of your plots so you don't overwrite other peoples results.

## Advanced plotting of results
The default plot of the results are in a figure (.png) with all the PCs colored according to the clusters.
If you want to change the extension of the figure or the color arrangement,
change the parameters in the config file (see HOW_TO_USE_CONFIG README).

If you want other options, there are a few available using keys in the terminal when executing the `PLOT` command.
Here are the plossibilities:

	-nd	(or --no_diag	) : do not plot diagonal
	-nf	(or --no_fit	) : do not fit in all dimensions simultanniously
	-nc	(or --no_colors	) : do not use colors
	-nl	(or --no_label	) : do not plot label
	-w	(or --window	) : keep plot in interactive window, this will not save the output automaticaly
	-pp	(or --plot_pars	) : plot specified pars, takes a string as input (ex: "1 2")
	-hs	(or --horiz_space) : set horizontal spacing between the plots
	-vs	(or --vert_space) : set vertical spacing between the plots

You can also see them by executing

	PLOT -h


## Advanced plotting of spectra
A plot of the orginial spectra by groups is also produced in a figure (.pdf).
The main figure shows the mean value of the spectra of each cluster found.

If you add the key -a , it will also produce a individual plot for each cluster with all the spectra and the mean value.
In the default option of extension (.pdf), all plots are grouped in a single file with multiple pages.
In other cases a extra file for each cluster will be created.

The parameters for plotting the spectra are:

	-w	(or --window	) : keep plot in interactive window, this will not save the output automaticaly
	-a	(or --all_spec	) : plot all spectra

You can also see them by executing

	PLOT_SPECS -h
