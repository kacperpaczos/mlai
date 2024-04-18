from math import e, log
import numpy as np
from icecream import ic


class c45:
    def gain_ratio(self, attribute, data):
        total_entropy = self.entropy(data)
        attribute_entropy, split_info = self.attribute_entropy_and_split_info(attribute, data)
        gain = total_entropy - attribute_entropy
        if split_info == 0:
            return 0
        return gain / split_info

    def conditional_entropyXY(self, X, Y, base=2, axis=0):
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
        return -sum([conj_freq[(x, y)] / omega * log(conj_freq[(x, y)] / prev_freq[x], base) for (x, y) in conj_freq])

    def special_entr(self, pk, axis=0):
        import numpy as np
        pk = np.asarray(pk)
        with np.errstate(divide='ignore', invalid='ignore'):
            result = np.where(pk > 0, -pk * np.log(pk), 0)
        return np.sum(result, axis=axis)

    def relative_entropy(self, pk, qk=None, base=None, axis=0):
        import numpy as np

        if qk is None:
            raise ValueError("qk (second distribution) must be provided")

        pk = np.asarray(pk, dtype=np.float64)
        qk = np.asarray(qk, dtype=np.float64)

        if np.any(pk < 0) or np.any(qk < 0):
            raise ValueError("Probability distributions must not be negative")

        pk = pk / np.sum(pk, axis=axis, keepdims=True)
        qk = qk / np.sum(qk, axis=axis, keepdims=True)

        with np.errstate(divide='ignore', invalid='ignore'):
            rel_entr = np.where(pk != 0, pk * np.log(pk / qk), 0)

        if base is not None:
            rel_entr /= np.log(base)

        return np.sum(rel_entr, axis=axis)
    
    def entropy(self, pk, qk=None, base=None, axis=0):
        if base is not None and base <= 0:
            raise ValueError("`base` must be a positive number or `None`.")

        pk = np.asarray(pk)
        with np.errstate(invalid='ignore'):
            pk = 1.0*pk / np.sum(pk, axis=axis, keepdims=True)
        if qk is None:
            vec = self.special_entr(pk)
        else:
            qk = np.asarray(qk)
            pk, qk = np.broadcast_arrays(pk, qk)
            sum_kwargs = dict()
            qk = 1.0*qk / np.sum(qk, **sum_kwargs)
            vec = self.relative_entropy(pk, qk)
        S = np.sum(vec, axis=axis)
        if base is not None:
            S /= np.log(base)
        return S

class Node:
	def __init__(self,isLeaf, label, threshold):
		self.label = label
		self.threshold = threshold
		self.isLeaf = isLeaf
		self.children = []
          

          
