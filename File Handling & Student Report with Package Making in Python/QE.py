import csv
import json
import sys
from operator import itemgetter

def query_execute(Data,DI):
    f = open('Queries.txt','w')
    f.write("\n")
    f.close()
    f = open('Queries.txt','a')
    f.write("Start of Program Run\n\n")
    f.write("Text File containing Query No. and their result: \n\n")
    q=0
    for i in range(len(Data)):
        for j in range(3,8):
            Data[i][j]=float(Data[i][j])
    while(True):
        try:
            i=int(input("Enter your choice: \n1-finding topper overall and semsesterwise \n2-Weak Category Students \n3-c)Sorting the student list as per CGPA\n"))
        except:
            print("Invalid Choice. Exiting...")
            sys.exit(0)
        if i==1:
            q=q+1
            s1=0
            max1=0
            s2=0
            max2=0
            s3=0
            max3=0
            s4=0
            max4=0
            cg=0
            max5=0
            for i in range(len(Data)):
                if(Data[i][3]>max1):
                    max1=Data[i][3]
                    s1=i
                if(Data[i][4]>max2):
                    max2=Data[i][4]
                    s2=i
                if(Data[i][5]>max3):
                    max3=Data[i][5]
                    s3=i
                if(Data[i][6]>max4):
                    max4=Data[i][6]
                    s4=i
                if(Data[i][7]>max5):
                    max5=Data[i][7]
                    cg=i
            f.write("Query No. "+str(q))
            f.write('\n')
            f.write("Sem1 Topper: "+str(Data[s1][0])+"\nSem2 Topper: "+str(Data[s2][0])+"\nSem3 Topper: "+str(Data[s3][0])+"\nSem4 Topper: "+str(Data[s4][0])+"\nOverall Topper: "+str(Data[cg][0])+"\n")
            print("Sem1 Topper: ",Data[s1][0]," Sem2 Topper: ",Data[s2][0]," Sem3 Topper: ",Data[s3][0]," Sem4 Topper: ",Data[s4][0]," Overall Topper: ",Data[cg][0])
        elif i==2:
            wc=[]
            q=q+1
            for i in range(len(Data)):
                if Data[i][7]<6.0:
                    wc.append(Data[i][0])
            f.write("Query No. "+str(q))
            f.write('\n')
            f.write("The Weak Students are: \n")
            for i in wc:
                f.write(str(i))
                f.write("\n")
            print("The Weak Students are: ",wc)
        elif i==3:
            q=q+1
            f.write("Query No. "+str(q))
            f.write('\n')
            f.write("Sorted Data: \n")
            list1=sorted(Data, key=itemgetter(7),reverse=True)
            for i in list1:
                f.write("Name: "+str(i[0])+" Roll No. : "+str(i[1])+" Hall: "+str(i[2])+" SG1: "+str(i[3])+" SG2: "+str(i[4])+" SG3: "+str(i[5])+" SG4: "+str(i[6])+" CG: "+str(i[7]))
                f.write("\n")
            print("Sorted Data: ")
            for z in list1:
                print(z)
        f.write('\n')
        n = raw_input("Please enter y to quit or any other charecter to continue: ")
        if n.strip() == 'y':
            f.write("End of Program Run.\n")
            f.close()
            break
    return (Data,DI)
