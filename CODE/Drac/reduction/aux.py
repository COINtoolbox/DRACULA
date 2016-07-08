def ERROR(item):
	out='### ERROR - '+item+' is not a valid key for this REDUCTION METHOD ###'
	line=''.join(['\n']+['#' for x in out]+['\n'])
	print line+out+line
	exit()
