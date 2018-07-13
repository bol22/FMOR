# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:30:26 2018

@author: liub725
"""
# line distance are eqaul  



import numpy as np
# write gridlab-d model
def CreateNode(seg_number,glmfile):
    f=open(glmfile,'a')
    f.write('object node {\n')
    f.write('	  name R5-12-47-1_node_'+nodelist[seg_number]['f_node']+';\n')
    f.write('     phases '+nodelist[seg_number]['phase_name']+'N;\n')
    f.write('	  nominal_voltage 7970.0 ;\n')
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
#    elif nodelist[seg_number]['phase_name']=='AB':
#        f.write('    phases ABN ;\n')
#    elif nodelist[seg_number]['phase_name']=='AC':
#        f.write('    phases ACN ;\n')
#    elif nodelist[seg_number]['phase_name']=='BC':
    return

# define line config seperately

#def CreateLineConfig_3phase(seg_number,glmfile):
#    f=open(glmfile,'a')
#    f.write('object line_configuration {\n')
#    f.write('    name line_seg_'+str(seg_number)+';\n')  
#    f.write('    z11 '+np.array2string(Z[seg_number][0][0])+';\n') 
#    f.write('    z12 '+np.array2string(Z[seg_number][0][1])+';\n') 
#    f.write('    z13 '+np.array2string(Z[seg_number][0][2])+';\n') 
#    f.write('    z21 '+np.array2string(Z[seg_number][1][0])+';\n') 
#    f.write('    z22 '+np.array2string(Z[seg_number][1][1])+';\n') 
#    f.write('    z23 '+np.array2string(Z[seg_number][1][2])+';\n') 
#    f.write('    z31 '+np.array2string(Z[seg_number][2][0])+';\n') 
#    f.write('    z32 '+np.array2string(Z[seg_number][2][1])+';\n') 
#    f.write('    z33 '+np.array2string(Z[seg_number][2][2])+';\n') 
#    f.write('    }\n')
#    return
#
#def CreateLineConfig_1phaseA(seg_number,glmfile):
#    f=open(glmfile,'a')
#    f.write('object line_configuration {\n')
#    f.write('    name line_config_seg_'+str(seg_number)+';\n')  
#    f.write('    z11 '+np.array2string(Z[seg_number][0][0])+';\n') 
#    f.write('    }\n')
#    return
#
#def CreateLineConfig_1phaseB(seg_number,glmfile):
#    f=open(glmfile,'a')
#    f.write('object line_configuration {\n')
#    f.write('    name line_config_seg_'+str(seg_number)+';\n')  
#    f.write('    z22 '+np.array2string(Z[seg_number][1][1])+';\n') 
#    f.write('    }\n')
#    return
#
#def CreateLineConfig_1phaseC(seg_number,glmfile):
#    f=open(glmfile,'a')
#    f.write('object line_configuration {\n')
#    f.write('    name line_config_seg_'+str(seg_number)+';\n')  
#    f.write('    z33 '+np.array2string(Z[seg_number][2][2])+';\n') 
#    f.write('    }\n')
#    return

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
    f.write('	 length 1.00 ;\n')
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
    
def CreateLoad(seg_number,glmfile):
    f=open(glmfile,'a')
    if nodelist[seg_number]['phase_name']=='ABC':
        f.write('object load {\n')
        f.write('   parent meter_seg_'+str(seg_number)+';\n')
        f.write('   name load_seg_'+str(seg_number)+';\n')
        f.write('   phases ABCN;\n')
        f.write('   nominal_voltage '+str(abs(Vfa[seg_number]))+';\n')        # can't specefy voltage for different phases 
        f.write('   constant_power_A '+np.array2string(S[seg_number][0][0])+';\n')
        f.write('   constant_power_B '+np.array2string(S[seg_number][1][0])+';\n')
        f.write('   constant_power_C '+np.array2string(S[seg_number][2][0])+';\n')    
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='AB':
        f.write('object load {\n')
        f.write('   parent meter_seg_'+str(seg_number)+';\n')
        f.write('   name load_seg_'+str(seg_number)+';\n')
        f.write('   phases ABN;\n')
        f.write('   nominal_voltage '+str(abs(Vfa[seg_number]))+';\n')        # can't specefy voltage for different phases 
        f.write('   constant_power_A '+np.array2string(S[seg_number][0][0])+';\n')
        f.write('   constant_power_B '+np.array2string(S[seg_number][1][0])+';\n')
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='AC':
        f.write('object load {\n')
        f.write('   parent meter_seg_'+str(seg_number)+';\n')
        f.write('   name load_seg_'+str(seg_number)+';\n')
        f.write('   phases ACN;\n')
        f.write('   nominal_voltage '+str(abs(Vfa[seg_number]))+';\n')        # can't specefy voltage for different phases 
        f.write('   constant_power_A '+np.array2string(S[seg_number][0][0])+';\n')
        f.write('   constant_power_C '+np.array2string(S[seg_number][2][0])+';\n')    
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='BC':
        f.write('object load {\n')
        f.write('   parent meter_seg_'+str(seg_number)+';\n')
        f.write('   name load_seg_'+str(seg_number)+';\n')
        f.write('   phases BCN;\n')
        f.write('   nominal_voltage '+str(abs(Vfa[seg_number]))+';\n')        # can't specefy voltage for different phases 
        f.write('   constant_power_B '+np.array2string(S[seg_number][1][0])+';\n')
        f.write('   constant_power_C '+np.array2string(S[seg_number][2][0])+';\n')    
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='A':
        f.write('object load {\n')
        f.write('   parent meter_seg_'+str(seg_number)+';\n')
        f.write('   name load_seg_'+str(seg_number)+';\n')
        f.write('	   phases AN;\n')
        f.write('	   nominal_voltage '+str(abs(Vfa[seg_number]))+';\n')        # can't specefy voltage for different phases 
        f.write('	   constant_power_A '+np.array2string(S[seg_number][0][0])+';\n')   
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='B':
        f.write('object load {\n')
        f.write('   parent meter_seg_'+str(seg_number)+';\n')
        f.write('   name load_seg_'+str(seg_number)+';\n')
        f.write('	   phases BN;\n')
        f.write('	   nominal_voltage '+str(abs(Vfb[seg_number]))+';\n')        # can't specefy voltage for different phases 
        f.write('	   constant_power_B '+np.array2string(S[seg_number][1][0])+';\n')   
        f.write('    }\n')
    elif nodelist[seg_number]['phase_name']=='C':
        f.write('object load {\n')
        f.write('   parent meter_seg_'+str(seg_number)+';\n')
        f.write('   name load_seg_'+str(seg_number)+';\n')
        f.write('	   phases ABCN;\n')
        f.write('	   nominal_voltage '+str(abs(Vfc[seg_number]))+';\n')        # can't specefy voltage for different phases 
        f.write('	   constant_power_C '+np.array2string(S[seg_number][2][0])+';\n')    
        f.write('    }\n')
    return

def CreateLoad_agg(seg_number,glmfile):
    f=open(glmfile,'a')
    if junctionlist[seg_number]['junction']=='junction':
        f.write('object load {\n')
        f.write('   parent meter_seg_'+str(seg_number)+';\n')
        f.write('   name load_junction_seg_'+str(seg_number)+';\n')
        f.write('   phases ABCN;\n')
        f.write('   nominal_voltage '+str(abs(Vfa[seg_number]))+';\n')        # can't specefy voltage for different phases 
        f.write('   constant_power_A '+np.array2string(S_agg[seg_number][0][0])+';\n')
        f.write('   constant_power_B '+np.array2string(S_agg[seg_number][1][0])+';\n')
        f.write('   constant_power_C '+np.array2string(S_agg[seg_number][2][0])+';\n')    
        f.write('    }\n')
#    elif junctionlist[seg_number]['phase_name']=='A':
#        f.write('object load {\n')
#        f.write('   parent meter_seg_'+str(seg_number)+';\n')
#        f.write('   name load_seg_'+str(seg_number)+';\n')
#        f.write('	   phases AN ;\n')
#        f.write('	   nominal_voltage '+str(abs(Vfa[seg_number]))+';\n')        # can't specefy voltage for different phases 
#        f.write('	   constant_power_A '+np.array2string(S[seg_number][0][0])+';\n')   
#        f.write('    }\n')
#    elif junctionlist[seg_number]['phase_name']=='B':
#        f.write('object load {\n')
#        f.write('   parent meter_seg_'+str(seg_number)+';\n')
#        f.write('   name load_seg_'+str(seg_number)+';\n')
#        f.write('	   phases BN ;\n')
#        f.write('	   nominal_voltage '+str(abs(Vfb[seg_number]))+';\n')        # can't specefy voltage for different phases 
#        f.write('	   constant_power_B '+np.array2string(S[seg_number][1][0])+';\n')   
#        f.write('    }\n')
#    elif junctionlist[seg_number]['phase_name']=='C':
#        f.write('object load {\n')
#        f.write('   parent meter_seg_'+str(seg_number)+';\n')
#        f.write('   name load_seg_'+str(seg_number)+';\n')
#        f.write('	   phases ABCN ;\n')
#        f.write('	   nominal_voltage '+str(abs(Vfc[seg_number]))+';\n')        # can't specefy voltage for different phases 
#        f.write('	   constant_power_C '+np.array2string(S[seg_number][2][0])+';\n')    
#        f.write('    }\n')
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

def CreateHeader(glmfile):
    f=open(glmfile,'a')
    f.write('//********************************\n')
    f.write('//Simplified feeder model\n')
#    f.write('// created by: Boming Liu\n')
    f.write('//\n')
    f.write('\n')
    f.write('clock{\n')
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
    f.write('    name R5-12-47-1_node_'+nodelist[0]['i_node']+';\n')
    f.write('    phases ABCN;\n')
    f.write('	    nominal_voltage 7970.0;\n')
    f.write('    bustype SWING;\n')
    f.write('    }\n')

def _tests():
    #create the header
    CreateHeader('R5_s1.glm')
    for n in range(len(nodelist)):
         CreateNode(n,'R5_s1.glm')
    for n in range(len(nodelist)):
         CreateLineConfig(n,'R5_s1.glm')
    for n in range(len(nodelist)):        
        CreateLine('R5-12-47-1',n,'R5_s1.glm')
    for n in range(len(nodelist)):        
        CreateMeter('R5-12-47-1',n,'R5_s1.glm')
    for n in range(len(nodelist)):        
        CreateLoad(n,'R5_s1.glm')
        CreateLoad_agg(n,'R5_s1.glm')
    

if __name__ == '__main__':
	_tests()