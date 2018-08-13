import json
data = {
    'name' : 'JSON File',
    'Is it Cool ?': "Yes" ,
    'price' : '1254673269870'
}
json_str = json.dumps(data)
data = json.loads(json_str)
with open('JSON_File.json', 'w') as file:
    json.dump(data, file)
file.close()
with open('JSON_File.json', 'r') as file1:
    dat = json.load(file1)
    print(dat)
file1.close()
