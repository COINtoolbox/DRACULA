# Use of DRACULA for comparison of dimensionality reduction and clustering methods
It is  strongly recomended that you learn how to use DRACULA in the Normal approach before using this.
This new module was introduced to vary one set of parameters and compare its results.
Here a similar configuration file (`config.py`) is necessary, but with extra keys.
See the advanced section of the README file in HOW_TO_USE_CONFIG to see the possibilities of this configuration file.


### DRACULA function
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
