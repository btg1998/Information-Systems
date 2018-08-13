import csv
import json
import sys
from operator import itemgetter

def do_processing(Data,DI):
    for i in Data:
        dit={"Name":i[0],"SG1":float(i[3]),"SG2":float(i[4]),"SG3":float(i[5]),"SG4":float(i[6]),"CG":float(i[7])}
        DI[i[1]]=dit
    json_str = json.dumps(DI)
    data = json.loads(json_str)
    with open('JSON_File.json', 'w') as f:
        json.dump(data, f)
    f.close()
    return (Data,DI)
