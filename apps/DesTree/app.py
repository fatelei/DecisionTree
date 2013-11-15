#!/usr/bin/python
#-*-coding: utf8-*-

import argparse
import os
import json

from DesTree.core.tree import build_decision_tree
from DesTree.core.classify import classify


def run():
    parser = argparse.ArgumentParser(description='decision tree')
    parser.add_argument('--train_file', metavar='train_file', type=str,
                        dest='train_file', required=True, help=u'包含训练集的文件')
    parser.add_argument('--test_file', metavar='test_file', type=str,
                        dest='test_file', required=True, help=u'包含测试集的文件')

    args = parser.parse_args()

    if not os.path.isfile(args.train_file):
        parser.print_help()
        exit(0)

    if not os.path.isfile(args.test_file):
        parser.print_help()
        exit(0)

    dataset = []
    attributes = []
    with open(args.train_file) as f:
        data = f.read()
        dataset = json.loads(data)

    attributes = [i for i in range(len(dataset[0]) - 1)]

    testset = []
    with open(args.test_file) as f:
        data = f.read()
        testset = json.loads(data)

    tree = build_decision_tree(dataset, attributes)
    label = classify(tree, testset)
    print label
