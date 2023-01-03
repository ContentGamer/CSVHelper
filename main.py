import json
import os

# author: ContentGamer

seperator = os.path.abspath(__file__).split("\\")
folderPATH = ""
for i, v in enumerate(seperator):
    if(i != seperator.__len__()-1):
        if(i == 0):
            folderPATH += v
        else:
            folderPATH += "\\"+v


directory = f"{folderPATH}\\project.json"
file = open(directory)
data = json.load(file)
cvsData = []
createdItems = 0

def createNew(firstname, lastname):
    global createdItems
    global cvsData
    createdItems = createdItems+1
    output = {
        "id": createdItems,
        "firstname": firstname,
        "lastname": lastname
    }
    outputJSONFile = {
        "csv": data["csv"]
    }
    outputJSONFile["csv"].append(output)
    cvsData = outputJSONFile["csv"]
    with open(directory, 'w') as outfile:
        json.dump(outputJSONFile, outfile, indent=4)

def clearCSV():
    outputJSONFile = {
        "csv": []
    }
    cvsData.clear()
    data["csv"].clear()
    with open(directory, 'w') as outfile:
        json.dump(outputJSONFile, outfile, indent=4)

def getCSVDataAsArray():
    result = []
    for i,v in enumerate(data["csv"]):
        result.append("ID: " + str(v["id"]) + "; FIRST_NAME: "+ v["firstname"] + "; LAST_NAME: " + v["lastname"] + ";")
    return result

def getCSVData():
    return cvsData

clearCSV()