# -*- coding: utf-8 -*-

#https://collaborate.pnl.gov/projects/Transactive/SitePages/Home.aspx
"""
Created on Mon Jul 23 15:06:09 2018

@author: liub725
"""
import csv
import os
import numpy as np
from numpy.linalg import inv

def CreateLine(seg_number,dssfile):
    f=open(dssfile,'a')
    if nodelist[seg_number]['phase_name']=='ABC':
        f.write('New Line.line_seg_'+str(seg_number)+' length=1 units=ml '+\
        'bus1=node_'+nodelist[seg_number]['i_node']+' bus2=node_'+nodelist[seg_number]['f_node']+' phases=3 rmatrix=['+\
        np.array2string(Z[seg_number][0][0].real)+' |'+np.array2string(Z[seg_number][1][0].real)+' '+np.array2string(Z[seg_number][1][1].real)+' |'+\
        np.array2string(Z[seg_number][2][0].real)+' '+np.array2string(Z[seg_number][2][1].real)+' '+np.array2string(Z[seg_number][2][2].real)+' ] xmatrix=['+\
        np.array2string(Z[seg_number][0][0].imag)+'|'+np.array2string(Z[seg_number][1][0].imag)+' '+np.array2string(Z[seg_number][1][1].imag)+'|'+\
        np.array2string(Z[seg_number][2][0].imag)+' '+np.array2string(Z[seg_number][2][1].imag)+' '+np.array2string(Z[seg_number][2][2].imag)+' ] cmatrix=[0 |0 0 |0 0 0] \n')
    elif nodelist[seg_number]['phase_name']=='AB':
        f.write('New Line.line_seg_'+str(seg_number)+' length=1 units=ml '+\
        'bus1=node_'+nodelist[seg_number]['i_node']+'.1.2 bus2=node_'+nodelist[seg_number]['f_node']+'.1.2 phases=2 rmatrix=['+\
        np.array2string(Z[seg_number][0][0].real)+' |'+np.array2string(Z[seg_number][1][0].real)+' '+np.array2string(Z[seg_number][1][1].real)+' ] xmatrix=['+\
        np.array2string(Z[seg_number][0][0].imag)+'|'+np.array2string(Z[seg_number][1][0].imag)+' '+np.array2string(Z[seg_number][1][1].imag)+' ] cmatrix=[0 |0 0 ] \n')
    elif nodelist[seg_number]['phase_name']=='AC':
        f.write('New Line.line_seg_'+str(seg_number)+' length=1 units=ml '+\
        'bus1=node_'+nodelist[seg_number]['i_node']+'.1.3 bus2=node_'+nodelist[seg_number]['f_node']+'.1.3 phases=2 rmatrix=['+\
        np.array2string(Z[seg_number][0][0].real)+' |'+np.array2string(Z[seg_number][1][0].real)+' '+np.array2string(Z[seg_number][1][1].real)+' ] xmatrix=['+\
        np.array2string(Z[seg_number][0][0].imag)+'|'+np.array2string(Z[seg_number][1][0].imag)+' '+np.array2string(Z[seg_number][1][1].imag)+' ] cmatrix=[0 |0 0 ] \n')
    elif nodelist[seg_number]['phase_name']=='BC':
        f.write('New Line.line_seg_'+str(seg_number)+' length=1 units=ml '+\
        'bus1=node_'+nodelist[seg_number]['i_node']+'.2.3 bus2=node_'+nodelist[seg_number]['f_node']+'.2.3 phases=2 rmatrix=['+\
        np.array2string(Z[seg_number][0][0].real)+' |'+np.array2string(Z[seg_number][1][0].real)+' '+np.array2string(Z[seg_number][1][1].real)+' ] xmatrix=['+\
        np.array2string(Z[seg_number][0][0].imag)+'|'+np.array2string(Z[seg_number][1][0].imag)+' '+np.array2string(Z[seg_number][1][1].imag)+' ] cmatrix=[0 |0 0 ] \n')
    elif nodelist[seg_number]['phase_name']=='A':
        f.write('New Line.line_seg_'+str(seg_number)+' length=1 units=ml bus1=node_'+nodelist[seg_number]['i_node']+'.1 bus2=node_'+nodelist[seg_number]['f_node']+\
        '.1 phases=1 rmatrix=['+np.array2string(Z[seg_number][0][0].real)+' ] xmatrix=['+np.array2string(Z[seg_number][0][0].imag)+' ] cmatrix=[0] \n')
    elif nodelist[seg_number]['phase_name']=='B':
        f.write('New Line.line_seg_'+str(seg_number)+' length=1 units=ml bus1=node_'+nodelist[seg_number]['i_node']+'.2 bus2=node_'+nodelist[seg_number]['f_node']+\
        '.2 phases=1 rmatrix=['+np.array2string(Z[seg_number][1][1].real)+' ] xmatrix=['+np.array2string(Z[seg_number][1][1].imag)+' ] cmatrix=[0] \n')
    elif nodelist[seg_number]['phase_name']=='C':
        f.write('New Line.line_seg_'+str(seg_number)+' length=1 units=ml bus1=node_'+nodelist[seg_number]['i_node']+'.3 bus2=node_'+nodelist[seg_number]['f_node']+\
        '.3 phases=1 rmatrix=['+np.array2string(Z[seg_number][2][2].real)+' ] xmatrix=['+np.array2string(Z[seg_number][2][2].imag)+' ] cmatrix=[0] \n')
    return
