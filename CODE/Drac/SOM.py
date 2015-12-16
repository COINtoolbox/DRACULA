from __future__ import print_function
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(''))

import config_som
reload(config_som)
from config_som import *

import management.update_dict
reload(management.update_dict)
from management.update_dict import update_dict

from management.name_files import create_name,plot_name
from management.info_work import prt,print_info,read_info

from management.params_som import dict_som
update_dict(dict_som)

def ERROR(message):
	out='### **ERROR** - '+message+' ####'
	line='\n'
	for x in out: line+='#'
	line+='\n'
	print(line+out+line)
	exit()
def READ(NAME):
	if os.path.isfile(NAME):
		try: MASK_DATA
		except NameError: return np.loadtxt(NAME)
		else		: return np.loadtxt(NAME)[np.loadtxt(MASK_DATA)==1]
	else: ERROR('file '+NAME+' does not exist!')

import som_module.run_som
import som_module.plot_som
os.system('mkdir -p som_res/')
def run_som():
	som_module.run_som.func(READ(ORG_DATA),dict_som)
def plot_som():
	try:
		SPECTRAL_DATA_EXTERNAL
	except NameError: SPEC_DATA=ORG_DATA
	else		: SPEC_DATA=SPECTRAL_DATA_EXTERNAL;print('\t- using external spectral for plotting')
	som_module.plot_som.func(READ(SPEC_DATA))
