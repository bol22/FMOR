# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:14:50 2018

@author: liub725
"""

# read the Voltage amd Current Value for the given buses to be preserved
import csv
#import cmath


#def get_VI3P(model_name,node_list,VIdatafile)

# read all the value in the voltage dumpfile.
with open("output_voltage.csv",'r') as f, open("output_voltage1.csv",'w') as f1:
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

# get the segment node from the nodelist file
segmentkeys=['i_node','f_node','phase','phase_name']
with open ('node_list_R5-12-47-1.csv','r') as nodefile:            
    nodeinfo=nodefile.read().splitlines()
    nodeinfolist=[]
    for n in range(len(nodeinfo)):
        nodeinfolist.append(nodeinfo[n].split(','))
# make a dict that contains the segment information
nodelist=[]
for k in range(len(nodeinfolist)):
    nodelist.append(dict(zip(segmentkeys,nodeinfolist[k])))

# read the voltage according to segment node
Via=[]
Vib=[] 
Vic=[]
Vfa=[]
Vfb=[] 
Vfc=[]
for n in range(len(nodelist)):
#    temp_node='R5-12-47-1_'+nodelist[n]['i_node']
    Via.append(complex(float(Va['R5-12-47-1_node_'+nodelist[n]['i_node']]),float(Vaimg['R5-12-47-1_node_'+nodelist[n]['i_node']])))
    Vib.append(complex(float(Vb['R5-12-47-1_node_'+nodelist[n]['i_node']]),float(Vbimg['R5-12-47-1_node_'+nodelist[n]['i_node']])))
    Vic.append(complex(float(Vc['R5-12-47-1_node_'+nodelist[n]['i_node']]),float(Vcimg['R5-12-47-1_node_'+nodelist[n]['i_node']])))
    Vfa.append(complex(float(Va['R5-12-47-1_node_'+nodelist[n]['f_node']]),float(Vaimg['R5-12-47-1_node_'+nodelist[n]['f_node']]))) 
    Vfb.append(complex(float(Vb['R5-12-47-1_node_'+nodelist[n]['f_node']]),float(Vbimg['R5-12-47-1_node_'+nodelist[n]['f_node']])))
    Vfc.append(complex(float(Vc['R5-12-47-1_node_'+nodelist[n]['f_node']]),float(Vcimg['R5-12-47-1_node_'+nodelist[n]['f_node']])))
    
#Va=[row[3] for row in r][2:]

    


