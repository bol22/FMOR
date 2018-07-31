# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:55:52 2018

@author: liub725
"""

import csv
import matplotlib.pyplot as plt
import os
import numpy as np
from numpy.linalg import inv
#import cmath
# get node voltage from the full model  

def getV(model_name, nodelistfile, V_datafile, new_Vdatafile):

    with open(V_datafile,'r') as f, open(new_Vdatafile,'w') as f1:
        next(f) # skip header line
        for line in f:
            f1.write(line)
    f2=open(new_Vdatafile, 'r')
    r=csv.DictReader(f2)
    node=[row['node_name'] for row in r]
    f2=open(new_Vdatafile, 'r')
    r1=csv.DictReader(f2)
    Va=dict(zip(node,[row['voltA_real'] for row in r1]))
    f2=open(new_Vdatafile, 'r')
    r2=csv.DictReader(f2)
    Vb=dict(zip(node,[row['voltB_real'] for row in r2]))
    f2=open(new_Vdatafile, 'r')
    r3=csv.DictReader(f2)
    Vc=dict(zip(node,[row['voltC_real'] for row in r3]))
    f2=open(new_Vdatafile, 'r')
    r4=csv.DictReader(f2)
    Vaimg=dict(zip(node,[row['voltA_imag'] for row in r4]))
    f2=open(new_Vdatafile, 'r')
    r5=csv.DictReader(f2)
    Vbimg=dict(zip(node,[row['voltB_imag'] for row in r5]))
    f2=open(new_Vdatafile, 'r')
    r6=csv.DictReader(f2)
    Vcimg=dict(zip(node,[row['voltC_imag'] for row in r6]))
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
    global Via, Vib, Vic, Vfa, Vfb, Vfc
    Via=[]; Vib=[]; Vic=[]; Vfa=[]; Vfb=[]; Vfc=[]
    
    for n in range(len(nodelist)):
    #    temp_node='R5-12-47-1_'+nodelist[n]['i_node']
        Via.append(complex(float(Va[model_name+'_node_'+nodelist[n]['i_node']]),float(Vaimg[model_name+'_node_'+nodelist[n]['i_node']])))
        Vib.append(complex(float(Vb[model_name+'_node_'+nodelist[n]['i_node']]),float(Vbimg[model_name+'_node_'+nodelist[n]['i_node']])))
        Vic.append(complex(float(Vc[model_name+'_node_'+nodelist[n]['i_node']]),float(Vcimg[model_name+'_node_'+nodelist[n]['i_node']])))
        Vfa.append(complex(float(Va[model_name+'_node_'+nodelist[n]['f_node']]),float(Vaimg[model_name+'_node_'+nodelist[n]['f_node']]))) 
        Vfb.append(complex(float(Vb[model_name+'_node_'+nodelist[n]['f_node']]),float(Vbimg[model_name+'_node_'+nodelist[n]['f_node']])))
        Vfc.append(complex(float(Vc[model_name+'_node_'+nodelist[n]['f_node']]),float(Vcimg[model_name+'_node_'+nodelist[n]['f_node']])))
        
def getV_sim(model_name, nodelistfile, V_datafile, new_Vdatafile):

    with open(V_datafile,'r') as f, open(new_Vdatafile,'w') as f1:
        next(f) # skip header line
        for line in f:
            f1.write(line)
    f2=open(new_Vdatafile, 'r')
    r=csv.DictReader(f2)
    node=[row['node_name'] for row in r]
    f2=open(new_Vdatafile, 'r')
    r1=csv.DictReader(f2)
    Va=dict(zip(node,[row['voltA_real'] for row in r1]))
    f2=open(new_Vdatafile, 'r')
    r2=csv.DictReader(f2)
    Vb=dict(zip(node,[row['voltB_real'] for row in r2]))
    f2=open(new_Vdatafile, 'r')
    r3=csv.DictReader(f2)
    Vc=dict(zip(node,[row['voltC_real'] for row in r3]))
    f2=open(new_Vdatafile, 'r')
    r4=csv.DictReader(f2)
    Vaimg=dict(zip(node,[row['voltA_imag'] for row in r4]))
    f2=open(new_Vdatafile, 'r')
    r5=csv.DictReader(f2)
    Vbimg=dict(zip(node,[row['voltB_imag'] for row in r5]))
    f2=open(new_Vdatafile, 'r')
    r6=csv.DictReader(f2)
    Vcimg=dict(zip(node,[row['voltC_imag'] for row in r6]))
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
    global Vias, Vibs, Vics, Vfas, Vfbs, Vfcs
    Vias=[]; Vibs=[]; Vics=[]; Vfas=[]; Vfbs=[];  Vfcs=[]
    
    for n in range(len(nodelist)):
    #    temp_node='R5-12-47-1_'+nodelist[n]['i_node']
        Vias.append(complex(float(Va[model_name+'_node_'+nodelist[n]['i_node']]),float(Vaimg[model_name+'_node_'+nodelist[n]['i_node']])))
        Vibs.append(complex(float(Vb[model_name+'_node_'+nodelist[n]['i_node']]),float(Vbimg[model_name+'_node_'+nodelist[n]['i_node']])))
        Vics.append(complex(float(Vc[model_name+'_node_'+nodelist[n]['i_node']]),float(Vcimg[model_name+'_node_'+nodelist[n]['i_node']])))
        Vfas.append(complex(float(Va[model_name+'_node_'+nodelist[n]['f_node']]),float(Vaimg[model_name+'_node_'+nodelist[n]['f_node']]))) 
        Vfbs.append(complex(float(Vb[model_name+'_node_'+nodelist[n]['f_node']]),float(Vbimg[model_name+'_node_'+nodelist[n]['f_node']])))
        Vfcs.append(complex(float(Vc[model_name+'_node_'+nodelist[n]['f_node']]),float(Vcimg[model_name+'_node_'+nodelist[n]['f_node']])))

#***********************************************************************************************************
# get current from the full model
def getI(model_name, linelistfile, I_datafile,new_Idatafile):

    with open(I_datafile,'r') as f, open(new_Idatafile,'w') as f1:
        next(f) # skip header line
        for line in f:
            f1.write(line)
    f2=open(new_Idatafile, 'r')
    r=csv.DictReader(f2)
    link=[row['link_name'] for row in r]
    f2=open(new_Idatafile, 'r')
    r1=csv.DictReader(f2)
    Ia=dict(zip(link,[row['currA_real'] for row in r1]))
    f2=open(new_Idatafile, 'r')
    r2=csv.DictReader(f2)
    Ib=dict(zip(link,[row['currB_real'] for row in r2]))
    f2=open(new_Idatafile, 'r')
    r3=csv.DictReader(f2)
    Ic=dict(zip(link,[row['currC_real'] for row in r3]))
    f2=open(new_Idatafile, 'r')
    r4=csv.DictReader(f2)
    Iaimg=dict(zip(link,[row['currA_imag'] for row in r4]))
    f2=open(new_Idatafile, 'r')
    r5=csv.DictReader(f2)
    Ibimg=dict(zip(link,[row['currB_imag'] for row in r5]))
    f2=open(new_Idatafile, 'r')
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
    
    global Iia, Iib, Iic, Ifa, Ifb, Ifc
    Iia=[]; Iib=[]; Iic=[]; Ifa=[]; Ifb=[]; Ifc=[]
    
    for n in range(len(linelist)):
        Iia.append(complex(float(Ia[linelist[n]['i_branch']]),float(Iaimg[linelist[n]['i_branch']])))
        Iib.append(complex(float(Ib[linelist[n]['i_branch']]),float(Ibimg[linelist[n]['i_branch']])))
        Iic.append(complex(float(Ic[linelist[n]['i_branch']]),float(Icimg[linelist[n]['i_branch']])))
        Ifa.append(complex(float(Ia[linelist[n]['f_branch']]),float(Iaimg[linelist[n]['f_branch']]))) 
        Ifb.append(complex(float(Ib[linelist[n]['f_branch']]),float(Ibimg[linelist[n]['f_branch']])))
        Ifc.append(complex(float(Ic[linelist[n]['f_branch']]),float(Icimg[linelist[n]['f_branch']])))

#***********************************************************************************************************
# get current for junction load aggreggation
        
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
    Ibimg=dict(zip(link,[row['currB_imag'] for row in r5]))
    f2=open('output_current1.csv', 'r')
    r6=csv.DictReader(f2)
    Icimg=dict(zip(link,[row['currC_imag'] for row in r6]))
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

    global IiaJ, IibJ, IicJ, IoaJ, IobJ, IocJ
    IiaJ=[]; IibJ=[]; IicJ=[]; IoaJ=[]; IobJ=[]; IocJ=[]
    
    for n in range(len(junctionlist)):
        if junctionlist[n]['out_branch_1']=='' and junctionlist[n]['out_branch_2']=='' and junctionlist[n]['out_branch_3']=='':
            IiaJ.append(complex(float(Ia[junctionlist[n]['in_branch']]),float(Iaimg[junctionlist[n]['in_branch']])))
            IibJ.append(complex(float(Ib[junctionlist[n]['in_branch']]),float(Ibimg[junctionlist[n]['in_branch']])))
            IicJ.append(complex(float(Ic[junctionlist[n]['in_branch']]),float(Icimg[junctionlist[n]['in_branch']])))
            IoaJ.append(complex(float(0),float(0))) 
            IobJ.append(complex(float(0),float(0))) 
            IocJ.append(complex(float(0),float(0))) 
        elif junctionlist[n]['out_branch_1']!='' and junctionlist[n]['out_branch_2']=='' and junctionlist[n]['out_branch_3']=='':
            IiaJ.append(complex(float(Ia[junctionlist[n]['in_branch']]),float(Iaimg[junctionlist[n]['in_branch']])))
            IibJ.append(complex(float(Ib[junctionlist[n]['in_branch']]),float(Ibimg[junctionlist[n]['in_branch']])))
            IicJ.append(complex(float(Ic[junctionlist[n]['in_branch']]),float(Icimg[junctionlist[n]['in_branch']])))
            IoaJ.append(complex(float(Ia[junctionlist[n]['out_branch_1']]),float(Iaimg[junctionlist[n]['out_branch_1']]))) 
            IobJ.append(complex(float(Ib[junctionlist[n]['out_branch_1']]),float(Ibimg[junctionlist[n]['out_branch_1']])))
            IocJ.append(complex(float(Ic[junctionlist[n]['out_branch_1']]),float(Icimg[junctionlist[n]['out_branch_1']])))
        elif junctionlist[n]['out_branch_1']!='' and junctionlist[n]['out_branch_2']!='' and junctionlist[n]['out_branch_3']=='':
            IiaJ.append(complex(float(Ia[junctionlist[n]['in_branch']]),float(Iaimg[junctionlist[n]['in_branch']])))
            IibJ.append(complex(float(Ib[junctionlist[n]['in_branch']]),float(Ibimg[junctionlist[n]['in_branch']])))
            IicJ.append(complex(float(Ic[junctionlist[n]['in_branch']]),float(Icimg[junctionlist[n]['in_branch']])))
            IoaJ.append(complex(float(Ia[junctionlist[n]['out_branch_1']]),float(Iaimg[junctionlist[n]['out_branch_1']]))+complex(float(Ia[junctionlist[n]['out_branch_2']]),float(Iaimg[junctionlist[n]['out_branch_2']]))) 
            IobJ.append(complex(float(Ib[junctionlist[n]['out_branch_1']]),float(Ibimg[junctionlist[n]['out_branch_1']]))+complex(float(Ib[junctionlist[n]['out_branch_2']]),float(Ibimg[junctionlist[n]['out_branch_2']])))
            IocJ.append(complex(float(Ic[junctionlist[n]['out_branch_1']]),float(Icimg[junctionlist[n]['out_branch_1']]))+complex(float(Ic[junctionlist[n]['out_branch_2']]),float(Icimg[junctionlist[n]['out_branch_2']])))
        elif junctionlist[n]['out_branch_1']!='' and junctionlist[n]['out_branch_2']!='' and junctionlist[n]['out_branch_3']!='':
            IiaJ.append(complex(float(Ia[junctionlist[n]['in_branch']]),float(Iaimg[junctionlist[n]['in_branch']])))
            IibJ.append(complex(float(Ib[junctionlist[n]['in_branch']]),float(Ibimg[junctionlist[n]['in_branch']])))
            IicJ.append(complex(float(Ic[junctionlist[n]['in_branch']]),float(Icimg[junctionlist[n]['in_branch']])))
            IoaJ.append(complex(float(Ia[junctionlist[n]['out_branch_1']]),float(Iaimg[junctionlist[n]['out_branch_1']]))+complex(float(Ia[junctionlist[n]['out_branch_2']]),float(Iaimg[junctionlist[n]['out_branch_2']]))+complex(float(Ia[junctionlist[n]['out_branch_3']]),float(Iaimg[junctionlist[n]['out_branch_3']]))) 
            IobJ.append(complex(float(Ib[junctionlist[n]['out_branch_1']]),float(Ibimg[junctionlist[n]['out_branch_1']]))+complex(float(Ib[junctionlist[n]['out_branch_2']]),float(Ibimg[junctionlist[n]['out_branch_2']]))+complex(float(Ib[junctionlist[n]['out_branch_3']]),float(Ibimg[junctionlist[n]['out_branch_3']])))
            IocJ.append(complex(float(Ic[junctionlist[n]['out_branch_1']]),float(Icimg[junctionlist[n]['out_branch_1']]))+complex(float(Ic[junctionlist[n]['out_branch_2']]),float(Icimg[junctionlist[n]['out_branch_2']]))+complex(float(Ic[junctionlist[n]['out_branch_3']]),float(Icimg[junctionlist[n]['out_branch_3']])))

#***********************************************************************************************************
# calculate impedance and load for simplified model

def calculate_Z_S():
    global Z, S, S_agg, dV, dV2, dI, dI2, Ii, Ii2, Zv, Zv2, S2, dIJ   
    #initiallize the arrays
    # no way to store matrix with different dimensions in a single variable
    dV=np.empty((53,3,1),dtype=complex)
    dV2=np.empty((53,2,1),dtype=complex)      #variables for two phase segment need to be defined seperatly
    dI=np.empty((53,3,1),dtype=complex)
    dI2=np.empty((53,2,1),dtype=complex)
    Ii=np.empty((53,3,6),dtype=complex)
    Ii2=np.empty((53,2,3),dtype=complex)
    Zv=np.empty((53,6,1),dtype=complex)
    Zv2=np.empty((53,3,1),dtype=complex)
    Z=np.empty((53,3,3),dtype=complex)
    S=np.empty((53,3,1),dtype=complex)
    S2=np.empty((53,2,1),dtype=complex)
    dIJ=np.empty((53,3,1),dtype=complex)
    S_agg=np.empty((53,3,1),dtype=complex)
        
    for n in range(len(Via)):
        
        if junctionlist[n]['junction']=='junction':
            dIJ[n]=np.array([[IiaJ[n]-IoaJ[n]],[IibJ[n]-IobJ[n]],[IicJ[n]-IocJ[n]]])
            S_agg[n][0][0]=Vfa[n]*dIJ[n][0][0].conjugate()
            S_agg[n][1][0]=Vfb[n]*dIJ[n][1][0].conjugate()
            S_agg[n][2][0]=Vfc[n]*dIJ[n][2][0].conjugate()
        else:
            S_agg[n]=np.array([[0],[0],[0]]) 
        

        if nodelist[n]['phase_name']=='ABC': # 3phase segment
            
            dV[n]=np.array([[Via[n]-Vfa[n]],[Vib[n]-Vfb[n]],[Vic[n]-Vfc[n]]])
            dI[n]=np.array([[Iia[n]-Ifa[n]],[Iib[n]-Ifb[n]],[Iic[n]-Ifc[n]]])
            
            Ii[n]=np.array([[Iia[n],Iib[n],Iic[n],0,0,0],[0,Iia[n],0,Iib[n],Iic[n],0],[0,0,Iia[n],0,Iib[n],Iic[n]]])
            Zv[n]=np.dot(np.dot(Ii[n].transpose().conjugate(),inv((np.dot(Ii[n],Ii[n].transpose().conjugate())))),dV[n])
            Z[n]=np.array([[Zv[n].item(0),Zv[n].item(1),Zv[n].item(2)],[Zv[n].item(1),Zv[n].item(3),Zv[n].item(4)],[Zv[n].item(2),Zv[n].item(4),Zv[n].item(5)]])
            if linelist[n]['i_branch']==linelist[n]['f_branch']:
                S[n]=np.array([[0],[0],[0]])
            else:
                S[n]=np.multiply(np.array([[Vfa[n]],[Vfb[n]],[Vfc[n]]]),dI[n].conjugate())
        elif nodelist[n]['phase_name']=='AB':
        
            dV2[n]=np.array([[Via[n]-Vfa[n]],[Vib[n]-Vfb[n]]])
            dI2[n]=np.array([[Iia[n]-Ifa[n]],[Iib[n]-Ifb[n]]])
            
            Ii2[n]=np.array([[Iia[n],Iib[n],0],[0,Iia[n],Iib[n]]])
            Zv2[n]=np.dot(np.dot(Ii2[n].transpose().conjugate(),inv((np.dot(Ii2[n],Ii2[n].transpose().conjugate())))),dV2[n])
            Z[n]=np.array([[Zv2[n].item(0),Zv2[n].item(1),0],[Zv2[n].item(1),Zv2[n].item(2),0],[0,0,0]])
            S2[n]=np.multiply(np.array([[Vfa[n]],[Vfb[n]]]),dI2[n].conjugate())
            S[n]=np.array([[S2[n][0][0]],[S2[n][1][0]],[0]])
            if linelist[n]['i_branch']==linelist[n]['f_branch']:
                S[n]=np.array([[0],[0],[0]])
            else:
                S[n]=np.array([[S2[n][0][0]],[S2[n][1][0]],[0]])
        elif nodelist[n]['phase_name']=='AC':
        
            dV2[n]=np.array([[Via[n]-Vfa[n]],[Vic[n]-Vfc[n]]])
            dI2[n]=np.array([[Iia[n]-Ifa[n]],[Iic[n]-Ifc[n]]])
            
            Ii2[n]=np.array([[Iia[n],Iic[n],0],[0,Iia[n],Iic[n]]])
            Zv2[n]=np.dot(np.dot(Ii2[n].transpose().conjugate(),inv((np.dot(Ii2[n],Ii2[n].transpose().conjugate())))),dV2[n])
            Z[n]=np.array([[Zv2[n].item(0),Zv2[n].item(1),0],[Zv2[n].item(1),Zv2[n].item(2),0],[0,0,0]])
            S2[n]=np.multiply(np.array([[Vfa[n]],[Vfc[n]]]),dI2[n].conjugate())
            if linelist[n]['i_branch']==linelist[n]['f_branch']:
                S[n]=np.array([[0],[0],[0]])
            else:
                S[n]=np.array([[S2[n][0][0]],[0],[S2[n][1][0]]])
        
        elif nodelist[n]['phase_name']=='BC':
        
            dV2[n]=np.array([[Vib[n]-Vfb[n]],[Vic[n]-Vfc[n]]])
            dI2[n]=np.array([[Iib[n]-Ifb[n]],[Iic[n]-Ifc[n]]])
            
            Ii2[n]=np.array([[Iib[n],Iic[n],0],[0,Iib[n],Iic[n]]])
            Zv2[n]=np.dot(np.dot(Ii2[n].transpose().conjugate(),inv((np.dot(Ii2[n],Ii2[n].transpose().conjugate())))),dV2[n])
            Z[n]=np.array([[Zv2[n].item(0),Zv2[n].item(1),0],[Zv2[n].item(1),Zv2[n].item(2),0],[0,0,0]])
            S2[n]=np.multiply(np.array([[Vfb[n]],[Vfc[n]]]),dI2[n].conjugate())
            if linelist[n]['i_branch']==linelist[n]['f_branch']:
                S[n]=np.array([[0],[0],[0]])
            else:
                S[n]=np.array([[0],[S2[n][0][0]],[S2[n][1][0]]])
                
        elif nodelist[n]['phase_name']=='A':
            
            dV[n]=np.array([[Via[n]-Vfa[n]],[0],[0]])
            dI[n]=np.array([[Iia[n]-Ifa[n]],[0],[0]])
            
            Z[n]=np.array([[np.dot(Via[n]-Vfa[n],(Iia[n])**(-1)),0,0],[0,0,0],[0,0,0]])
            if linelist[n]['i_branch']==linelist[n]['f_branch']:
                S[n]=np.array([[0],[0],[0]])
            else:
                S[n]=np.array([[np.multiply(Vfa[n],dI[n][0].conjugate())],[0],[0]])
        
        elif nodelist[n]['phase_name']=='B':
        
            dV[n]=np.array([[0],[Vib[n]-Vfb[n]],[0]])
            dI[n]=np.array([[0],[Iib[n]-Ifb[n]],[0]])
            
            Z[n]=np.array([[0,0,0],[0,np.dot(Vib[n]-Vfb[n],(Iib[n])**(-1)),0],[0,0,0]])
            if linelist[n]['i_branch']==linelist[n]['f_branch']:
                S[n]=np.array([[0],[0],[0]])
            else:
                S[n]=np.array([[0],[np.multiply(Vfb[n],dI[n][1].conjugate())],[0]])
        
        elif nodelist[n]['phase_name']=='C':
        
            dV[n]=np.array([[0],[0],[Vic[n]-Vfc[n]]])
            dI[n]=np.array([[0],[0],[Iic[n]-Ifc[n]]])
        
            Z[n]=np.array([[0,0,0],[0,0,0],[0,0,np.dot(Vic[n]-Vfc[n],(Iic[n])**(-1))]])
            if linelist[n]['i_branch']==linelist[n]['f_branch']:
                S[n]=np.array([[0],[0],[0]])
            else:
                S[n]=np.array([[0],[0],[np.multiply(Vfc[n],dI[n][2].conjugate())]])
                
#***********************************************************************************************************               
# write new gld model 
def CreateNode(seg_number,glmfile):
    f=open(glmfile,'a')
    f.write('object node {\n')
    f.write('	  name R5-12-47-1_node_'+nodelist[seg_number]['f_node']+';\n')
    f.write('     phases '+nodelist[seg_number]['phase_name']+'N;\n')
    f.write('	  nominal_voltage 7970.0 ;\n')
    f.write('	    voltage_A 7970.0+0.0j;\n')
    f.write('	    voltage_B -3985.00-6902.22j;\n')
    f.write('	    voltage_C -3985.00+6902.22j;\n')
    f.write('    }\n')
    return
    
# create line configurations
def CreateLineConfig(seg_number,glmfile):
    f=open(glmfile,'a')
    if nodelist[seg_number]['phase_name']=='ABC':
        f.write('object line_configuration {\n')
        f.write('    name line_config_seg_'+str(seg_number)+';\n')  
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
    elif nodelist[seg_number]['phase_name']=='AB':
        f.write('object line_configuration {\n')
        f.write('    name line_config_seg_'+str(seg_number)+';\n')  
        f.write('    z11 '+np.array2string(Z[seg_number][0][0])+';\n') 
        f.write('    z12 '+np.array2string(Z[seg_number][0][1])+';\n') 
        f.write('    z21 '+np.array2string(Z[seg_number][1][0])+';\n') 
        f.write('    z22 '+np.array2string(Z[seg_number][1][1])+';\n')         
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='AC':
        f.write('object line_configuration {\n')
        f.write('    name line_config_seg_'+str(seg_number)+';\n')  
        f.write('    z11 '+np.array2string(Z[seg_number][0][0])+';\n')         
        f.write('    z13 '+np.array2string(Z[seg_number][0][1])+';\n')         
        f.write('    z31 '+np.array2string(Z[seg_number][1][0])+';\n') 
        f.write('    z33 '+np.array2string(Z[seg_number][1][1])+';\n') 
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='BC':
        f.write('object line_configuration {\n')
        f.write('    name line_config_seg_'+str(seg_number)+';\n')          
        f.write('    z22 '+np.array2string(Z[seg_number][0][0])+';\n') 
        f.write('    z23 '+np.array2string(Z[seg_number][0][1])+';\n') 
        f.write('    z32 '+np.array2string(Z[seg_number][1][0])+';\n') 
        f.write('    z33 '+np.array2string(Z[seg_number][1][1])+';\n') 
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='A':
        f.write('object line_configuration {\n')
        f.write('    name line_config_seg_'+str(seg_number)+';\n')  
        f.write('    z11 '+np.array2string(Z[seg_number][0][0])+';\n') 
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='B':
        f.write('object line_configuration {\n')
        f.write('    name line_config_seg_'+str(seg_number)+';\n')  
        f.write('    z22 '+np.array2string(Z[seg_number][1][1])+';\n') 
        f.write('    }\n')        
    elif nodelist[seg_number]['phase_name']=='C':
        f.write('object line_configuration {\n')
        f.write('    name line_config_seg_'+str(seg_number)+';\n')  
        f.write('    z33 '+np.array2string(Z[seg_number][2][2])+';\n') 
        f.write('    }\n')
    return


# Create lines
def CreateLine(model_name,seg_number,glmfile):
    f=open(glmfile,'a')
    f.write('object overhead_line {\n')    
    f.write('    name line_seg_'+str(seg_number)+';\n') 
    if nodelist[seg_number]['phase_name']=='ABC':
        f.write('	 phases ABC;\n')
    elif nodelist[seg_number]['phase_name']=='A':
        f.write('    phases A;\n')
    elif nodelist[seg_number]['phase_name']=='B':
        f.write('    phases B;\n')
    elif nodelist[seg_number]['phase_name']=='C':
        f.write('    phases C;\n')
    elif nodelist[seg_number]['phase_name']=='AB':
        f.write('    phases AB;\n')
    elif nodelist[seg_number]['phase_name']=='AC':
        f.write('    phases AC;\n')
    elif nodelist[seg_number]['phase_name']=='BC':
        f.write('    phases BC;\n')
    f.write('    from '+model_name+'_node_'+nodelist[seg_number]['i_node']+';\n') 
    f.write('    to '+model_name+'_node_'+nodelist[seg_number]['f_node']+';\n')
    f.write('	 length 5280 ft;\n')
    f.write('	 configuration line_config_seg_'+str(seg_number)+';\n')
    f.write('    }\n')
    return

# Creat Meters to attached the loads
    
def CreateMeter(model_name,seg_number,glmfile):
    f=open(glmfile,'a')
    f.write('object meter {\n')
    f.write('    name meter_seg_'+str(seg_number)+';\n')
    f.write('    parent '+model_name+'_node_'+nodelist[seg_number]['f_node']+';\n')
    f.write('    }\n')
    return
    
    
# Create loads
    
def CreateLoad(model_name,seg_number,glmfile):
    f=open(glmfile,'a')
    if nodelist[seg_number]['phase_name']=='ABC':
        f.write('object load {\n')
        f.write('   parent '+model_name+'_node_'+nodelist[seg_number]['f_node']+';\n')
        f.write('   name load_seg_'+str(seg_number)+';\n')
        f.write('   phases ABCN;\n')
        f.write('   nominal_voltage 7970.0;\n')        # can't specefy voltage for different phases 
        f.write('   load_class U;\n')
        f.write('   constant_power_A '+np.array2string(S[seg_number][0][0])+';\n')
        f.write('   constant_power_B '+np.array2string(S[seg_number][1][0])+';\n')
        f.write('   constant_power_C '+np.array2string(S[seg_number][2][0])+';\n')
        f.write('	    voltage_A 7970.0+0.0j;\n')
        f.write('	    voltage_B -3985.00-6902.22j;\n')
        f.write('	    voltage_C -3985.00+6902.22j;\n')
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='AB':
        f.write('object load {\n')
        f.write('   parent '+model_name+'_node_'+nodelist[seg_number]['f_node']+';\n')
        f.write('   name load_seg_'+str(seg_number)+';\n')
        f.write('   phases ABN;\n')
        f.write('   nominal_voltage 7970.0;\n')        # can't specefy voltage for different phases 
        f.write('   load_class U;\n')
        f.write('   constant_power_A '+np.array2string(S[seg_number][0][0])+';\n')
        f.write('   constant_power_B '+np.array2string(S[seg_number][1][0])+';\n')
        f.write('	    voltage_A 7970.0+0.0j;\n')
        f.write('	    voltage_B -3985.00-6902.22j;\n')
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='AC':
        f.write('object load {\n')
        f.write('   parent '+model_name+'_node_'+nodelist[seg_number]['f_node']+';\n')
        f.write('   name load_seg_'+str(seg_number)+';\n')
        f.write('   phases ACN;\n')
        f.write('   nominal_voltage 7970.0;\n')        # can't specefy voltage for different phases
        f.write('   load_class U;\n')
        f.write('   constant_power_A '+np.array2string(S[seg_number][0][0])+';\n')
        f.write('   constant_power_C '+np.array2string(S[seg_number][2][0])+';\n')
        f.write('	    voltage_A 7970.0+0.0j;\n')
        f.write('	    voltage_C -3985.00+6902.22j;\n')
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='BC':
        f.write('object load {\n')
        f.write('   parent '+model_name+'_node_'+nodelist[seg_number]['f_node']+';\n')
        f.write('   name load_seg_'+str(seg_number)+';\n')
        f.write('   phases BCN;\n')
        f.write('   nominal_voltage 7970.0;\n')        # can't specefy voltage for different phases 
        f.write('   load_class U;\n')
        f.write('   constant_power_B '+np.array2string(S[seg_number][1][0])+';\n')
        f.write('   constant_power_C '+np.array2string(S[seg_number][2][0])+';\n')
        f.write('	    voltage_B -3985.00-6902.22j;\n')
        f.write('	    voltage_C -3985.00+6902.22j;\n')
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='A':
        f.write('object load {\n')
        f.write('   parent '+model_name+'_node_'+nodelist[seg_number]['f_node']+';\n')
        f.write('   name load_seg_'+str(seg_number)+';\n')
        f.write('	   phases AN;\n')
        f.write('   nominal_voltage 7970.0;\n')        # can't specefy voltage for different phases
        f.write('   load_class U;\n')
        f.write('	   constant_power_A '+np.array2string(S[seg_number][0][0])+';\n')
        f.write('	    voltage_A 7970.0+0.0j;\n')
        f.write('	    voltage_B -3985.00-6902.22j;\n')
        f.write('	    voltage_C -3985.00+6902.22j;\n')
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='B':
        f.write('object load {\n')
        f.write('   parent '+model_name+'_node_'+nodelist[seg_number]['f_node']+';\n')
        f.write('   name load_seg_'+str(seg_number)+';\n')
        f.write('	   phases BN;\n')
        f.write('   nominal_voltage 7970.0;\n')        # can't specefy voltage for different phases 
        f.write('   load_class U;\n')
        f.write('	   constant_power_B '+np.array2string(S[seg_number][1][0])+';\n')
        f.write('	    voltage_B -3985.00-6902.22j;\n')
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='C':
        f.write('object load {\n')
        f.write('   parent '+model_name+'_node_'+nodelist[seg_number]['f_node']+';\n')
        f.write('   name load_seg_'+str(seg_number)+';\n')
        f.write('	   phases CN;\n')
        f.write('   nominal_voltage 7970.0;\n')        # can't specefy voltage for different phases 
        f.write('   load_class U;\n')
        f.write('	   constant_power_C '+np.array2string(S[seg_number][2][0])+';\n')
        f.write('	    voltage_C -3985.00+6902.22j;\n')
        f.write('    }\n')
    return

def CreateLoad_agg(model_name,seg_number,glmfile):
    f=open(glmfile,'a')
    if junctionlist[seg_number]['junction']=='junction':
        f.write('object load {\n')
        f.write('   parent '+model_name+'_node_'+nodelist[seg_number]['f_node']+';\n')
        f.write('   name load_junction_seg_'+str(seg_number)+';\n')
        f.write('   phases '+nodelist[seg_number]['phase_name']+'N;\n')
        f.write('   nominal_voltage 7970.0;\n')        # can't specefy voltage for different phases 
        f.write('   load_class U;\n')
        f.write('   constant_power_A '+np.array2string(S_agg[seg_number][0][0])+';\n')
        f.write('   constant_power_B '+np.array2string(S_agg[seg_number][1][0])+';\n')
        f.write('   constant_power_C '+np.array2string(S_agg[seg_number][2][0])+';\n') 
        f.write('	    voltage_A 7970.0+0.0j;\n')
        f.write('	    voltage_B -3985.00-6902.22j;\n')
        f.write('	    voltage_C -3985.00+6902.22j;\n')
        f.write('    }\n')
    return
    
def CreateLoad_3phase(seg_number,glmfile):
    f=open(glmfile,'a')
    f.write('object load {\n')
    f.write('    name load_seg_'+str(seg_number)+';\n')
    f.write('	   phases ABCN;\n')
    f.write('	   nominal_voltage '+str(abs(Vfa[seg_number]))+';\n')        # can't specefy voltage for different phases 
    f.write('	   constant_power_A '+np.array2string(S[seg_number][0][0])+';\n')
    f.write('	   constant_power_B '+np.array2string(S[seg_number][1][0])+';\n')
    f.write('	   constant_power_C '+np.array2string(S[seg_number][2][0])+';\n')    
    f.write('    }\n')
    return
# two phase undefined
def CreateLoad_1phaseA(seg_number,glmfile):
    f=open(glmfile,'a')
    f.write('object load {\n')
    f.write('    name load_seg_'+str(seg_number)+';\n')
    f.write('	   phases AN;\n')
    f.write('	   nominal_voltage '+str(abs(Vfa[seg_number]))+';\n')        # can't specefy voltage for different phases 
    f.write('	   constant_power_A '+np.array2string(S[seg_number][0][0])+';\n')   
    f.write('    }\n')

def CreateLoad_1phaseB(seg_number,glmfile):
    f=open(glmfile,'a')
    f.write('object load {\n')
    f.write('    name load_seg_'+str(seg_number)+';\n')
    f.write('	   phases BN;\n')
    f.write('	   nominal_voltage '+str(abs(Vfb[seg_number]))+';\n')        # can't specefy voltage for different phases 
    f.write('	   constant_power_B '+np.array2string(S[seg_number][1][0])+';\n')   
    f.write('    }\n')

def CreateLoad_1phaseC(seg_number,glmfile):
    f=open(glmfile,'a')
    f.write('object load {\n')
    f.write('    name load_seg_'+str(seg_number)+';\n')
    f.write('	   phases ABCN;\n')
    f.write('	   nominal_voltage '+str(abs(Vfc[seg_number]))+';\n')        # can't specefy voltage for different phases 
    f.write('	   constant_power_C '+np.array2string(S[seg_number][2][0])+';\n')    
    f.write('    }\n')


#*********************************************
def CreateHeader(glmfile):
    f=open(glmfile,'a')
    f.write('//********************************\n')
    f.write('//Simplified feeder model\n')
#    f.write('// created by: Boming Liu\n')
    f.write('//\n')
    f.write('\n')
    f.write('clock{\n')
    f.write("   timezone EST+5EDT;\n")
    f.write("	timestamp '2000-01-01 0:00:00';\n")
    f.write("	stoptime '2000-01-02 0:00:00';\n")
    f.write("}\n")
    f.write("#set profiler=1\n\n")
    #create the module section
    f.write("\n")  
    f.write('module tape;\n')
    f.write('module powerflow{\n')
    f.write("	solver_method NR;\n")
    f.write("	default_maximum_voltage_error 1e-6;\n};\n\n")
    
    #swing bus node define
    f.write('object node {\n')
    f.write('    name R5-12-47-1_node_266;\n')
    f.write('    phases ABCN;\n')
    f.write('	    nominal_voltage 7970.0;\n')
    f.write('    bustype SWING;\n')
    f.write('	    voltage_A 7970.0+0.0j;\n')
    f.write('	    voltage_B -3985.00-6902.22j;\n')
    f.write('	    voltage_C -3985.00+6902.22j;\n')
    f.write('    }\n')
    
    f.write('object regulator_configuration {\n')
    f.write('	   name feeder_reg_cfg;\n')
    f.write('    Control OUTPUT_VOLTAGE;\n')
    f.write('	    band_center 8300.0;\n')
    f.write('	    band_width 132;\n')
    f.write('	    connect_type WYE_WYE;\n')
    f.write('	    time_delay 30;\n')
    f.write('	    raise_taps 16;\n')
    f.write('	    lower_taps 16;\n')
    f.write('	    regulation 0.10;\n')
    f.write('	    tap_pos_A 0;\n')
    f.write('	    tap_pos_B 0;\n')
    f.write('	    tap_pos_C 0;\n')
    f.write('    }\n')
    
    
    f.write('object meter {\n')
    f.write('	   name R5-12-47-1_meter_49;\n')
    f.write('    phases ABCN;\n')
    f.write('	    nominal_voltage 7970.0;\n')
    f.write('	    voltage_A 7970.0+0.0j;\n')
    f.write('	    voltage_B -3985.00-6902.22j;\n')
    f.write('	    voltage_C -3985.00+6902.22j;\n')
    f.write('    }\n')
    
    f.write('object regulator {\n')
    f.write('	   name feeder_reg_1;\n')
    f.write('    from R5-12-47-1_node_266;\n')
    f.write('	    to R5-12-47-1_meter_49;\n')
    f.write('	    phases ABCN;\n')
    f.write('	    configuration feeder_reg_cfg;\n')
    f.write('    }\n')

    # bus node
    f.write('object node {\n')
    f.write('	   parent R5-12-47-1_meter_49;\n')
    f.write('    name R5-12-47-1_node_'+nodelist[0]['i_node']+';\n')
    f.write('    phases ABCN;\n')
    f.write('	    nominal_voltage 7970.0;\n')
    f.write('	    voltage_A 7970.0+0.0j;\n')
    f.write('	    voltage_B -3985.00-6902.22j;\n')
    f.write('	    voltage_C -3985.00+6902.22j;\n')
    f.write('    }\n')
#create voltdump objects
#*********************************************
def CreateVoltdump(glmfile,outputfileName1,outputfileName2):
    f=open(glmfile,'a')
    f.write("object voltdump {\n")
    f.write("	filename "+outputfileName1+";\n")
    f.write("}\n\n")
    f=open(glmfile,'a')
    f.write("object voltdump {\n")
    f.write("	filename "+outputfileName2+";\n")
    f.write('mode polar;\n')
    f.write("}\n\n")
    return
def errorplot(baseV):
#    global errora
#    global errorb
#    global errorc    
    errora=[]
    errorb=[]
    errorc=[]
    for n in range(len(Vfa)):
        if Vfas[n]!=0j:      
            errora.append(abs((abs(Vfa[n])-abs(Vfas[n])))/baseV*100)
        else:            
            n=n+1
    for n in range(len(Vfb)):
        if Vfbs[n]!=0j:      
            errorb.append(abs((abs(Vfb[n])-abs(Vfbs[n])))/baseV*100)
        else:            
            n=n+1
    for n in range(len(Vfc)):
        if Vfcs[n]!=0j:      
            errorc.append(abs((abs(Vfc[n])-abs(Vfcs[n])))/baseV*100)
        else:            
            n=n+1

    indexa = np.arange(len(errora))
    indexb = np.arange(len(errorb))
    indexc = np.arange(len(errorc))
    plt.subplot(311)
    plt.bar(indexc,errorc,0.3,color='r',align="center")
    plt.title('Phase A error')
    plt.ylabel('V Error [p.u.]')
    plt.subplots_adjust(hspace=0.5)
    plt.subplot(312)
    plt.bar(indexa,errora,0.3,color='b',align="center")
    plt.title('Phase B error')
    plt.ylabel('V Error [p.u.]')
    plt.subplot(313)
    plt.bar(indexb,errorb,0.3,color='g',align="center")
    plt.title('Phase C error')
    plt.ylabel('V Error [p.u.]')
    plt.show()
    return

#******************************************
#create voltdump objects
#*********************************************
def CreateCurrdump(glmfile,outputfileName,):
    f=open(glmfile,'a')
    f.write("object currdump {\n")
    f.write("	filename "+outputfileName+";\n")
    f.write("}\n\n")
    return

def _tests():
    os.system('gridlabd R5-12.47-1_new')
    if os.path.exists('R5_s1.glm'):
        os.remove('R5_s1.glm')
    getV('R5-12-47-1','node_list_R5-12-47-1_new.csv','output_voltage.csv','output_voltage1.csv')
    getI('R5-12-47-1','line_list_R5-12-47-1_new.csv','output_current.csv','output_current1.csv')
    getI_agg('R5-12-47-1','junction_list_R5-12-47-1_new.csv','output_current.csv')
    calculate_Z_S()
    CreateHeader('R5_s1.glm')
    for n in range(len(nodelist)):
         CreateNode(n,'R5_s1.glm')
    for n in range(len(nodelist)):
         CreateLineConfig(n,'R5_s1.glm')
    for n in range(len(nodelist)):        
        CreateLine('R5-12-47-1',n,'R5_s1.glm')
#    for n in range(len(nodelist)):        
#        CreateMeter('R5-12-47-1',n,'R5_s1.glm')
    for n in range(len(nodelist)):        
        CreateLoad('R5-12-47-1',n,'R5_s1.glm')
    for n in range(len(nodelist)):  
        CreateLoad_agg('R5-12-47-1',n,'R5_s1.glm')
    CreateVoltdump('R5_s1.glm','R5_s1_voltage.csv','R5_s1_voltage_polar.csv')
    CreateCurrdump('R5_s1.glm','R5_s1_current.csv')
# run the simplified feeder model
    os.system('gridlabd R5_s1')
    getV_sim('R5-12-47-1','node_list_R5-12-47-1_new.csv','R5_s1_voltage.csv','output_voltage1sim.csv')
    errorplot(7970)

    

if __name__ == '__main__':
    _tests()
