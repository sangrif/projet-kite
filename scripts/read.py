import csv
import numpy as np

# read csv file into array X
fichier = open("../data/validations-sur-le-reseau-ferre-profils-horaires-par-jour-type-1er-sem.csv","r")
fichiercsv = csv.reader(fichier,  delimiter=';')
X = []
count = 0
for row in fichiercsv:
    if(count == 0):
        attributeNames = row
        count = 1
    else:
            X.append(row)

fichier.close()
X = np.array(X)
N=X.shape[0]
M=X.shape[1]



