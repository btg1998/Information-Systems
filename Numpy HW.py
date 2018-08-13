# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 05:23:46 2017

@author: bharg
"""
import sys
import numpy as np
sub=['sub1','sub2','sub3','sub4','sub5','sub6']
stud=['stud1','stud2','stud3','stud4','stud5','stud6','stud7','stud8','stud9','stud10']
S=np.array(sub)
St=np.array(stud)
M=np.random.rand(10,6)
M=M*100
M=np.around(M,2)
print(M)
ch=int(input("Enter Choice:\n 1-Students with highest and lowest total marks\n 2-Subjects with highest and lowest Average Score\n 3-Student with highest score across all subjects"))
if ch==1:
    TM=np.zeros(10)
    TM=M.sum(axis=1)
    max1=max(TM)
    min2=min(TM)
    print("\nStudent(s) with lowest total marks: ")
    i=0
    while i<10:
        if max1==TM[i]:
            print(St[i])
        i=i+1
    print("\nStudent(s) with lowest total marks: ")
    i=0
    while i<10:
        if min2==TM[i]:
            print(St[i])
        i=i+1
elif ch==2:
    TMS=np.zeros(6)
    TMS=M.sum(axis=0)
    print("Subjects with Highest and Lowest Average Scores: \nHighest: "+str(S[np.argmax(TMS)])+" \nLowest: "+str(S[np.argmin(TMS)]))
elif ch==3:
    i=np.argmax(M)
    print("Info. about the student with the highest marks across all subjects: ")
    print(i)
    print(M[i/6][i%6])
    print("Name: "+St[i/6]+" in subject: "+S[i%6])
else:
    print("Invalid Choice...Exiting...")
    sys.exit(0)
