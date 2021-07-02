## BERKELEY S.D LABEL READER ##

import json

with open('labelData.json') as images:
    data = json.load(images)

def write_json(data, filename = 'labelData.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent = 4)

def label_category():
    labelCount = 0
    for labels in data['labels']:
        labelCount = labelCount + 1
        print(labels['category'])
    print("Their are " + str(labelCount) + " Labels.")

def Add():
    print("1. Traffic Light")
    print("2. Traffic Sign")
    print("3. Car")
    print("4. Drivable Area")
    print("5. Lane")
    choice = input("\nWhat kind of label would you like to add? ")

    if(choice == str(1)):
        print("Enter box2d Values\n")
        x1 = input("x1: ")
        y1 = input("y1: ")
        x2 = input("x2: ")
        y2 = input("y2: ")

        with open('labelData.json') as json_file:
            data = json.load(json_file)

            temp = data["labels"]

            y = {"category": 'Traffic Light',
                 "box2d": {
                     "x1": x1,
                     "y1": y1,
                     "x2": x2,
                     "y2": y2
                     }
                 }

            temp.append(y)

        write_json(data)
    
    elif(choice == 2):
        print("Enter box2d Values\n")
        x1 = input("x1: ")
        y1 = input("y1: ")
        x2 = input("x2: ")
        y2 = input("y2: ")

        with open('labelData.json') as json_file:
            data = json.load(json_file)

            temp = data["labels"]

            y = {"category": 'Traffic Light',
                 "box2d": {
                     "x1": x1,
                     "y1": y1,
                     "x2": x2,
                     "y2": y2
                     }
                 }

            temp.append(y)

        write_json(data)
    elif(choice == 3):
        print("Enter box2d Values\n")
        x1 = input("x1: ")
        y1 = input("y1: ")
        x2 = input("x2: ")
        y2 = input("y2: ")

        with open('labelData.json') as json_file:
            data = json.load(json_file)

            temp = data["labels"]

            y = {"category": 'Traffic Light',
                 "box2d": {
                     "x1": x1,
                     "y1": y1,
                     "x2": x2,
                     "y2": y2
                     }
                 }

            temp.append(y)

        write_json(data)
    elif(choice == 4):
        print("Enter box2d Values\n")
        x1 = input("x1: ")
        y1 = input("y1: ")
        x2 = input("x2: ")
        y2 = input("y2: ")

        with open('labelData.json') as json_file:
            data = json.load(json_file)

            temp = data["labels"]

            y = {"category": 'Traffic Light',
                 "box2d": {
                     "x1": x1,
                     "y1": y1,
                     "x2": x2,
                     "y2": y2
                     }
                 }

            temp.append(y)

        write_json(data)
    elif(choice == 5):
        print("Enter box2d Values\n")
        x1 = input("x1: ")
        y1 = input("y1: ")
        x2 = input("x2: ")
        y2 = input("y2: ")

        with open('labelData.json') as json_file:
            data = json.load(json_file)

            temp = data["labels"]

            y = {"category": 'Traffic Light',
                 "box2d": {
                     "x1": x1,
                     "y1": y1,
                     "x2": x2,
                     "y2": y2
                     }
                 }

            temp.append(y)

        write_json(data)

def box2d_Data():
    for labels in data['labels']:
        
        if(str(labels['category']) == "lane"):
            continue
        if(str(labels['category']) == "drivable area"):
            continue
        print(labels['box2d'])
        print(list((labels['box2d'].values())))

def box2d_Points(element):
        return list(data['labels'][element]['box2d'].values())

def poly2d_Data():
    for labels in data['labels']:
        if(str(labels['category']) == "drivable area"):
            print(labels['poly2d'])

            
