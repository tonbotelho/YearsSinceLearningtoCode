#-*- coding: utf-8 -*-

# ------------------------------------------------------------------------
# This file is responsable for data files manipulation
# ------------------------------------------------------------------------

# Import system librarys to manipulate the paths
#os and sys = It is used to manipulation

import os
import csv
import sys
import pandas as pd

datasource_name = 'lecturer.csv'
datasource_path = os.path.join(sys.path[1], 'database', datasource_name)
print(datasource_path)
datasource_file = open(datasource_path, 'r', encoding="utf8") #open file on read mode
datasource_file.readline()
reader = csv.reader(datasource_file, delimiter=',')
columns = [0,5,6]
for r in reader:
    print([r[i] for i in columns])
