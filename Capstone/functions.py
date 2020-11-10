#get info
import pandas as pd
import numpy as np
from collections import Counter
import math
from sklearn.metrics import f1_score, precision_recall_curve, classification_report, auc, accuracy_score, roc_auc_score, confusion_matrix, mean_squared_error, roc_curve
import matplotlib.pyplot as plt

def get_details(data):
    skew= data.skew()
#     corr = data.corr()[target]

    nulls = data.apply(lambda x: x.isnull().sum())
    nulls_perc = data.apply(lambda x: x.isnull().sum()/data.shape[0]*100)
    unique = data.apply(lambda x: [x.unique()])

    details = pd.concat([skew, nulls, nulls_perc, unique], axis=1, sort=False)
    details.columns = ['skew', 'nulls', 'nulls_perc', 'unique']
    
    return details

def add(a, b):
    return a + b

def deciles(data, decile):
    decile = 10/100
    percent = np.arange(0,1+decile,decile)
    return data.quantile(q = percent)

def purity(L, metric='gini'):
    total = len(L)
    freq = map(lambda x: float(x) / total, list(Counter(L).values()))
    if metric == 'gini':
        scores = map(lambda x: x * (1 - x), freq)
    elif metric == 'entropy':
        scores = map(lambda x: -x * math.log(x, 2), freq)
    return scores

def gini_coeff(auc):
    return 2*auc - 1

def get_report(actual, predicted):
    
    print(confusion_matrix(actual, predicted))
    print(classification_report(actual, predicted))

def ROC_graph(actual, predicted, probability):
    fpr, tpr, thresholds = roc_curve(actual, probability)
    precision, recall, _ = precision_recall_curve(actual, probability)

    f1 = f1_score(actual, predicted)
    roc_area = auc(fpr, tpr)
    pr_area = auc(recall, precision)

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))
    lw = 2
    ax1.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_area)
    ax1.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    ax1.set_xlim([0.0, 1.0])
    ax1.set_ylim([0.0, 1.05])
    ax1.set_xlabel('False Positive Rate')
    ax1.set_ylabel('True Positive Rate')
    ax1.set_title('Receiver operating characteristic')
    ax1.legend(loc="lower right")
    
    ax2.plot(recall, precision, color='darkorange',
             lw=lw, label='Precision recall curve (area = %0.2f)' % pr_area)
    no_skill = len(actual[actual==1]) / len(actual)
    ax2.plot([0, 1], [no_skill, no_skill], color='navy', lw=lw, linestyle='--')
    ax2.set_xlim([0.0, 1.0])
    ax2.set_ylim([0.0, 1.05])
    ax2.set_xlabel('Recall')
    ax2.set_ylabel('Precision')
    ax2.set_title('Precision Recall Curve')
    ax2.legend(loc="lower right")
    
    print("F1 is %.2f" %(f1))
    print("ROC gini is %.2f" %(gini_coeff(roc_area)))
    print("Precision Recall gini is %.2f" %(gini_coeff(pr_area)))
    plt.show()
    
def class_overlap(x1, x2):
    plt.hist(x1, color='g', label='0', alpha=0.5)
    plt.hist(x2, color='b', label='1', alpha=0.5)
    plt.xlabel('Predictions')
    plt.ylabel('Frequency')
    plt.title('Class overlap')
    plt.legend()
    plt.show()