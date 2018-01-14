import pandas as pd
import numpy as np

F1 = pd.read_csv('origin_data/itsdb/switch/N15151F1-10:00:00~10:15:00', dtype=np.str).values[:, 1]
F2 = pd.read_csv('origin_data/itsdb/switch/N15151F2-10:00:00~10:15:00', dtype=np.str).values[:, 1]
F3 = pd.read_csv('origin_data/itsdb/switch/N15151F3-10:00:00~10:15:00', dtype=np.str).values[:, 1]
R1 = pd.read_csv('origin_data/itsdb/switch/N15151R1-10:00:00~10:15:00', dtype=np.str).values[:, 1]
V1 = pd.read_csv('origin_data/itsdb/switch/N15151V1-10:00:00~10:15:00', dtype=np.str).values[:, 1]
V2 = pd.read_csv('origin_data/itsdb/switch/N15151V2-10:00:00~10:15:00', dtype=np.str).values[:, 1]
V3 = pd.read_csv('origin_data/itsdb/switch/N15151V3-10:00:00~10:15:00', dtype=np.str).values[:, 1]

"""
96
"""


def flow(detector,key='01'):
    return ''.join(detector).count(key)
