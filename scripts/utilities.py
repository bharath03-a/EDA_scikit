import numpy as np
import pandas as pd
import os

def convert_cpu(cpu):
    if 'i3' in cpu:
        return 'i3'
    elif 'i5'in cpu:
        return 'i5'
    elif 'i7' in cpu:
        return 'i7'
    else:
        return 'others'
    
def get_storage_type(storage):
    if 'SSD' and 'HDD' in storage:
        return 'SSD+'
    elif 'SSD' in storage:
        return 'SSD'
    elif 'HDD' in storage:
        return 'HDD'
    elif 'Flash Storage' in storage:
        return 'Flash Storage'
    elif 'Hybrid' in storage:
        return 'Hybrid'
    
def get_gpu(gpu):
    if 'Nvidia' in gpu:
        return 'Nvidia'
    elif 'AMD' in gpu:
        return 'AMD'
    elif 'Intel' in gpu:
        return 'Intel'
    else:
        return 'others'