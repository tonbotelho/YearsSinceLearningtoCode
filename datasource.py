#-*- coding: utf-8 -*-

# ------------------------------------------------------------------------
# This file is responsable for data files manipulation
# ------------------------------------------------------------------------

# Import system librarys to manipulate the paths
#os and sys = It is used to manipulation

import os
import csv
import sys

#datasource_name = 'lecturer.csv'
datasource_name = 'survey_results_public.csv'

# Ensure multiplatform Mac, Nix, Windows
# Comparing with java
# os.path = System.getProperty("file.separator"), 'c:/dir' or 'c:\dir'
# sys.path[1] = System.getProperty("user.dir"), current app dir
# join is python string method to join lists elements '/'.join( ['c:/dir','subdir','file.ext'] ) - c:/dir/subdir/file.txt
datasource_path = os.path.join(sys.path[1], 'database', datasource_name) # string with p
# print(datasource_path)
datasource_file = open(datasource_path, 'r', encoding="utf8") #open file on read mode

reader = csv.reader(datasource_file, delimiter=',') # reader method of csv library

columns = [10, 11] #columns to read in csv -> YearCoding, YearCodingProf
header = datasource_file.readline() # read a line in file

yearscoding = {} # {'2-5 years': (10, 12%), '0-5': (1, 4%)}
yearscodingprof = {}

limit_iter = 93835  # limit to iterator in loop, descending by 1
limit = 93835  # consult per limit, used for percent calculte

limit_iter_prof = 87259  # limit to iterator in loop, descending by 1
limit_prof = 87259  # consult per limit, used for percent calculte

for r in reader:
    if limit_iter==0:
        break # broken loop
    else:
        i = r[10].replace(' or more years', '').replace(' years', '').split('-')
        if 'NA' in i:
            continue # go to next registry
        if '30' in i:
            i.append(100)
            # NOTe: Created a formule math to organize the years as by order by was not possible.
            # By function the dictionary was reading just the first number and not the number as an integer
            # 0-2 = 2
            # 3-5 = 8
            # 6-8 = 14
            # 9-11 = 20
            # .
            # .
            # 18-20 = 38
            # 24-26 = 50
            # 30 > maior d

        name1 = (sum(list(map(int, i))), r[10])

        if name1 in yearscoding:
            percent = ((yearscoding[name1][0] + 1) * 100)/limit
            yearscoding[name1] = [yearscoding[name1][0] + 1, percent]
        else:
            yearscoding[name1] = [1, 1*100/limit]

        i = r[11].replace(' or more years', '').replace(' years', '').split('-')

        if 'NA' in i:
            continue # go to next registry
        if '30' in i:
            i.append(100)

        name1 = (sum(list(map(int, i))), r[11])
        if name1 in yearscodingprof:
            percent = ((yearscodingprof[name1][0] + 1) * 100)/limit_prof #Still not working
            yearscodingprof[name1] = [yearscodingprof[name1][0] + 1, percent]
        else:
            yearscodingprof[name1] = [1, 1*100/limit_prof] #Still not working

print('\nAll Respondents')
new_dict = {}
for k,v in sorted(yearscoding.items()):
    new_dict[k[1]] = "%.1f"%v[1]
    print("%s %.1f%%"%(str(k[1]), v[1]))
# print (json.dumps(new_dict))

#Still not working
print('\nProfessional Developers')
for k,v in sorted(yearscodingprof.items()):
    print("%s %.1f%%"%(str(k[1]), v[1]) )
