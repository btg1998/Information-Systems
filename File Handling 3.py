f = open('P.txt','w')
data = "Test File Data"
f.write(data)
f.close()
f = open('P.txt','r')
g = f.read()
print (g)
f.close()
