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

#############################
#### UPDATE DICTS AND	 ####
#### CREATE FILE NAMES	 ####
#############################
def set_red_dict(REDUCTION_METHOD):
	exec('from management.params_red import '+REDUCTION_METHOD+'_dict as dict_red')
	update_dict(dict_red,REDUCTION_METHOD)
	return dict_red
def set_cl_dict(CLUSTERING_METHOD):
	exec('from management.params_clust import '+CLUSTERING_METHOD+'_dict as dict_clust')
	update_dict(dict_clust,CLUSTERING_METHOD)
	return dict_clust
#############################
#### CHECK FOR EXT FILES ####
#############################
def set_mask():
	try		: MASK_DATA
	except NameError: return ''
	else		: return MASK_DATA
def set_red(dict_red,REDUCTION_METHOD):
	try		: REDUCED_DATA_EXTERNAL
	except NameError: return create_name(REDUCTION_METHOD,dict_red,'red_data/reduced_data_'),REDUCTION_METHOD
	else		: print('\t- using external reduced data'); return REDUCED_DATA_EXTERNAL,'EXT'
def set_cl(dict_clust,CLUSTERING_METHOD):
	try		: CLUSTERS_DATA_EXTERNAL
	except NameError: return create_name(CLUSTERING_METHOD,dict_clust,'cl_data/clustering_'),CLUSTERING_METHOD
	else		: print('\t- using external clusters');return CLUSTERS_DATA_EXTERNAL,'EXT'
def set_lab(dict_clust,CLUSTERING_METHOD):
	try		: LABELS_DATA_EXTERNAL
	except NameError: return create_name(CLUSTERING_METHOD+'_label',dict_clust,'cl_data/clustering_')
	else		: print('\t- using external labels');return LABELS_DATA_EXTERNAL
def set_spec():
	try		: SPECTRAL_DATA_EXTERNAL
	except NameError: return ORG_DATA
	else		: print('\t- using external spectral for plotting');return SPECTRAL_DATA_EXTERNAL
################################
#### CREATE CLASS CONFIG #######
################################
class set_prop:
	def __init__(self): 
		info_dir,info_sufix	= 'info/','.info'
		self.REDUCTION_INFO	= info_dir + 'reduction' 	+ info_sufix
		self.CLUSTER_INFO	= info_dir + 'clustering'	+ info_sufix
		self.QUALITY_INFO	= info_dir + 'quality'		+ info_sufix
		self.PLOT_INFO		= info_dir + 'plot'		+ info_sufix
		self.PLOTSPEC_INFO	= info_dir + 'plot_spec'	+ info_sufix
		os.system('mkdir -p '+info_dir)

		self.REDUCTION_METHOD	= REDUCTION_METHOD	
		self.CLUSTERING_METHOD	= CLUSTERING_METHOD	

		self.dict_red	= set_red_dict(self.REDUCTION_METHOD)
		self.dict_clust	= set_cl_dict(self.CLUSTERING_METHOD)

		self.MASK			= set_mask()
		self.RED_DATA,self.RED_TYPE	= set_red(self.dict_red,self.REDUCTION_METHOD)
		self.CL_DATA,self.CL_TYPE	= set_cl(self.dict_clust,self.CLUSTERING_METHOD)
		self.LAB_DATA			= set_lab(self.dict_clust,self.CLUSTERING_METHOD)
		self.SPEC_DATA			= set_spec()
	def update(self,VAR_TYPE,VAR_PAR,VAL):
		if VAR_TYPE=='REDUCTION' :
			if VAR_PAR=='REDUCTION_METHOD'  : self.dict_red, self.REDUCTION_METHOD			= set_red_dict(VAL), VAL
			else				: self.dict_red[VAR_PAR[len(self.REDUCTION_METHOD)+1:]]	= eval(VAL)
		if VAR_TYPE=='CLUSTERING': 
			if VAR_PAR=='CLUSTERING_METHOD' : self.dict_clust, self.CLUSTERING_METHOD			= set_cl_dict(VAL), VAL
			else				: self.dict_clust[VAR_PAR[len(self.CLUSTERING_METHOD)+1:]]	= eval(VAL)
		

	
#############################
#### REDUCTION PART	 ####
#############################
def reducC(CONFIG,case=''):
	if CONFIG.RED_TYPE =='EXT': print ("REDUCED_DATA_EXTERNAL is defined, please check what you realy want to do!"); exit()

	exec('from reduction.'+CONFIG.REDUCTION_METHOD+' import reduction')
	os.system('mkdir -p red_data')
	try		: ORG_DATA
	except NameError: ERROR('ORG_DATA key missing!')
	else		:	
		np.savetxt(CONFIG.RED_DATA+case,reduction(READ(ORG_DATA),CONFIG.dict_red))
		print_info(CONFIG.REDUCTION_METHOD,CONFIG.dict_red,'### REDUCTION USED ###',ORG_DATA,CONFIG.REDUCTION_INFO+case)
		PRT_FMSG('REDUCTED DATA printed to','REDUCED DATA not printed',CONFIG.RED_DATA+case)

