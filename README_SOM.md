# Use of Pipeline for the visualization of the clustering of the data using SOM
In this module, the SOM method is used.
It should be used for visualization of the possible clustering of the data.
This use does not folow the steps of the pipeline.
Be careful for this module may take a realy long time according to the parameters chosen.
The configuration file is `config_som.py`.


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

Create your own dir (preferably outside the pipeline dir) to run the code and copy the `config_som.py` file there:

	mkdir your_dir
	cd your_dir
	cp PIPELINE_DIR/example_configs/config_som.py config_som.py

Now you are ready to run the pipeline functions!

### Pipeline function
Inside your own working dir with the `config_som.py` file you can use any of these functions:

To run the whole som pipeline execute:

	DRAC_SOM

## Outputs
The outputs of placed in `som_res/`.
