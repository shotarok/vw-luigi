#!/usr/bin/env python

import numpy as np
from sklearn.metrics import average_precision_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import log_loss


def vweval(test_path, pred_path, result_path):
    with open(test_path) as fp:
        labels = np.array([1 if line.split()[0] == '1' else 0 for line in fp])
    probs = np.loadtxt(pred_path)[:, 0]
    with open(result_path, 'w') as fp:
        print("AUROC:{0:.5f}".format(roc_auc_score(labels, probs)),
              file=fp, end=" ")
        print("AUPR:{0:.5f}".format(average_precision_score(labels, probs)),
              file=fp, end=" ")
        print("LOGLOSS:{0:.5f}".format(log_loss(labels, probs)), file=fp)
