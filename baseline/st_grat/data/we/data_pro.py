# -- coding: utf-8 --
import pandas as pd
import csv
import numpy as np

def triple_adjacent(adjacent_file=None, road_segments=108, target_file='adjacent.txt'):
    '''
    :return: [N*N, 3], for example [i, j, distance]
    '''
    adjacent=pd.read_csv(adjacent_file, encoding='utf-8').values

    triple_adjacent = np.zeros(shape=[road_segments**2, 3])
    full_adjacent = np.zeros(shape=[road_segments, road_segments])
    for i in range(road_segments):
        for j in range(road_segments):
            triple_adjacent[i * road_segments + j] = np.array([i, j, 0])
    for pair in adjacent:
        triple_adjacent[pair[0]*road_segments+pair[1]] = np.array([pair[0], pair[1], 1])
        full_adjacent[pair[0],pair[1]]=1

    np.savez('adjacent.npz', data=full_adjacent)
    np.savetxt(target_file, triple_adjacent, '%d')

def train_npz(source_file=None, site_num=108, target_file='train.npz'):
    '''
    :param source_file:
    :param site_num:
    :param target_file:
    :return:
    '''
    data = pd.read_csv(source_file, encoding='utf-8').values
    print(data.shape)
    data = np.reshape(data, [-1, site_num, data.shape[-1]])
    print(data.shape)
    np.savez(target_file, data=data)

if __name__=='__main__':
    print('hello')
    # 生成三元组形式的邻接矩阵
    # triple_adjacent(adjacent_file='adjacent.csv')

    # 训练集生成为.npz格式
    train_npz(source_file='train.csv')

    print('finished')