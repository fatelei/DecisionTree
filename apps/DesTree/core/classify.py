#!/usr/bin/python
#-*-coding: utf8-*-


def classify(tree, path):
    """
    根据path进行分类
    """
    if tree == None:
        return None
    if tree.label != None:
        return tree.label
    return classify(tree.children[path[tree.attribute]], path)
