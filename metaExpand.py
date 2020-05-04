#!/usr/bin/env python3

# meta materials structure expanding tool
# 05/04/2020 Bingyin Hu

import numpy as np

class metaExpand():
    def __init__(self, struc, multiplier, symshort= True):
        self.multiplier = multiplier
        if symshort:
            self.struc = self.symToFullStruc(struc)
        else:
            assert np.sqrt(len(np.ndarray.flatten(struc)))**2 == len(np.ndarray.flatten(struc))
            self.struc = struc # an numpy array
        self.size = int(np.sqrt(len(np.ndarray.flatten(struc)))*self.multiplier) # size of the expanded array
        self.big_struc = np.zeros((self.size,self.size))
        self.__expand__()

    # TODO (input a short version of the structure, return the full structure array)
    def symToFullStruc(self, struc):
        return

    # expanding function, external
    def expand(self, struc, multiplier):
        size = int(np.sqrt(len(struc))*multiplier)
        big_struc = np.zeros((size,size))
        for r in range(multiplier):
            for c in range(multiplier):
                big_struc[r::multiplier,c::multiplier] = struc
        return big_struc

    # expanding function, internal
    def __expand__(self):
        for r in range(self.multiplier):
            for c in range(self.multiplier):
                self.big_struc[r::self.multiplier,c::self.multiplier] = self.struc

    # output function
    def getStruc(self):
        return self.big_struc

    # output flattened
    def getFlatStruc(self):
        return np.ndarray.flatten(self.big_struc)