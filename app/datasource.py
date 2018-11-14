#-*- coding: utf-8 -*-

# ------------------------------------------------------------------------
# This file is responsable for data files manipulation
# ------------------------------------------------------------------------

# Import system librarys to manipulate the paths
#os and sys = It is used to manipulation

import os
import csv
import sys
from itertools import count


def setup(column, num_rows): #function set up
    """
    :param column: column csv number 10, number 11, ...
    :param num_rows: number of rows of csv file
    :param iter_limit: number of rows  of csv file descending on iterator
    :return: dict
    """

    datasource_name = 'survey_results_public.csv'

    # Ensure multiplatform Mac, Nix, Windows
    # Comparing with java
    # os.path = System.getProperty("file.separator"), 'c:/dir' or 'c:\dir'
    # sys.path[1] = System.getProperty("user.dir"), current app dir
    # join is python string method to join lists elements '/'.join( ['c:/dir','subdir','file.ext'] ) - c:/dir/subdir/file.txt
    datasource_path = os.path.join(sys.path[1], 'database', datasource_name)  # string with p
    # print(datasource_path)
    datasource_file = open(datasource_path, 'r', encoding="utf8")  # open file on read mode
    header = datasource_file.readline()  # To avoid get headers

    datasource = {}
    iter_limit = num_rows  # iter_limit establish a limit to iterate in rows,
    # iter_limit is rows limit than descending with loop
    reader = csv.reader(datasource_file, delimiter=',')  # reader method of csv library

    for r in reader:  # iterate the reader

        if iter_limit == 0:  # if iteration limit is zero then break the loop
            break
        else:  # processing...
            # NOTE: replace search a sentence and replace to anyway, replace return a new string

            i = r[column].replace(' or more years', '').replace(' years', '').split('-') # split function slice the new string
            if 'NA' in i:  # NOT AVAILABLE, so nothing to do
                continue  # go to next registry
            if '30' in i:  # if 30 or more years, so aggregate a value to high the index 30+100 = 130
                i.append(100)
                # NOTE: Created a math formule to organize the years by order. The data taken from csv was a string,
                # and it was not possible to sort.
                # By function the dictionary was reading just the first number and not the number as an integer
                # 0-2 = 2 pass to be a number and not a string
                # 3-5 = 8
                # 6-8 = 14
                # 9-11 = 20
                # .
                # .
                # 18-20 = 38
                # 24-26 = 50
                # 30 > much d
            # map references: http://book.pythontips.com/en/latest/map_filter.html

            name1 = (sum(list(map(int, i))), r[column])  # combine building functions to create index
            #var = sum a list and declare that i is an int.

            # Use the pool three
            # https://www.portaleducacao.com.br/conteudo/artigos/contabilidade/calculos-de-porcentagens-utilizando-regra-de-tres/66995

            if name1 in datasource:
                percent = ((datasource[name1][0] + 1) * 100) / num_rows
                datasource[name1] = [datasource[name1][0] + 1, percent]
            else:
                datasource[name1] = [1, 1 * 100 / num_rows]


        iter_limit = iter_limit -1 #
    datasource_file.close()

    return datasource


def create_datasource(template, datasource1, delimiter1, datasource2, delimiter2):
    """create a file html format
    path - path to json file
    datasource - dict to be manipulated
    """
    import json
    # Code: Read the Base.html and store in an variable call aux)
    path = os.path.join(sys.path[1], 'templates', template)
    base_file = open( path, 'r' ) # open the base.html
    template_file = base_file.read()
    base_file.close()

    #  Creating a dictionary to store the rows of 10 column
    new_dict = {}
    for k, value in sorted(datasource1.items()):
        new_dict[k[1]] = "%.1f" % value[1]
    template_file = template_file.replace(delimiter1, json.dumps(new_dict))


    #  Creating a dictionary to store the rows of 11 column
    new_dict = {}
    for k, value in sorted(datasource2.items()): # organizing for desc order
        # 10.2389499 -> %.2f -> 10.20 -- %.1f --> 10.2
        new_dict[k[1]] = "%.1f" % value[1]
    template_file = template_file.replace(delimiter2, json.dumps(new_dict))

    path = os.path.join(sys.path[1], 'templates', 'index.html') #creating index.html in order to do not lost the reference of delimiter
    html_file = open(path, 'w') # creating file index. It is the compilated file (with the data that will be displayed on the screen)
    html_file.write(template_file) # writing into index.file
    html_file.flush() # commit insertion
    html_file.close() #close the file

# This data is used to calc the percentage
datasource2 = setup(column=11, num_rows=77903)
# print(datasource2)
datasource1 = setup(column=10, num_rows=93835)
# print(datasource1)

# creating the index file using the base.html as template
create_datasource(template="base.html"
                  , datasource1=datasource1
                  , delimiter1='{%years_coding_data%}'
                  , datasource2=datasource2
                  , delimiter2='{%years_coding_prof_data%}')