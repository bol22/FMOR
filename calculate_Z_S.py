# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:29:51 2018

@author: liub725
"""
import numpy as np
def calculate_Z_S():
    global Z
    global S 
    global S_agg
    #initiallize the arrays
    # no way to store matrix with different dimensions in a single variable

    dV=np.empty((52,3,1),dtype=complex)
    dV2=np.empty((52,2,1),dtype=complex)      #variables for two phase segment need to be defined seperatly
    dI=np.empty((52,3,1),dtype=complex)
    dI2=np.empty((52,2,1),dtype=complex)
    Ii=np.empty((52,3,6),dtype=complex)
    Ii2=np.empty((52,2,3),dtype=complex)
    Zv=np.empty((52,6,1),dtype=complex)
    Zv2=np.empty((52,3,1),dtype=complex)
    Z=np.empty((52,3,3),dtype=complex)
    S=np.empty((52,3,1),dtype=complex)
    S2=np.empty((52,2,1),dtype=complex)
    dIJ=np.empty((52,3,1),dtype=complex)
    S_agg=np.empty((52,3,1),dtype=complex)
    
    for n in range(len(Via)):
        
        if junctionlist[n]['junction']=='junction':
            dIJ[n]=np.array([[IiaJ[n]-IoaJ[n]],[IibJ[n]-IobJ[n]],[IicJ[n]-IocJ[n]]])
            S_agg[n]=np.multiply(np.array([[Vfa[n]],[Vfb[n]],[Vfc[n]]]),dIJ[n].conjugate())
        else:
            S_agg[n]=np.array([[0],[0],[0]]) 
        

        if nodelist[n]['phase_name']=='ABC': # 3phase segment
            
            dV[n]=np.array([[Via[n]-Vfa[n]],[Vib[n]-Vfb[n]],[Vic[n]-Vfc[n]]])
            dI[n]=np.array([[Iia[n]-Ifa[n]],[Iib[n]-Ifb[n]],[Iic[n]-Ifc[n]]])
            
            Ii[n]=np.array([[Iia[n],Iib[n],Iic[n],0,0,0],[0,Iia[n],0,Iib[n],Iic[n],0],[0,0,Iia[n],0,Iib[n],Iic[n]]])
            Zv[n]=np.dot((np.dot(Ii[n].transpose(),(np.dot(Ii[n],Ii[n].transpose()))**(-1))),dV[n])
            Z[n]=np.array([[Zv[n].item(0),Zv[n].item(1),Zv[n].item(2)],[Zv[n].item(1),Zv[n].item(3),Zv[n].item(4)],[Zv[n].item(2),Zv[n].item(4),Zv[n].item(5)]])
            if linelist[n]['i_branch']==linelist[n]['f_branch']:
                S[n]=np.array([[0],[0],[0]])
            else:
                S[n]=np.multiply(np.array([[Vfa[n]],[Vfb[n]],[Vfc[n]]]),dI[n].conjugate())
        elif nodelist[n]['phase_name']=='AB':
        
            dV2[n]=np.array([[Via[n]-Vfa[n]],[Vib[n]-Vfb[n]]])
            dI2[n]=np.array([[Iia[n]-Ifa[n]],[Iib[n]-Ifb[n]]])
            
            Ii2[n]=np.array([[Iia[n],Iib[n],0],[0,Iia[n],Iib[n]]])
            Zv2[n]=np.dot((np.dot(Ii2[n].transpose(),(np.dot(Ii2[n],Ii2[n].transpose()))**(-1))),dV2[n])
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
            Zv2[n]=np.dot((np.dot(Ii2[n].transpose(),(np.dot(Ii2[n],Ii2[n].transpose()))**(-1))),dV2[n])
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
            Zv2[n]=np.dot((np.dot(Ii2[n].transpose(),(np.dot(Ii2[n],Ii2[n].transpose()))**(-1))),dV2[n])
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
  
#define new line configuration

def _tests():
    
	calculate_Z_S()

if __name__ == '__main__':
	_tests()