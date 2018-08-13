# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 05:23:46 2017

@author: bharg
"""
import sys
import numpy as np
sub=[]
print("Enter the 6 Subjects: ")
for i in range(6):
    sub.append(input())
print("Enter the name of the 10 students: ")
stud=[]
for i in range(10):
    stud.append(input())
S=np.array(sub)
St=np.array(stud)
M=np.random.rand(10,6)
M=M*100
M=np.around(M,2)
print(M)
ch=int(input("Enter Choice:\n 1-Students with highest and lowest total marks\n 2-Subjects with highest and lowest Average Squares\n 3-Student with highest score across all subjects"))
if ch==1:
    max1=0
    ma=0
    min2=600
    mi=0
    Sum=[]
    for i in range(10):
       t=M[i].sum()
       Sum.append(t)
       if t>=max1:
           max1=t
           ma=i
       if t<=min2:
           min2=t
           mi=i
    print("\nStudents with highest total marks: ")
    i=0
    while i<10:
        if max1==Sum[i]:
            print(St[i])
        i=i+1
    print("\nStudents with lowest total marks: ")
    i=0
    while i<10:
        if min2==Sum[i]:
            print(St[i])
        i=i+1
    
    
elif ch==2:
    max1=0
    ma=0
    min2=100
    mi=0
    for i in range(6):
       t=M[:,i].sum()
       t=t/10
       if t>=max1:
           max1=t
           ma=i
       if t<=min2:
           min2=t
           mi=i
    print("Highest: "+str(S[ma])+" Lowest: "+str(S[mi]))
elif ch==3:
    i=0
    for i in range(6):
        print("Highest in "+str(S[i])+" is: "+str(St[M[:,i].argmax()]))
else:
    print("Invalid Choice...Exiting...")
    sys.exit(0)
    
    