def CreateLoad(seg_number,dssfile):
    f=open(dssfile,'a')
    if nodelist[seg_number]['phase_name']=='ABC':
        f.write('New Load.seg_'+str(seg_number)+'_a phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.1\
        kV=7.970 kW='+np.array2string(S[seg_number][0][0].real/1000)+' kvar='+np.array2string(S[seg_number][0][0].imag/1000)+\
        ' Vmaxpu=1.2 Vminpu=0.8 \n')
        f.write('New Load.seg_'+str(seg_number)+'_b phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.2\
        kV=7.970 kW='+np.array2string(S[seg_number][1][0].real/1000)+' kvar='+np.array2string(S[seg_number][1][0].imag/1000)+\
        ' Vmaxpu=1.2 Vminpu=0.8 \n')
        f.write('New Load.seg_'+str(seg_number)+'_c phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.3\
        kV=7.970 kW='+np.array2string(S[seg_number][2][0].real/1000)+' kvar='+np.array2string(S[seg_number][2][0].imag/1000)+\
        ' Vmaxpu=1.2 Vminpu=0.8 \n')
    elif nodelist[seg_number]['phase_name']=='AB':
        f.write('New Load.seg_'+str(seg_number)+'_a phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.1\
        kV=7.970 kW='+np.array2string(S[seg_number][0][0].real/1000)+' kvar='+np.array2string(S[seg_number][0][0].imag/1000)+\
        ' Vmaxpu=1.2 Vminpu=0.8 \n')
        f.write('New Load.seg_'+str(seg_number)+'_b phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.2\
        kV=7.970 kW='+np.array2string(S[seg_number][1][0].real/1000)+' kvar='+np.array2string(S[seg_number][1][0].imag/1000)+\
        ' Vmaxpu=1.2 Vminpu=0.8 \n')
    elif nodelist[seg_number]['phase_name']=='AC':
        f.write('New Load.seg_'+str(seg_number)+'_a phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.1\
        kV=7.970 kW='+np.array2string(S[seg_number][0][0].real/1000)+' kvar='+np.array2string(S[seg_number][0][0].imag/1000)+\
        ' Vmaxpu=1.2 Vminpu=0.8 \n')
        f.write('New Load.seg_'+str(seg_number)+'_c phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.3\
        kV=7.970 kW='+np.array2string(S[seg_number][2][0].real/1000)+' kvar='+np.array2string(S[seg_number][2][0].imag/1000)+\
        ' Vmaxpu=1.2 Vminpu=0.8 \n')
    elif nodelist[seg_number]['phase_name']=='BC':
        f.write('New Load.seg_'+str(seg_number)+'_b phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.2\
        kV=7.970 kW='+np.array2string(S[seg_number][1][0].real/1000)+' kvar='+np.array2string(S[seg_number][1][0].imag/1000)+\
        ' Vmaxpu=1.2 Vminpu=0.8 \n')
        f.write('New Load.seg_'+str(seg_number)+'_c phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.3\
        kV=7.970 kW='+np.array2string(S[seg_number][2][0].real/1000)+' kvar='+np.array2string(S[seg_number][2][0].imag/1000)+\
        ' Vmaxpu=1.2 Vminpu=0.8 \n')
    elif nodelist[seg_number]['phase_name']=='A':
        f.write('New Load.seg_'+str(seg_number)+'_a phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.1\
        kV=7.970 kW='+np.array2string(S[seg_number][0][0].real/1000)+' kvar='+np.array2string(S[seg_number][0][0].imag/1000)+\
        ' Vmaxpu=1.2 Vminpu=0.8 \n')
    elif nodelist[seg_number]['phase_name']=='B':
        f.write('New Load.seg_'+str(seg_number)+'_b phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.2\
        kV=7.970 kW='+np.array2string(S[seg_number][1][0].real/1000)+' kvar='+np.array2string(S[seg_number][1][0].imag/1000)+\
        ' Vmaxpu=1.2 Vminpu=0.8 \n')
    elif nodelist[seg_number]['phase_name']=='C':
        f.write('New Load.seg_'+str(seg_number)+'_c phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.3\
        kV=7.970 kW='+np.array2string(S[seg_number][2][0].real/1000)+' kvar='+np.array2string(S[seg_number][2][0].imag/1000)+\
        ' Vmaxpu=1.2 Vminpu=0.8 \n')
    return

