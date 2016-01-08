# Use of DRACULA for the visualization of the clustering of the data using SOM
In this module, the SOM method is used.
It should be used for visualization of the possible clustering of the data.
This use does not folow the steps of the pipeline.
Be careful for this module may take a realy long time according to the parameters chosen.
The configuration file is `config_som.py`.


## Requirements
To run this module, you will need:

[numpy](http://www.numpy.org/)

[matplotlib](http://matplotlib.org/)

[sklearn](http://scikit-learn.org/stable/)

[minisom](https://github.com/JustGlowing/minisom)


### Configuration file
Note that the SOM module has its own configuration file `config_som.py`.
As this config file is used exclusively for SOM,
there is no need for adding a prefix `SOM_` before the extra parameters
as it is done in the main pipeline.

### Pipeline function
Inside your own working dir with the `config_som.py` file you can use any of these functions:

To run the whole som pipeline execute:

	DRAC_SOM

## Outputs
The outputs of placed in `som_res/`.
