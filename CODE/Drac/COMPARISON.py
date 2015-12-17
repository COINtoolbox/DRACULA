#!/usr/bin/env python
from __future__ import print_function
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(''))
def PRT_FMSG(msg_ok,msg_fail,FILE):
	if os.path.isfile(FILE) : print('\t*',msg_ok,'->',FILE)
	else 			: print('\t*',msg_fail,'- no',FILE,'file')
def PRT_FMSG_PLT(msg_ok,msg_fail,FILE):
	if FILE[-3:]=='pdf': PRT_FMSG(msg_ok,msg_fail,FILE)
	else:
		for Q in QUALITY_METHODS: PRT_FMSG(msg_ok,msg_fail,FILE[:-4]+'_'+Q+FILE[-4:])

from config_comparison import *
import config_comparison

if os.path.isfile('config.py'):
	if open('config.py', 'r').readline().split()[0]!='#TEMPCONFIG':
		print('ATENTION!!!\n\t<< moving config.py to config.safe.py >>\n')
		os.system('cp config.py config.safe.py')


def run_comparison():
	BASE_CONF='#TEMPCONFIG\n'
	for item in dir(config_comparison):
		if item[:2]!='__' and item!='VAR_PAR' and item!='VAR_VALS' :
			exec('temp='+item)
			if isinstance(temp, str): temp='"'+str(temp)+'"'
			BASE_CONF += item+'='+str(temp)+'\n'
	
	Qmat=[]
	for VAL,ind in zip(VAR_VALS,range(1,1+len(VAR_VALS))):
		CASE_LINE="******************* CASE "+str(ind)+" *******************************************"
		BORD_LINE=''
		for x in CASE_LINE: BORD_LINE+='*'
		if isinstance(VAL, str)	: VAL='"'+str(VAL)+'"'
		else 			: VAL=str(VAL)
		case,case_red='.case'+str(ind),''
	
		os.system('rm -rf config.pyc')
		fconf=open('config.py','w')
		print(BASE_CONF+VAR_PAR+'='+VAL,file=fconf)
		print(BASE_CONF+VAR_PAR+'='+VAL)
		fconf.close()
		import Main
	
		print (BORD_LINE);print (CASE_LINE);print (BORD_LINE)
		reload(Main)
		from Main import reduc,cluster,do_quality,plot,plot_spec
		if VAR_TYPE=='REDUCTION':
			print ("\t** REDUCTION **\n")
			case_red=case 
			reduc(case)
			print ('\t\t[ok]\n')
		elif VAR_TYPE=='CLUSTERING': pass 
		else: print('\t**ERROR** - VAR_TYPE is neither REDUCTION nor CLUSTERING');exit()
	
		print ("\t** CLUSTERING **\n")
		Qvec=[len(set(cluster(case_red,case)[1]))]
		print ('\t\t[ok]\n')
	
		print ("\t** QUALITY CHECK **\n")
		Qmat.append(Qvec+do_quality(case_red,case))
		print ('\t\t[ok]\n')
	
	fqual=open('quality_comparison.dat','w')
	print('#\tn_clust',end='',file=fqual)
	for qtest in QUALITY_METHODS:	print('\t',qtest,end='',file=fqual)
	print('',file=fqual)
	for Qvec in Qmat:
		for q in Qvec: print('\t',q,end='',file=fqual)
		print('',file=fqual)
	fqual.close()

from plotting.plot_quality import plot_quality
def plot_comparison():
	os.system('mkdir -p plots/')
	plot_quality(QUALITY_METHODS,'plots/quality'+PLOT_QUA_EXT)
	PRT_FMSG_PLT('QUALITY PLOT generated at','QUALITY PLOT not generated','plots/quality'+PLOT_QUA_EXT)
	print ('\t[ok]\n')