def CreateLoad_agg(seg_number,dssfile):
    if junctionlist[seg_number]['junction']=='junction':
        f=open(dssfile,'a')
        if nodelist[seg_number]['phase_name']=='ABC':
            f.write('New Load.seg_junction_'+str(seg_number)+'_a phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.1\
            kV=7.970 kW='+np.array2string(S_agg[seg_number][0][0].real/1000)+' kvar='+np.array2string(S_agg[seg_number][0][0].imag/1000)+\
            ' Vmaxpu=1.2 Vminpu=0.8 \n')
            f.write('New Load.seg_junction_'+str(seg_number)+'_b phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.2\
            kV=7.970 kW='+np.array2string(S_agg[seg_number][1][0].real/1000)+' kvar='+np.array2string(S_agg[seg_number][1][0].imag/1000)+\
            ' Vmaxpu=1.2 Vminpu=0.8 \n')
            f.write('New Load.seg_junction_'+str(seg_number)+'_c phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.3\
            kV=7.970 kW='+np.array2string(S_agg[seg_number][2][0].real/1000)+' kvar='+np.array2string(S_agg[seg_number][2][0].imag/1000)+\
            ' Vmaxpu=1.2 Vminpu=0.8 \n')
        elif nodelist[seg_number]['phase_name']=='AB':
            f.write('New Load.seg_junction_'+str(seg_number)+'_a phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.1\
            kV=7.970 kW='+np.array2string(S_agg[seg_number][0][0].real/1000)+' kvar='+np.array2string(S_agg[seg_number][0][0].imag/1000)+\
            ' Vmaxpu=1.2 Vminpu=0.8 \n')
            f.write('New Load.seg_junction_'+str(seg_number)+'_b phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.2\
            kV=7.970 kW='+np.array2string(S_agg[seg_number][1][0].real/1000)+' kvar='+np.array2string(S_agg[seg_number][1][0].imag/1000)+\
            ' Vmaxpu=1.2 Vminpu=0.8 \n')
        elif nodelist[seg_number]['phase_name']=='AC':
            f.write('New Load.seg_junction_'+str(seg_number)+'_a phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.1\
            kV=7.970 kW='+np.array2string(S_agg[seg_number][0][0].real/1000)+' kvar='+np.array2string(S_agg[seg_number][0][0].imag/1000)+\
            ' Vmaxpu=1.2 Vminpu=0.8 \n')
            f.write('New Load.seg_junction_'+str(seg_number)+'_c phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.3\
            kV=7.970 kW='+np.array2string(S_agg[seg_number][2][0].real/1000)+' kvar='+np.array2string(S_agg[seg_number][2][0].imag/1000)+\
            ' Vmaxpu=1.2 Vminpu=0.8 \n')
        elif nodelist[seg_number]['phase_name']=='BC':
            f.write('New Load.seg_junction_'+str(seg_number)+'_b phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.2\
            kV=7.970 kW='+np.array2string(S_agg[seg_number][1][0].real/1000)+' kvar='+np.array2string(S_agg[seg_number][1][0].imag/1000)+\
            ' Vmaxpu=1.2 Vminpu=0.8 \n')
            f.write('New Load.seg_junction_'+str(seg_number)+'_c phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.3\
            kV=7.970 kW='+np.array2string(S_agg[seg_number][2][0].real/1000)+' kvar='+np.array2string(S_agg[seg_number][2][0].imag/1000)+\
            ' Vmaxpu=1.2 Vminpu=0.8 \n')
        elif nodelist[seg_number]['phase_name']=='A':
            f.write('New Load.seg_junction_'+str(seg_number)+'_a phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.1\
            kV=7.970 kW='+np.array2string(S_agg[seg_number][0][0].real/1000)+' kvar='+np.array2string(S_agg[seg_number][0][0].imag/1000)+\
            ' Vmaxpu=1.2 Vminpu=0.8 \n')
        elif nodelist[seg_number]['phase_name']=='B':
            f.write('New Load.seg_junction_'+str(seg_number)+'_b phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.2\
            kV=7.970 kW='+np.array2string(S_agg[seg_number][1][0].real/1000)+' kvar='+np.array2string(S_agg[seg_number][1][0].imag/1000)+\
            ' Vmaxpu=1.2 Vminpu=0.8 \n')
        elif nodelist[seg_number]['phase_name']=='C':
            f.write('New Load.seg_junction_'+str(seg_number)+'_c phases=1 Bus1=node_'+nodelist[seg_number]['f_node']+'.3\
            kV=7.970 kW='+np.array2string(S_agg[seg_number][2][0].real/1000)+' kvar='+np.array2string(S_agg[seg_number][2][0].imag/1000)+\
            ' Vmaxpu=1.2 Vminpu=0.8 \n')

     
