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

import som_module.run_som
import som_module.plot_som
def run_som():
	som_module.run_som.func(dict_som)
def plot_som():
	som_module.plot_som.func(dict_som)
