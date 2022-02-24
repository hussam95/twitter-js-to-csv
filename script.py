import json
import os
import pandas as pd
import numpy as np
import glob

path="/home/hussam/Desktop/twitter_parse/twitter_parse_virtual_env/data"
filenames = glob.glob(path + "/*.js")
for file in filenames:
    with open(file) as read_file:
        data=read_file.read()
        data=data.partition("=")
        data=data[2]
        developer=json.loads(data)

        dic={}  
        prefix=os.path.basename(file).split(".")[0] # getting the .js filename to use as a prefix for every col_name
        #import pdb; pdb.set_trace()
        def parse_json_recursively(json_object):
            if type(json_object) is dict:
                for index,key in enumerate(json_object):                            
                    if type(json_object[key]) is str:
                        if "{}_{}".format(prefix,key) not in dic:
                            dic["{}_{}".format(prefix,key)]=[]
                        if index==0:
                            dic["{}_{}".format(prefix,key)].append(json_object[key])
                        elif "{}_{}".format(prefix,key) in dic:
                            dic["{}_{}".format(prefix,key)].append(json_object[key])                            
                    else:
                        parse_json_recursively(json_object[key])


            elif type(json_object) is list:
                for item in json_object:
                    parse_json_recursively(item)
        #let's feed the json to our recursive function
        parse_json_recursively(developer)
        df=pd.DataFrame(dict([(k,pd.Series(v)) for k,v in dic.items()]))
        os.makedirs("/home/hussam/Desktop/twitter_parse/twitter_parse_virtual_env/csvs", exist_ok=True)
        df.to_csv("/home/hussam/Desktop/twitter_parse/twitter_parse_virtual_env/csvs"+"/"+"{}.csv".format(prefix))