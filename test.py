#-*- coding: utf-8 -*-

import scholarly
import json

import optparse

import os
import sys
import re

# print(next(scholarly.search_author('Steven A. Cholewiak')))

# search_query = scholarly.search_pubs_query('Big data')


file_name = 'large scale data mining'
search_query = scholarly.search_pubs_query(file_name)



with open(file_name + '.txt', 'a') as f:
    for i in range(0, 200):
        temp = next(search_query)

        dict = temp.bib
        json.dump(dict, f)
        f.write('\n')

f.close()

print("it is done")





# if __name__ == "__main__":
#   print_query('Decision making')




# get_financial_statements('035720')
