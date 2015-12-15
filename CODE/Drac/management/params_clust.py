from __future__ import print_function
MeanShift_dict=dict([
	[ 'quantile'	, .25	],
	[ 'cluster_all'	, True	],
])

KMeans_dict=dict([
	[ 'n_clusters'	, 4		],
	[ 'tol'		, 1e-4		],
	[ 'init'	, 'k-means++'	],
	[ 'n_jobs'	, 1		],
])

AgglomerativeClustering_dict=dict([
	[ 'n_clusters'	, 6		],
	[ 'affinity'	, 'euclidean'	],
	[ 'linkage'	, 'ward'	],
])

AffinityPropagation_dict=dict([
	[ 'preference'		, None		],
	[ 'convergence_iter'	, 15		],
	[ 'max_iter'		, 200		],
	[ 'damping'		, 0.5		],
	[ 'affinity'		, 'euclidean'	],
])

DBSCAN_dict=dict([
	[ 'eps'		, 0.5		],
	[ 'min_samples'	, 5		],
	[ 'metric'	, 'euclidean'	],
	[ 'algorithm'	, 'auto'	],
	[ 'leaf_size'	, 30		],
])
