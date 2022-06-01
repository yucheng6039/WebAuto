import os
path="D:\\jiguang\\Reference Group"
def listdir(path):  #传入存储的list
    dir_list=os.listdir(path)
    dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(path, x)))
    print(dir_list)
    return  dir_list
    # for file in dir_list:
    #     file_path = os.path.join("", file)
    #     if os.path.isdir(file_path):
    #         listdir(file_path, list_name)
    #     else:
    #         list_name.append(file_path)


a=listdir(path)

import pandas as pd


def deal(a):
    # 列表


    # list转dataframe
    df = pd.DataFrame(a, columns=['fluorescent tag'])

    # 保存到本地excel
    df.to_excel("D:\\1激光_allpeakchannel.xlsx", index=False)
deal(a)