def _tests():

    if os.path.exists('R5_s1.dss'):
        os.remove('R5_s1.dss')
    f=open('R5_s1.dss','a')
    f.write('new circuit.R5_s1 basekv=7.970 pu=1.000 phases=3 bus1=node_266 ang=-30 MVAsc3=60000 \n')
    f.write('new line.trunk bus1=node_266 bus2=node_265 phases=3 switch=yes\n')
    f.write('new energymeter.feeder element=line.trunk terminal=1\n')
    f.close()
    for n in range(len(nodelist)):        
        CreateLine(n,'R5_s1.dss')
    for n in range(len(nodelist)):       
        CreateLoad(n,'R5_s1.dss')
    for n in range(len(nodelist)):
        CreateLoad_agg(n,'R5_s1.dss')
    f=open('R5_s1.dss','a')
    f.write('Set Voltagebases=[7.970] \n')
#    f.write('set voltagebases="100,34.5,24.9,22.9,13.8,12.47,0.48,0.208"')
    f.write('calcv \n')
    f.write('Solve \n')
#    for n in range(len(nodelist)):        
#        CreateMeter('R5-12-47-1',n,'R5_s1.glm')
#    for n in range(len(nodelist)):        
#        CreateLoad('R5-12-47-1',n,'R5_s1.glm')
#        CreateLoad_agg('R5-12-47-1',n,'R5_s1.glm')
#    CreateVoltdump('R5_s1.glm','R5_s1_voltage.csv')
#    CreateCurrdump('R5_s1.glm','R5_s1_current.csv')
    

if __name__ == '__main__':
	_tests()