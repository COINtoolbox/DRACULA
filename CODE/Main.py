from __future__ import print_function
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(''))

import config
reload(config)
from config import *

import management.update_dict
reload(management.update_dict)
from management.update_dict import update_dict

from management.name_files import create_name,plot_name
from management.info_work import prt,print_info,read_info

def ERROR(message):
	out='### **ERROR** - '+message+' ####'
	line='\n'
	for x in out: line+='#'
	line+='\n'
	print(line+out+line)
	exit()
def READ(NAME,MASK=''):
	if os.path.isfile(NAME):
		if MASK==''	: return np.loadtxt(NAME)
		else		: return np.loadtxt(NAME)[np.loadtxt(MASK)==1]
	else: ERROR('file '+NAME+' does not exist!')
def PRT_FMSG(msg_ok,msg_fail,FILE):
	if os.path.isfile(FILE) : print('\t*',msg_ok,'->',FILE)
	else 			: print('\t*',msg_fail,'- no',FILE,'file')

print('''
################################################
########## BEGINNING HMV PIPELINE ##############
################################################
''')
#############################
#### UPDATE DICTS AND	 ####
#### CREATE FILE NAMES	 ####
#############################
exec('from management.params_red import '+REDUCTION_METHOD+'_dict as dict_red')
update_dict(dict_red,REDUCTION_METHOD)
RED_DATA_NAME=create_name(REDUCTION_METHOD,dict_red,'red_data/reduced_data_')

exec('from management.params_clust import '+CLUSTERING_METHOD+'_dict as dict_clust')
update_dict(dict_clust,CLUSTERING_METHOD)
CLUSTERS_DATA_NAME = create_name(CLUSTERING_METHOD,dict_clust,'cl_data/clustering_')
CLUSTERS_LABEL_NAME= create_name(CLUSTERING_METHOD+'_label',dict_clust,'cl_data/clustering_')

info_dir='info/'
os.system('mkdir -p '+info_dir)
info_sufix='.info'
REDUCTION_INFO	= info_dir + 'reduction' 	+ info_sufix
CLUSTER_INFO	= info_dir + 'clustering'	+ info_sufix
QUALITY_INFO	= info_dir + 'quality'		+ info_sufix
PLOT_INFO	= info_dir + 'plot'		+ info_sufix
PLOTSPEC_INFO	= info_dir + 'plot_spec'	+ info_sufix
#############################
#### CHECK FOR EXT FILES ####
#############################
try:
	MASK_DATA
except NameError: MASK=''
else		: MASK=MASK_DATA
try:
	REDUCED_DATA_EXTERNAL
except NameError: RED_DATA,RED_TYPE=RED_DATA_NAME,REDUCTION_METHOD
else		: RED_DATA,RED_TYPE=REDUCED_DATA_EXTERNAL,'EXT';print('\t- using external reduced data')

try:
	CLUSTERS_DATA_EXTERNAL
except NameError: CL_DATA,CL_TYPE=CLUSTERS_DATA_NAME,CLUSTERING_METHOD
else		: CL_DATA,CL_TYPE=CLUSTERS_DATA_EXTERNAL,'EXT';print('\t- using external clusters')

try:
	LABELS_DATA_EXTERNAL
except NameError: LAB_DATA=CLUSTERS_LABEL_NAME
else		: LAB_DATA=LABELS_DATA_EXTERNAL;print('\t- using external labels')
try:
	SPECTRAL_DATA_EXTERNAL
except NameError: SPEC_DATA=ORG_DATA
else		: SPEC_DATA=SPECTRAL_DATA_EXTERNAL;print('\t- using external spectral for plotting')
	
#############################
#### REDUCTION PART	 ####
#############################
def reduc(case=''):
	try:
		REDUCED_DATA_EXTERNAL
	except NameError: pass
	else		: print ("REDUCED_DATA_EXTERNAL is defined, please check what you realy want to do!"); exit()
	exec('from reduction.'+REDUCTION_METHOD+' import reduction')
	os.system('mkdir -p red_data')
	try:
		ORG_DATA
	except NameError: ERROR('ORG_DATA key missing!')
	else:	
		np.savetxt(RED_DATA_NAME+case,reduction(READ(ORG_DATA),dict_red))
		print_info(REDUCTION_METHOD,dict_red,'### REDUCTION USED ###',ORG_DATA,REDUCTION_INFO+case)
		PRT_FMSG('REDUCTED DATA printed to','REDUCED DATA not printed',RED_DATA_NAME+case)

