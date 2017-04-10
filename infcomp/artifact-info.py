#
# Oxford Inference Compilation
# https://arxiv.org/abs/1610.09900
#
# Tuan-Anh Le, Atilim Gunes Baydin
# University of Oxford
# May 2016 -- March 2017
#

import infcomp.util
import torch
import argparse
from termcolor import colored
import datetime
import sys
import os
from pprint import pformat
import matplotlib.pyplot as plt
import numpy as np
from itertools import zip_longest
import csv

parser = argparse.ArgumentParser(description='Oxford Inference Compilation ' + util.version + ' (Artifact Info)', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-v', '--version', help='show version information', action='store_true')
parser.add_argument('--dir', help='directory to save artifacts and logs', default='.')
parser.add_argument('--latest', help='show the latest artifact', action='store_true')
parser.add_argument('--nth', help='show the nth artifact (-1: last)', type=int)
parser.add_argument('--structure', help='show extra information about artifact structure', action='store_true')
parser.add_argument('--savePlot', help='save loss plot to file (supported formats: eps, jpg, png, pdf, svg, tif)', type=str)
parser.add_argument('--showPlot', help='show the loss plot in screen', action='store_true')
parser.add_argument('--saveHist', help='save the training and validation loss history (csv)', type=str)
opt = parser.parse_args()

if opt.version:
    print(infcomp.__version__)
    quit()

if not opt.latest and opt.nth is None:
    parser.print_help()
    quit()

time_stamp = util.get_time_stamp()
util.init_logger('{0}/{1}'.format(opt.dir, 'artifact-info-log' + time_stamp))

util.log_print()
util.log_print(colored('█ Oxford Inference Compilation ' + util.version, 'blue', attrs=['bold']))
util.log_print()
util.log_print('Artifact Info')
util.log_print()
util.log_print('Started ' +  str(datetime.datetime.now()))
util.log_print()
util.log_print('Running on PyTorch ' + torch.__version__)
util.log_print()
util.log_print('Command line arguments:')
util.log_print(' '.join(sys.argv[1:]))

util.log_print()
util.log_print(colored('█ Artifact info configuration', 'blue', attrs=['bold']))
util.log_print()
util.log_print(pformat(vars(opt)))
util.log_print()

if opt.latest:
    opt.nth = -1
file_name = util.file_starting_with('{0}/{1}'.format(opt.dir, 'compile-artifact'), opt.nth)
artifact = torch.load(file_name)
file_size = '{:,}'.format(os.path.getsize(file_name))

util.log_print()
util.log_print(colored('█ Artifact', 'blue', attrs=['bold']))
util.log_print()

util.check_versions(artifact)

util.log_print('File name             : {0}'.format(file_name))
util.log_print('File size (Bytes)     : {0}'.format(file_size))
util.log_print(artifact.get_info())

if opt.structure:
    util.log_print()
    util.log_print(colored('█ Artifact structure', 'blue', attrs=['bold']))
    util.log_print()

    util.log_print(artifact.get_structure())

if opt.showPlot or opt.savePlot:
    util.log_print()
    util.log_print(colored('█ Loss plot', 'blue', attrs=['bold']))
    util.log_print()
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(artifact.train_history_trace, artifact.train_history_loss, label='Training')
    ax.plot(artifact.valid_history_trace, artifact.valid_history_loss, label='Validation')
    ax.legend()
    plt.xlabel('Traces')
    plt.ylabel('Loss')
    plt.grid()
    fig.tight_layout()
    if opt.showPlot:
        util.log_print('Plotting loss to screen')
        plt.show()
    if not opt.savePlot is None:
        util.log_print('Saving loss plot to file: ' + opt.savePlot)
        fig.savefig(opt.savePlot)

if not opt.saveHist is None:
    util.log_print('Saving training and validation loss history to file: ' + opt.saveHist)
    with open(opt.saveHist, 'w') as f:
        data = [artifact.train_history_trace, artifact.train_history_loss, artifact.valid_history_trace, artifact.valid_history_loss]
        writer = csv.writer(f)
        writer.writerow(['train_trace', 'train_loss', 'valid_trace', 'valid_loss'])
        for values in zip_longest(*data):
            writer.writerow(values)
