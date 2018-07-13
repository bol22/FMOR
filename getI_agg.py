# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 13:57:04 2018

@author: liub725
"""
import csv


def getI_agg(model_name, junctionlistfile, I_datafile):
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
    Ibimg=dict(zip(link,[row['currA_imag'] for row in r5]))
    f2=open('output_current1.csv', 'r')
    r6=csv.DictReader(f2)
    Icimg=dict(zip(link,[row['currA_imag'] for row in r6]))
    f2.close()
    
    
    
   
    junctionkeys=['junction','info','in_branch','out_branch_1','out_branch_2','out_branch_3']
    with open (junctionlistfile,'r') as junctionfile:            
        junctioninfo=junctionfile.read().splitlines()
        junctioninfolist=[]
        for n in range(len(junctioninfo)):
            junctioninfolist.append(junctioninfo[n].split(','))
    global junctionlist
    junctionlist=[]
    for k in range(len(junctioninfolist)):
        junctionlist.append(dict(zip(junctionkeys,junctioninfolist[k])))

    global IiaJ
    global IibJ
    global IicJ
    global IoaJ
    global IobJ
    global IocJ
    IiaJ=[]
    IibJ=[] 
    IicJ=[]
    IoaJ=[]
    IobJ=[] 
    IocJ=[]
    for n in range(len(junctionlist)):
        if junctionlist[n]['out_branch_1']=='' and junctionlist[n]['out_branch_2']=='' and junctionlist[n]['out_branch_3']=='':
            IiaJ.append(complex(float(Ia[junctionlist[n]['in_branch']]),float(Iaimg[junctionlist[n]['in_branch']])))
            IibJ.append(complex(float(Ib[junctionlist[n]['in_branch']]),float(Ibimg[junctionlist[n]['in_branch']])))
            IicJ.append(complex(float(Ic[junctionlist[n]['in_branch']]),float(Icimg[junctionlist[n]['in_branch']])))
            IoaJ.append(complex(float(0),float(0))) 
            IobJ.append(complex(float(0),float(0))) 
            IocJ.append(complex(float(0),float(0))) 
        elif junctionlist[n]['out_branch_2']=='' and junctionlist[n]['out_branch_3']=='':
            IiaJ.append(complex(float(Ia[junctionlist[n]['in_branch']]),float(Iaimg[junctionlist[n]['in_branch']])))
            IibJ.append(complex(float(Ib[junctionlist[n]['in_branch']]),float(Ibimg[junctionlist[n]['in_branch']])))
            IicJ.append(complex(float(Ic[junctionlist[n]['in_branch']]),float(Icimg[junctionlist[n]['in_branch']])))
            IoaJ.append(complex(float(Ia[junctionlist[n]['out_branch_1']]),float(Iaimg[junctionlist[n]['out_branch_1']]))) 
            IobJ.append(complex(float(Ib[junctionlist[n]['out_branch_1']]),float(Ibimg[junctionlist[n]['out_branch_1']])))
            IocJ.append(complex(float(Ic[junctionlist[n]['out_branch_1']]),float(Icimg[junctionlist[n]['out_branch_1']])))
        elif junctionlist[n]['out_branch_2']!='' and junctionlist[n]['out_branch_3']=='':
            IiaJ.append(complex(float(Ia[junctionlist[n]['in_branch']]),float(Iaimg[junctionlist[n]['in_branch']])))
            IibJ.append(complex(float(Ib[junctionlist[n]['in_branch']]),float(Ibimg[junctionlist[n]['in_branch']])))
            IicJ.append(complex(float(Ic[junctionlist[n]['in_branch']]),float(Icimg[junctionlist[n]['in_branch']])))
            IoaJ.append(complex(float(Ia[junctionlist[n]['out_branch_1']]),float(Iaimg[junctionlist[n]['out_branch_1']]))+complex(float(Ia[junctionlist[n]['out_branch_2']]),float(Iaimg[junctionlist[n]['out_branch_2']]))) 
            IobJ.append(complex(float(Ib[junctionlist[n]['out_branch_1']]),float(Ibimg[junctionlist[n]['out_branch_1']]))+complex(float(Ib[junctionlist[n]['out_branch_2']]),float(Ibimg[junctionlist[n]['out_branch_2']])))
            IocJ.append(complex(float(Ic[junctionlist[n]['out_branch_1']]),float(Icimg[junctionlist[n]['out_branch_1']]))+complex(float(Ic[junctionlist[n]['out_branch_2']]),float(Icimg[junctionlist[n]['out_branch_2']])))
        elif junctionlist[n]['out_branch_2']!='' and junctionlist[n]['out_branch_3']!='':
            IiaJ.append(complex(float(Ia[junctionlist[n]['in_branch']]),float(Iaimg[junctionlist[n]['in_branch']])))
            IibJ.append(complex(float(Ib[junctionlist[n]['in_branch']]),float(Ibimg[junctionlist[n]['in_branch']])))
            IicJ.append(complex(float(Ic[junctionlist[n]['in_branch']]),float(Icimg[junctionlist[n]['in_branch']])))
            IoaJ.append(complex(float(Ia[junctionlist[n]['out_branch_1']]),float(Iaimg[junctionlist[n]['out_branch_1']]))+complex(float(Ia[junctionlist[n]['out_branch_2']]),float(Iaimg[junctionlist[n]['out_branch_2']]))+complex(float(Ia[junctionlist[n]['out_branch_3']]),float(Iaimg[junctionlist[n]['out_branch_3']]))) 
            IobJ.append(complex(float(Ib[junctionlist[n]['out_branch_1']]),float(Ibimg[junctionlist[n]['out_branch_1']]))+complex(float(Ib[junctionlist[n]['out_branch_2']]),float(Ibimg[junctionlist[n]['out_branch_2']]))+complex(float(Ib[junctionlist[n]['out_branch_3']]),float(Ibimg[junctionlist[n]['out_branch_3']])))
            IocJ.append(complex(float(Ic[junctionlist[n]['out_branch_1']]),float(Icimg[junctionlist[n]['out_branch_1']]))+complex(float(Ic[junctionlist[n]['out_branch_2']]),float(Icimg[junctionlist[n]['out_branch_2']]))+complex(float(Ic[junctionlist[n]['out_branch_3']]),float(Icimg[junctionlist[n]['out_branch_3']])))
#def calculate_S_agg():
#    global S_agg

def _tests():
    
	getI_agg('R5-12-47-1','junction_list_R5-12-47-1_new.csv','output_current.csv')

if __name__ == '__main__':
	_tests()