#############################
#### CLUSTERING PART	 ####
#############################
def clusterC(CONFIG,case_in='',case_out=''):
	if CONFIG.CL_TYPE =='EXT': print ("CLUSTERS_DATA_EXTERNAL is defined, please check what you realy want to do!"); exit()

	exec('from clustering.'+CONFIG.CLUSTERING_METHOD+' import clustering')
	os.system('mkdir -p cl_data')
	clusters,labels= clustering(READ(CONFIG.RED_DATA+case_in,CONFIG.MASK),CONFIG.dict_clust)
	np.savetxt(CONFIG.CL_DATA+case_out,clusters)
	np.savetxt(CONFIG.LAB_DATA+case_out,labels)

	if CONFIG.RED_TYPE =='EXT': RED_PROP='### REDUCTION USED ###\nfrom external data = '+REDUCED_DATA_EXTERNAL
	else			  : RED_PROP=open(CONFIG.REDUCTION_INFO+case_in,'r').read()

	prt(CONFIG.CLUSTER_INFO+case_out,RED_PROP,'w')
	print_info(CONFIG.CLUSTERING_METHOD,CONFIG.dict_clust,'### CLUSTERING USED ###',CONFIG.RED_DATA,CONFIG.CLUSTER_INFO+case_out,'a')
	prt(CONFIG.CLUSTER_INFO+case_out,'\n\t-outputs:','a')
	prt(CONFIG.CLUSTER_INFO+case_out,'n_clusters = '+str(clusters.shape[0]),'a')
	PRT_FMSG('CLUSTER CENTERS printed to','CLUSTERS CENTERS not printed',CONFIG.CL_DATA+case_out)
	PRT_FMSG('CLUSTER LABELS printed to','CLUSTERS LABELS not printed',CONFIG.LAB_DATA+case_out)
	return clusters,labels
	
#############################
#### QUALITY CHECK PART	 ####
#############################
def check_quality(CONFIG,METHOD,case_red='',case=''):
	exec('from management.params_quality import '+METHOD+'_dict as dict_qual')
	update_dict(dict_qual,METHOD)
	exec ('from quality.'+METHOD+' import quality')
	q=quality(READ(CONFIG.RED_DATA+case_red),READ(CONFIG.CL_DATA+case),READ(CONFIG.LAB_DATA+case),dict_qual)
	return q
def do_qualityC(CONFIG,case_red='',case=''):
	try		: QUALITY_METHODS
	except NameError: ERROR('QUALITY_METHODS key missing!')
	else		:
		used=False
		if CONFIG.CL_TYPE =='EXT': CL_PROP='### CLUSTERS USED ###\nfrom external data = '+CONFIG.CL_DATA
		else			 : CL_PROP=open(CONFIG.CLUSTER_INFO+case,'r').read()

		prt(CONFIG.QUALITY_INFO+case,CL_PROP,'w')
		prt(CONFIG.QUALITY_INFO+case,'### QUALITIES USED ###','a')
		prt(CONFIG.QUALITY_INFO+case,'INPUT_DATA = '+CONFIG.CL_DATA,'a')
		for METHOD in QUALITY_METHODS:
			print_info(METHOD,CONFIG.dict_clust,'','',CONFIG.QUALITY_INFO+case,'a')
		prt(CONFIG.QUALITY_INFO+case,'\n\t-outputs:','a')
		Qvec=[]
		for METHOD in QUALITY_METHODS:
			if METHOD!='':
				q=check_quality(CONFIG,METHOD,case_red,case)
				print('\t\tquality from',METHOD,':',q,'\n')
				prt(CONFIG.QUALITY_INFO+case,'quality from '+METHOD+' = '+str(q),'a')
				used=True
				Qvec.append(q)
		PRT_FMSG('QUALITY results printed to','QUALITY results not printed',CONFIG.QUALITY_INFO+case)
		if used: return Qvec
		else:
			print('\t\t<no quality checks>')
			prt(CONFIG.QUALITY_INFO+case,'\t<no quality checks>')

#############################
#### PLOTTIING PART	 ####
#############################
def plotC(CONFIG):
	from plotting.plot import plot_data
	PLOT_NAME=plot_name(CONFIG.RED_TYPE,CONFIG.CL_TYPE,CONFIG.dict_red,CONFIG.dict_clust,PLOT_EXT)
	os.system('mkdir -p plots')
	plot_data(READ(CONFIG.RED_DATA,CONFIG.MASK).T,READ(CONFIG.CL_DATA).T,READ(CONFIG.LAB_DATA),PLOT_NAME)
	if CONFIG.CL_TYPE =='EXT': CL_PROP='### CLUSTERS USED ###\nfrom external data = '+CONFIG.CL_DATA
	else			 : CL_PROP=open(CONFIG.CLUSTER_INFO,'r').read()
	prt(CONFIG.PLOT_INFO,CL_PROP,'w')
	PRT_FMSG('PLOT generated at','PLOT file not generated',PLOT_NAME)
def plot_specC(CONFIG):
	from plotting.plot_specs import plot_spectra
	PLOT_NAME=plot_name(CONFIG.RED_TYPE,CONFIG.CL_TYPE,CONFIG.dict_red,CONFIG.dict_clust,'_specs'+PLOT_SPEC_EXT)
	os.system('mkdir -p plots')
	plot_spectra(READ(CONFIG.SPEC_DATA,CONFIG.MASK),READ(CONFIG.LAB_DATA),PLOT_NAME)
	if CONFIG.CL_TYPE =='EXT': CL_PROP='### CLUSTERS USED ###\nfrom external data = '+CONFIG.CL_DATA
	else			 : CL_PROP=open(CONFIG.CLUSTER_INFO,'r').read()
	prt(CONFIG.PLOTSPEC_INFO,CL_PROP,'w')
	PRT_FMSG('SPECS PLOT generated at','SPECS PLOT not generated',PLOT_NAME)
