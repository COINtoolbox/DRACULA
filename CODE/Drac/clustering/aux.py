def ERROR(item):
	out='### ERROR - '+item+' is not a valid key for this CLUSTERING METHOD ###'
	line=''.join(['\n']+['#' for x in out]+['\n'])
	print line+out+line
	exit()
