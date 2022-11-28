#Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
import numpy as np 
import genes# importing different geneome sequence from genes file

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
    percentage = ((G_count + C_count) / total_nucleotides)*100
    print("The Percentage of CYTOSINE & GUANINE (GC) in The Given Deoxyribonucleic acid (DNA) Sequence is",percentage )



geneome= '''ATGTACTCATTCGTTTCGGAAGAGACAGGTACGTTAATAGTTAATAGCGTACTTCTTTTTCTTGCTTTCGTGGTATTCTTGCTAGTTACACTAGCCATCCTTACTGCGCTTCGATTGTGTGCGTACTGCTGCAATATTGTTAACGTGAGTCTTGTAAAACCTTCTTTTTACGTTTACTCTCGTGTTAAAAATCTGAATTCTTCTAGAGTTCCTGATCTTCTGGTCTAA'''

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

















