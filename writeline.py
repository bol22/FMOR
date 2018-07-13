# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:30:26 2018

@author: liub725
"""
import numpy as np
# write gridlab-d model
def CreateLineConfig_3phase(seg_number,glmfile):
    f=open(glmfile,'a')
    f.write('object line_configuration {\n')
    f.write('    name line_seg_'+str(seg_number)+';\n')  
    f.write('    z11 '+np.array2string(Z[seg_number][0][0])+';\n') 
    f.write('    z12 '+np.array2string(Z[seg_number][0][1])+';\n') 
    f.write('    z13 '+np.array2string(Z[seg_number][0][2])+';\n') 
    f.write('    z21 '+np.array2string(Z[seg_number][1][0])+';\n') 
    f.write('    z22 '+np.array2string(Z[seg_number][1][1])+';\n') 
    f.write('    z23 '+np.array2string(Z[seg_number][1][2])+';\n') 
    f.write('    z31 '+np.array2string(Z[seg_number][2][0])+';\n') 
    f.write('    z32 '+np.array2string(Z[seg_number][2][1])+';\n') 
    f.write('    z33 '+np.array2string(Z[seg_number][2][2])+';\n') 
    f.write('    }\n')
    return


def _tests():
    for n in range(10):
        CreateLineConfig_3phase(n,'abc.csv')

if __name__ == '__main__':
	_tests()