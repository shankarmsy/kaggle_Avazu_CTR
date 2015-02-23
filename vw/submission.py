from datetime import datetime
from csv import DictReader
from math import exp, log, sqrt
import os, csv

# TL; DR, the main training process starts on line: 250,
# you may want to start reading the code from there


##############################################################################
# parameters #################################################################
##############################################################################

# A, paths
test = 'test.csv'                 # path to testing file
# trainvw = 'train.vw'  # path of output file for vowpal wabbit
# testvw = 'test.vw'  # path of output file for vowpal wabbit

pred = 'vwpredftrl_holdout100.dat'  # path of output file for vowpal wabbit

def data(path):
    ''' GENERATOR: Apply hash-trick to the original csv row
                   and for simplicity, we one-hot-encode everything

        INPUT:
            path: path to training or testing file
            D: the max index that we can hash to

        YIELDS:
            ID: id of the instance, mainly useless
            x: a list of hashed and one-hot-encoded 'indices'
               we only need the index since all values are either 0 or 1
            y: y = 1 if we have a click, else we have y = 0
    '''

    for t, row in enumerate(DictReader(open(path))):
        yield t, row['id']


##############################################################################
# start training #############################################################
##############################################################################

start = datetime.now()
o_f=open('vwpredftrl_holdout100.csv','wb')
writer=csv.writer(o_f)
writer.writerow(['id','click'])
predfile=open(pred,'r')

for t, Id in data(test):  # data is a generator
    writer.writerow([Id, predfile.readline().split('\n')[-2]])

print "%d rows written successfully" %t
