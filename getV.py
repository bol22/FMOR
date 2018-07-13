# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 09:43:11 2018

@author: liub725
"""

# read the Voltage amd Current Value for the given buses to be preserved
import csv
#import cmath

def getV(model_name, nodelistfile, V_datafile):

    with open(V_datafile,'r') as f, open("output_voltage1.csv",'w') as f1:
        next(f) # skip header line
        for line in f:
            f1.write(line)
    f2=open('output_voltage1.csv', 'r')
    r=csv.DictReader(f2)
    node=[row['node_name'] for row in r]
    f2=open('output_voltage1.csv', 'r')
    r1=csv.DictReader(f2)
    Va=dict(zip(node,[row['voltA_real'] for row in r1]))
    f2=open('output_voltage1.csv', 'r')
    r2=csv.DictReader(f2)
    Vb=dict(zip(node,[row['voltB_real'] for row in r2]))
    f2=open('output_voltage1.csv', 'r')
    r3=csv.DictReader(f2)
    Vc=dict(zip(node,[row['voltC_real'] for row in r3]))
    f2=open('output_voltage1.csv', 'r')
    r4=csv.DictReader(f2)
    Vaimg=dict(zip(node,[row['voltA_imag'] for row in r4]))
    f2=open('output_voltage1.csv', 'r')
    r5=csv.DictReader(f2)
    Vbimg=dict(zip(node,[row['voltA_imag'] for row in r5]))
    f2=open('output_voltage1.csv', 'r')
    r6=csv.DictReader(f2)
    Vcimg=dict(zip(node,[row['voltA_imag'] for row in r6]))
    f2.close()
    # get the segment node from the nodelist file
    segmentkeys=['i_node','f_node','phase','phase_name']
    global nodelist
    with open (nodelistfile,'r') as nodefile:            
        nodeinfo=nodefile.read().splitlines()
        nodeinfolist=[]
        for n in range(len(nodeinfo)):
            nodeinfolist.append(nodeinfo[n].split(','))
    # make a dict that contains the segment information
    nodelist=[]
    for k in range(len(nodeinfolist)):
        nodelist.append(dict(zip(segmentkeys,nodeinfolist[k])))    
    # read the voltage according to segment node
    global Via
    global Vib
    global Vic
    global Vfa
    global Vfb
    global Vfc
    Via=[]
    Vib=[] 
    Vic=[]
    Vfa=[]
    Vfb=[] 
    Vfc=[]
    for n in range(len(nodelist)):
    #    temp_node='R5-12-47-1_'+nodelist[n]['i_node']
        Via.append(complex(float(Va[model_name+'_node_'+nodelist[n]['i_node']]),float(Vaimg[model_name+'_node_'+nodelist[n]['i_node']])))
        Vib.append(complex(float(Vb[model_name+'_node_'+nodelist[n]['i_node']]),float(Vbimg[model_name+'_node_'+nodelist[n]['i_node']])))
        Vic.append(complex(float(Vc[model_name+'_node_'+nodelist[n]['i_node']]),float(Vcimg[model_name+'_node_'+nodelist[n]['i_node']])))
        Vfa.append(complex(float(Va[model_name+'_node_'+nodelist[n]['f_node']]),float(Vaimg[model_name+'_node_'+nodelist[n]['f_node']]))) 
        Vfb.append(complex(float(Vb[model_name+'_node_'+nodelist[n]['f_node']]),float(Vbimg[model_name+'_node_'+nodelist[n]['f_node']])))
        Vfc.append(complex(float(Vc[model_name+'_node_'+nodelist[n]['f_node']]),float(Vcimg[model_name+'_node_'+nodelist[n]['f_node']])))
    
def _tests():
    
	getV('R5-12-47-1','node_list_R5-12-47-1_new.csv','output_voltage.csv')

if __name__ == '__main__':
	_tests()