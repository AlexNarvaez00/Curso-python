#Lectura de artivos

# DOC https://docs.python.org/3/library/io.html

from io import open

CSV = open('LANGUAGE.csv','r',encoding="ANSI")
linesCSV = CSV.readlines()

for line in linesCSV:
    print(line.replace('\n','')) 

CSV.close()
#Video 37