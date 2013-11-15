#!/usr/bin/python
#-*-coding: utf8-*-

from math import log


def entropy(probabilities):
    """
    计算信息熵
    """
    log2 = lambda x: log(x) / log(2)
    rst = 0.0

    for p in probabilities:
        rst = rst - (p * log2(p))
    return rst


def info_gain(HD, HDA):
    """
    获取信息增益
    HD 划分D的经验熵
    HDA 在属性A下划分D的信息熵
    """
    gain = HD - HDA
    return gain


def calc_experence_entropy(dataset):
    """
    计算当前划分下的经验熵
    dataset 当前划分下的训练集
    """
    total = len(dataset)
    classify = {}
    probabilities = []

    for di in dataset:
        if di[-1] not in classify:
            classify[di[-1]] = 0.0
        classify[di[-1]] += 1.0

    for k, v in classify.iteritems():
        p = v / total
        probabilities.append(p)

    res = entropy(probabilities)
    return res


def calc_condition_entropy(dataset, attribute):
    """
    计算当前属性下的对于当前划分的条件熵
    dataset 训练集
    attribute 属性id
    """
    total = len(dataset)
    attri_feature = {}  # 当前属性下么个特征的数量
    attri_feature_label = {}  # 当前属性下每个特征所属的分类
    res = 0.0

    for d in dataset:
        if d[attribute] not in attri_feature:
            attri_feature[d[attribute]] = 0.0
            attri_feature_label[d[attribute]] = {}
        attri_feature[d[attribute]] += 1.0

        if d[-1] not in attri_feature_label[d[attribute]]:
            attri_feature_label[d[attribute]][d[-1]] = 0.0
        attri_feature_label[d[attribute]][d[-1]] += 1.0

    for k, v in attri_feature.iteritems():
        pk = v / total
        probabilities = []
        lables = attri_feature_label[k]

        for i, j in lables.iteritems():
            p = j / v
            probabilities.append(p)

        tmp_entropy = entropy(probabilities)
        res = res + pk * tmp_entropy
    return res
