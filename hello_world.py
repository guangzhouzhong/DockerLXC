#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import json
#data=np.random.randint(1,100,200)
#data=pd.DataFrame(data)
#data.to_csv("../tcdata/num_list.csv",index=False,header=False)
data=pd.read_csv("/tcdata/num_list.csv",header=None)#天池python镜像默认包含此文件，自己测试用如下指令
#data=pd.read_csv("../tcdata/num_list.csv",header=None)

#第一题
result_1="Hello world"
#第二题
result_2=0
for i,num in enumerate(data[0]):
    result_2+=num
#第三题
data.sort_values(by=0,ascending=False,inplace=True)
result_3=data[0][:10]
result_3=list(result_3)

result={"Q1":result_1,
        "Q2":result_2,
        "Q3":result_3
       }
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)