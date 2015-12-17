from __future__ import print_function
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(''))

from main_funcs import *

CONFIG=set_prop()


def reduc()	: reducC		(CONFIG)
def cluster()	: clusterC		(CONFIG)
def do_quality(): do_qualityC		(CONFIG)
def plot()	: plotC			(CONFIG)
def plot_spec()	: plot_specC		(CONFIG)
