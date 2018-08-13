import BTG
import sys
Data=[]
DI={}
(Data,DI)=BTG.AP.accept_input(Data,DI)
(Data,DI)=BTG.DP.do_processing(Data,DI)
(Data,DI)=BTG.QE.query_execute(Data,DI)
sys.exit(0)
