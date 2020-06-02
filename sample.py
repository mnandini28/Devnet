import xmltodict
import json
import yaml
with open('sample.json', 'r') as jsonData:
    pythonDictData = json.load(jsonData)

with open('sample.yaml', 'w') as sampleFile:
    yamlData = yaml.dump(pythonDictData, sampleFile)
with open('sample.xml', 'w') as sampleFile:
    sampleFile.write(xmltodict.unparse(pythonDictData))