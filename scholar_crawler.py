#-*- coding: utf-8 -*-

import scholarly
import json


def gscholar_craw(file_name):
    search_query = scholarly.search_pubs_query(file_name)
    with open('./gs_data/'+file_name + '.txt', 'w') as f:
        for i in range(0, 200):
            temp = next(search_query)
            dict = temp.bib
            json.dump(dict, f)
            f.write('\n')
    f.close()