#############################
#### CLUSTERING PART	 ####
#############################
def cluster(case_in='',case_out=''):
	try:
		CLUSTERS_DATA_EXTERNAL
	except NameError: pass
	else		: print ("CLUSTERS_DATA_EXTERNAL is defined, please check what you realy want to do!"); exit()
	exec('from clustering.'+CLUSTERING_METHOD+' import clustering')
	os.system('mkdir -p cl_data')
	clusters,labels= clustering(READ(RED_DATA+case_in,MASK),dict_clust)
	np.savetxt(CLUSTERS_DATA_NAME+case_out,clusters)
	np.savetxt(CLUSTERS_LABEL_NAME+case_out,labels)
	try:
		REDUCED_DATA_EXTERNAL
	except NameError: RED_PROP=open(REDUCTION_INFO+case_in,'r').read()
	else		: RED_PROP='### REDUCTION USED ###\nfrom external data = '+REDUCED_DATA_EXTERNAL
	prt(CLUSTER_INFO+case_out,RED_PROP,'w')
	print_info(CLUSTERING_METHOD,dict_clust,'### CLUSTERING USED ###',RED_DATA,CLUSTER_INFO+case_out,'a')
	prt(CLUSTER_INFO+case_out,'\n\t-outputs:','a')
	prt(CLUSTER_INFO+case_out,'n_clusters = '+str(clusters.shape[0]),'a')
	PRT_FMSG('CLUSTER CENTERS printed to','CLUSTERS CENTERS not printed',CLUSTERS_DATA_NAME+case_out)
	PRT_FMSG('CLUSTER LABELS printed to','CLUSTERS LABELS not printed',CLUSTERS_LABEL_NAME+case_out)
	return clusters,labels
	
#############################
#### QUALITY CHECK PART	 ####
#############################
def check_quality(METHOD,case_red='',case=''):
	exec('from management.params_quality import '+METHOD+'_dict as dict_qual')
	update_dict(dict_qual,METHOD)
	exec ('from quality.'+METHOD+' import quality')
	q=quality(READ(RED_DATA+case_red),READ(CL_DATA+case),READ(LAB_DATA+case),dict_qual)
	return q
def do_quality(case_red='',case=''):
	try:
		QUALITY_METHODS
	except NameError: ERROR('QUALITY_METHODS key missing!')
	else:
		used=False
		try:
			CLUSTERS_DATA_EXTERNAL
		except NameError: CL_PROP=open(CLUSTER_INFO+case,'r').read()
		else		: CL_PROP='### CLUSTERS USED ###\nfrom external data = '+CLUSTERS_DATA_EXTERNAL
		prt(QUALITY_INFO+case,CL_PROP,'w')
		prt(QUALITY_INFO+case,'### QUALITIES USED ###','a')
		prt(QUALITY_INFO+case,'INPUT_DATA = '+CL_DATA,'a')
		for METHOD in QUALITY_METHODS:
			print_info(METHOD,dict_clust,'','',QUALITY_INFO+case,'a')
		prt(QUALITY_INFO+case,'\n\t-outputs:','a')
		Qvec=[]
		for METHOD in QUALITY_METHODS:
			if METHOD!='':
				q=check_quality(METHOD,case_red,case)
				print('\tquality from',METHOD,':',q,'\n')
				prt(QUALITY_INFO+case,'quality from '+METHOD+' = '+str(q),'a')
				used=True
				Qvec.append(q)
		PRT_FMSG('QUALITY results printed to','QUALITY results not printed',QUALITY_INFO+case)
		if used: return Qvec
		else:
			print('\t<no quality checks>')
			prt(QUALITY_INFO+case,'\t<no quality checks>')

#############################
#### PLOTTIING PART	 ####
#############################
def plot():
	from plotting.plot import plot_data
	PLOT_NAME=plot_name(RED_TYPE,CL_TYPE,dict_red,dict_clust,PLOT_EXT)
	os.system('mkdir -p plots')
	plot_data(READ(RED_DATA,MASK).T,READ(CL_DATA).T,READ(LAB_DATA),PLOT_NAME)
	try:
		CLUSTERS_DATA_EXTERNAL
	except NameError: CL_PROP=open(CLUSTER_INFO,'r').read()
	else		: CL_PROP='### CLUSTERS USED ###\nfrom external data = '+CLUSTERS_DATA_EXTERNAL
	prt(PLOT_INFO,CL_PROP,'w')
	PRT_FMSG('PLOT generated at','PLOT file not generated',PLOT_NAME)
def plot_spec():
	from plotting.plot_specs import plot_spectra
	PLOT_NAME=plot_name(RED_TYPE,CL_TYPE,dict_red,dict_clust,'_specs'+PLOT_SPEC_EXT)
	os.system('mkdir -p plots')
	plot_spectra(READ(SPEC_DATA,MASK),READ(LAB_DATA),PLOT_NAME)
	try:
		CLUSTERS_DATA_EXTERNAL
	except NameError: CL_PROP=open(CLUSTER_INFO,'r').read()
	else		: CL_PROP='### CLUSTERS USED ###\nfrom external data = '+CLUSTERS_DATA_EXTERNAL
	prt(PLOTSPEC_INFO,CL_PROP,'w')
	PRT_FMSG('SPECS PLOT generated at','SPECS PLOT not generated',PLOT_NAME)
