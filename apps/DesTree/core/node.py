#!/usr/bin/python
#-*-coding: utf8-*-

"""
定义决策树中的节点结构
"""


class Node(object):

    def __init__(self, dataset=None, parent=None):
        """
        dataset 节点i的训练集
        attrset 节点i的属性集
        """
        self.dataset = dataset
        self.attribute = None
        self.parent = None  # 节点i的父节点
        self.children = {}  # 节点i的孩子节点
        self.label = None  # 节点所属的标记
        