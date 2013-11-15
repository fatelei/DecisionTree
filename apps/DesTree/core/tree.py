#!/usr/bin/python
#-*-coding: utf8-*-

from .node import Node
from .entropy import *


def get_label(dataset):
    """
    获取分类名
    dataset 训练集
    """
    labels_count = {}
    max_value = -1 << 32
    label = None

    for d in dataset:
        if d[-1] not in labels_count:
            labels_count[d[-1]] = 0
        labels_count[d[-1]] += 1

    for k, v in labels_count.iteritems():
        if max_value < v:
            max_value = v
            label = k
    return label

def split_dataset(dataset, label):
    """
    根据分类划分训练集
    dataset 训练集
    attribute 属性
    """
    subset = {}
    for d in dataset:
        if d[label] not in subset:
            subset[d[label]] = []
        subset[d[label]].append(d)
    return subset

def build_decision_tree(dataset, attributes, threshold=0.0001, tree=None):
    """
    构建决策树
    dataset 训练集
    attributes 属性集
    threshold 阀值
    tree 决策树
    """
    if tree == None:
        tree = Node(dataset, None)

    subset = split_dataset(dataset, -1)
    
    # 当训练集中只有一类c
    if len(subset) <= 1:
        tree.label = subset.keys()[0]
        return tree

    # 当属性集为空
    if len(attributes) == 0:
        tree.label = get_label(dataset)
        return tree

    hd = calc_experence_entropy(dataset)
    max_value = -1 << 32
    attribute_id = None

    for attribute in attributes:
        hda = calc_condition_entropy(dataset, attribute)
        gain = info_gain(hd, hda)

        if max_value < gain:
            max_value = gain
            attribute_id = attribute

    if max_value < threshold:
        tree.label = get_label(dataset)
        return tree

    tree.attribute = attribute_id
    subset = split_dataset(dataset, attribute_id)

    # 溢出使用过的特征
    attributes.remove(attribute_id)

    for key in subset.keys():
        child = Node(subset[key], tree)
        tree.children[key] = child
        build_decision_tree(subset[key], attributes, threshold=0.0001, tree=child)

    return tree

