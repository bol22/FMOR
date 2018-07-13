# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:09:37 2018

@author: liub725
"""

import csv
#import cmath


def getI(model_name, linelistfile, I_datafile):


    with open(I_datafile,'r') as f, open("output_current1.csv",'w') as f1:
        next(f) # skip header line
        for line in f:
            f1.write(line)
    f2=open('output_current1.csv', 'r')
    r=csv.DictReader(f2)
    link=[row['link_name'] for row in r]
    f2=open('output_current1.csv', 'r')
    r1=csv.DictReader(f2)
    Ia=dict(zip(link,[row['currA_real'] for row in r1]))
    f2=open('output_current1.csv', 'r')
    r2=csv.DictReader(f2)
    Ib=dict(zip(link,[row['currB_real'] for row in r2]))
    f2=open('output_current1.csv', 'r')
    r3=csv.DictReader(f2)
    Ic=dict(zip(link,[row['currC_real'] for row in r3]))
    f2=open('output_current1.csv', 'r')
    r4=csv.DictReader(f2)
    Iaimg=dict(zip(link,[row['currA_imag'] for row in r4]))
    f2=open('output_current1.csv', 'r')
    r5=csv.DictReader(f2)
    Ibimg=dict(zip(link,[row['currB_imag'] for row in r5]))
    f2=open('output_current1.csv', 'r')
    r6=csv.DictReader(f2)
    Icimg=dict(zip(link,[row['currC_imag'] for row in r6]))
    f2.close()
    
    
    segmentkeys=['i_branch','f_branch','phase','phase_name']
    with open (linelistfile,'r') as linefile:            
        lineinfo=linefile.read().splitlines()
        lineinfolist=[]
        for n in range(len(lineinfo)):
            lineinfolist.append(lineinfo[n].split(','))
    global linelist
    linelist=[]
    for k in range(len(lineinfolist)):
        linelist.append(dict(zip(segmentkeys,lineinfolist[k])))
    
    global Iia
    global Iib
    global Iic
    global Ifa
    global Ifb
    global Ifc
    Iia=[]
    Iib=[] 
    Iic=[]
    Ifa=[]
    Ifb=[] 
    Ifc=[]
    for n in range(len(linelist)):
        Iia.append(complex(float(Ia[linelist[n]['i_branch']]),float(Iaimg[linelist[n]['i_branch']])))
        Iib.append(complex(float(Ib[linelist[n]['i_branch']]),float(Ibimg[linelist[n]['i_branch']])))
        Iic.append(complex(float(Ic[linelist[n]['i_branch']]),float(Icimg[linelist[n]['i_branch']])))
        Ifa.append(complex(float(Ia[linelist[n]['f_branch']]),float(Iaimg[linelist[n]['f_branch']]))) 
        Ifb.append(complex(float(Ib[linelist[n]['f_branch']]),float(Ibimg[linelist[n]['f_branch']])))
        Ifc.append(complex(float(Ic[linelist[n]['f_branch']]),float(Icimg[linelist[n]['f_branch']])))

def _tests():
    
	getI('R5-12-47-1','line_list_R5-12-47-1_new.csv','output_current.csv')

if __name__ == '__main__':
	_tests()