from __future__ import print_function


def update_dict(DICT,prefix='',conf_file='config'):
	exec('from '+conf_file+' import *')
	print('\t* checking for',prefix,'updates *')
	updates=False
	pref=''
	if prefix!='': pref=prefix+'_'
	for item0 in DICT:
		item=pref+item0
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
