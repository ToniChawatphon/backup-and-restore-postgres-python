import os


ROOT_LIB    = os.path.dirname(os.path.abspath(__file__))
ROOT        = ROOT_LIB.replace('lib', '')
CREDENTIALS = ROOT + '/config/postgres.yaml'
