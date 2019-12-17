import csv

def readEdges():
    lst = []
    with open("edges.csv", "r") as file:
        txt = file.readlines()
        for line in txt:
            lst.append(line[:-1].split(','))
        return lst

def readVertices():
    lst = []
    with open("vertices.csv", "r") as file:
        txt = file.readlines()
        for line in txt:
            lst.append(line[:-1])
        return lst

def getDistance(v1, v2, lst):
    if v1 == v2:
        return 0
    for line in lst:
        if ((line[0] == v1 and line[1] == v2) or (line[0] == v2 and line[1] == v1)):
            return line[2]
    return "inf"
    
edges = readEdges()
vertices = readVertices()

matrix = []

for i in range(len(vertices)):
    v = []
    for j in range(len(vertices)):
        v.append(getDistance(vertices[i],vertices[j],edges))
    matrix.append(v)

with open("matrix.csv", 'w') as file:
    write = csv.writer(file)
    write.writerows(matrix)

#print(len(matrix[0]))










    
