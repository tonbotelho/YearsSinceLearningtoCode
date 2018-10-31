#-*- coding: utf-8 -*-

# ------------------------------------------------------------------------
# This file is responsable for data files manipulation
# ------------------------------------------------------------------------

# Import system librarys to manipulate the paths
#os and sys = It is used to envirement manipulation

import os, sys

datasource_name = 'survey_results_public.csv'
# In Java
# System.getProperty("user.dir") -> sys.path[1]
# System.getProperty("file.separator") -> os.path
# join has the responsability to concat strings of a list
# join put the file separator between each comma of the list
datasource_path = os.path.join(sys.path[1], 'database', datasource_name)
# print(datasource_path)

con = open(datasource_path , 'r')

test = con.readline().split(',')
# Arrange this csv into an dictionary based on ID so it can be handled.
for i,t in enumerate(test):
    print("%d, %s"%(i,t))


# HTTP used to catch data for google grafics