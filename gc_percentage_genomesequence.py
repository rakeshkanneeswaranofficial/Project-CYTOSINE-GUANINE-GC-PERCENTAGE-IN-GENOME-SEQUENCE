#Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome

import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt



import genome_sequences# importing different geneome sequence and user defined functions from genes file

#FUNCTION DECALARATION FOR :

#To take genome sequence of DNA from user as string and convert it to list
def gene_sequence(sequence):
    g_list = list(sequence)
    return g_list
    

#To convert genome sequence of DNA  to array structure
def gene_sequence_list(gene_sequence):
    g_array = np.array(gene_sequence)
    return g_array 

def GC_percentage(G_count,C_count,total_numclitoties):
    percentage = round(((G_count + C_count) / total_nucleotides)*100,2)
    print("The Percentage of CYTOSINE & GUANINE (GC) in The Given Deoxyribonucleic acid (DNA) Sequence is",percentage,'%' )
    print("Your Graph representing GC Percentage of CYTOSINE & GUANINE (GC) in The Given Deoxyribonucleic acid (DNA) Sequence is successfully plotted")


genome_sequences.welcome()
genome_sequences.select_gene()


sr = int(input("ENTER THE SR. NO"))

value = genome_sequences.enter_sr(sr)
geneome= genome_sequences.gene_selected(value)
title3 = genome_sequences.title(sr)

Gene_list = gene_sequence(geneome)
Gene_array = gene_sequence_list(Gene_list)
total_nucleotides = len(Gene_array)

#eval(input("Enter the geneome sequence of DNA"))   

total_nucleotides = len(Gene_array)
g_count = 0 
c_count = 0
for g in range(0,total_nucleotides):
    if Gene_array[g] == 'G':
        g_count = g_count+1

for c in range(0,total_nucleotides):
    if Gene_array[c] == 'C':
        c_count = c_count+1        

GC_percentage(g_count,c_count,total_nucleotides)  
percentage1 = int(((g_count + c_count) / (total_nucleotides))*100)

list_X=[]
list_Y=[]

for a in range (percentage1):
    list_X.append(a)
for a in range (percentage1):
    list_Y.append(a) 
'''ax = plt.axes(projection = '3d')'''
'''ax.plot3D(list_X, list_Y,list_X,color='green')'''
plt.bar(list_X, list_Y, color='red',linewidth=6)
plt.axis([0,100,0,100]) 
plt.xlabel('CYTOSINE & GUANINE(GC) PERCENTAGE IN DNA SEQUENCE',fontsize = 18)
plt.ylabel('TOTAL CYTOSINE & GUANINE(GC) PERCENTAGE', fontsize = 18)
plt.legend("PECRENTAGE")
plt.title("The Percentage of CYTOSINE & GUANINE (GC) in The Given Deoxyribonucleic acid (DNA) Sequence",fontsize = 18)

plt.show()












