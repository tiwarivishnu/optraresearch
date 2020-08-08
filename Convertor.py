import json
from pathlib import Path

strInput = Path('C:/aPythonClass/Input.json').read_text()
InputMessage = json.loads(strInput)

#func1 to extract the list of results from "callExpDateMap"
def __GetData(data):
    testlist = []
    for key,value in data.items():
        #print (str(key)+'->'+str(value))
        testlist.append(value)
    #print(testlist[0])
    return testlist

mylist = []
mylist = __GetData(InputMessage["callExpDateMap"])
#print(mylist)

#func2 is to get list of results without date and strike price keys.
# Please note that date and strike price are recorded in the Option record set.
def __GetOptionsArray(data):
    dict1 = {}
    optionslist2 = []
    for i in data:
        dict1.update(i)
        values_view = dict1.values()
        value_iterator = iter(values_view)
        first_value = next(value_iterator)
        optionslist2.append(first_value)
    json_string = json.dumps(optionslist2)

    #print(json_string)
    return  json_string


#func3 will get the basic details (line 1 to 13) about the Symbol
def __GetHeaderRecord( data ):
    dict1 = {}
    for key, value in data.items():
        if type(value) != type(dict()):
        # print (str(key)+'->'+str(value))
            dict1[str(key)] = str(value)

        json_data = json.dumps(dict1)
    #print(json_data)
    return json_data

#here we combine the dictionary and list and create the final JSON.

#Get header record (line 1 to 13)
header = json.loads(__GetHeaderRecord(InputMessage))

#Get the Options record
optionsArray = json.loads(__GetOptionsArray(mylist))

#Merge the dictionary and list and create final JSON
finalJSON = []
finalJSON.append(header)
finalJSON.append(optionsArray)
json_final = json.dumps(finalJSON)

print(json_final)







