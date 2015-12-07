from __future__ import print_function
from config import *

def update_dict(DICT,prefix):
	print('\t* checking for',prefix,'updates *')
	updates=False
	for item0 in DICT:
		item=prefix+'_'+item0
		try:
			exec(item)
		except NameError:
			pass
		else:
  			print ('\t\t-',item0,"\t was updated from",DICT[item0],"to",eval(item))
			DICT[item0]=eval(item)
			updates=True
	if updates==False: print('\t\t<no updates>')
	print('')
