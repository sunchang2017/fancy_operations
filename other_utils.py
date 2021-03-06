# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :fancy_operations
# @File     :other_utils
# @Date     :2020/12/30 下午8:17
# @Author   :SYJ
# @Email    :JuZiSYJ@gmail.com
# @Software :PyCharm
-------------------------------------------------
"""
import cv2
import numpy as np
from PIL import Image
import math
import torch
import os
from io import BytesIO
from torch import nn
import torch.nn.functional as F
from matplotlib import pyplot as plt
import threading
import yaml

def mul_thread():
    def mk_data(dir_list, time, q_list):
        '''
        could be a function outside mul_thread()
        :param dir_list:
        :param time:
        :param q_list:
        :return:
        '''
        pass

    T = []
    Dir_list = os.listdir('ILSVRC2012_img_val')
    q_list = [10,20,30,40,50]
    t1 = threading.Thread(target=mk_data, kwargs={'dir_list':Dir_list, 'time':1, 'q_list':q_list}) # given multual param
    t2 = threading.Thread(target=mk_data, kwargs={'dir_list':Dir_list, 'time':2, 'q_list':q_list})
    t3 = threading.Thread(target=mk_data, kwargs={'dir_list':Dir_list, 'time':3, 'q_list':q_list})
    t4 = threading.Thread(target=mk_data, kwargs={'dir_list':Dir_list, 'time':4, 'q_list':q_list})
    t5 = threading.Thread(target=mk_data, kwargs={'dir_list':Dir_list, 'time':5, 'q_list':q_list})

    T.append(t1)
    T.append(t2)
    T.append(t3)
    T.append(t4)
    T.append(t5)
    for t in T:
        t.setDaemon(True)
        t.start()
    for t in T:
        ## https://www.cnblogs.com/my8100/p/7366567.html
        t.join()



def draw_and_save():
    fig = plt.figure(dpi=600)
    plt.axis('off')
    img = np.zeros((224,224,3))

    plt.imshow(img, cmap='jet')

    save_path = os.path.join('xx',  '.png')

    plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
    plt.cla()
    plt.close()
    
def calcul_mac():
    pass
    ## https://github.com/zhijian-liu/torchprofile    accurate
    ## https://github.com/Lyken17/pytorch-OpCounter

def parse_yaml():
    '''
    a typical yaml:
    #### general settings

name: 01_IRN+_DB_x4_scratch_DIV2K
use_tb_logger: true
model: IRN+
distortion: sr
scale: 4
gpu_ids: [0]
lr: !!float 1e-4
is: ~

#### datasets

datasets:
  train:
    name: DIV2K
    mode: LQGT
    dataroot_GT: /home/forrest/Downloads/data/syj/DIV2K/DIV2K_train_HR_sub/ # path to training HR images
    dataroot_LQ: ~ # path to training reference LR images, not necessary, if not provided, LR images will be generated in dataloader

    use_shuffle: true
    n_workers: 4  # per GPU
    batch_size: 8
    GT_size: 144
    use_flip: true
    use_rot: true
    color: RGB

  val:
    name: val_DIV2K
    mode: LQGT

    :return:
    '''
    path = 'train_IRN+_x4.yml'
    # opt = yaml.load(path)
    with open(path, mode='r') as f:
        opt = yaml.load(f, Loader=yaml.Loader)
    print(opt)
    # print(opt.)
    '''{'name': '01_IRN+_DB_x4_scratch_DIV2K', 'use_tb_logger': True, 'model': 'IRN+', \
    'distortion': 'sr', 'scale': 4, 'gpu_ids': [0], 'lr":1e-4, 'is': None, datasets': {'train': {'na
    '''

    for phase, dataset in opt['datasets'].items():
        if dataset.get('dataroot_GT', None) is not None:
            pass

    # pass


if __name__ == '__main__':
    pass
