from __future__ import print_function
pca_dict=dict([
	[ 'n_components'	, 6	],
])

kpca_dict=dict([
	[ 'n_components'	, 6	],
	[ 'kernel'	        , 'linear'	],
])

empca_dict=dict([
	[ 'errors_file'	        , None	],
	[ 'n_components'	, 6			],
        [ 'smooth'	        , 0			],
	[ 'n_iter'	        , 50			],
])

DeepLearning_dict=dict([
	[ 'n_layers'		, 7						],
	[ 'training_frame'	, 'train.hex'					],
	[ 'activation'		, '"Tanh"'					],
	[ 'autoencoder'		, 'T'						],
	[ 'hidden'		, 'c(120,100,90,50,30,20,2,20,30,50,90,100,120)'],
	[ 'epochs'		, '100'						],
	[ 'ignore_const_cols'	, 'F'						],
])
