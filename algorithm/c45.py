from math import e, log
import numpy as np


class c45:
    def gain_ratio(self, attribute, data):
        total_entropy = self.entropy(data)
        attribute_entropy, split_info = self.attribute_entropy_and_split_info(attribute, data)
        gain = total_entropy - attribute_entropy
        if split_info == 0:
            return 0
        return gain / split_info

    def conditional_entropyXY(self, X, Y):
        conj_freq = {}
        prev_freq = {}
        for (x_index, x_val), (y_index, y_val) in zip(X.items(), Y.items()):
            if (x_val, y_val) in conj_freq:
                conj_freq[(x_val, y_val)] += 1
            else:
                conj_freq[(x_val, y_val)] = 1
            if x_val in prev_freq:
                prev_freq[x_val] += 1
            else:
                prev_freq[x_val] = 1
        omega = sum(conj_freq.values())
        return -sum([conj_freq[(x, y)] / omega * log(conj_freq[(x, y)] / prev_freq[x], 2) for (x, y) in conj_freq])


    # def entropy(y, base=None):
    #     value, counts = np.unique(y, return_counts=True)
    #     norm_counts = counts / counts.sum()
    #     base = e if base is None else base
    #     return -(norm_counts * np.log(norm_counts)/np.log(base)).sum()

    def entropy(self, y, base=None):
        if not y:  # Sprawdzenie, czy lista jest pusta
            return 0
        value, counts = np.unique(y, return_counts=True)
        norm_counts = counts / (counts.sum() + np.finfo(float).eps)  # Dodanie eps do mianownika
        base = e if base is None else base
        return -(norm_counts * np.log(norm_counts + np.finfo(float).eps) / np.log(base)).sum()  # Dodanie eps do logarytmu

class Node:
	def __init__(self,isLeaf, label, threshold):
		self.label = label
		self.threshold = threshold
		self.isLeaf = isLeaf
		self.children = []
          

          
