#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:data_lib.py
# @Time    :2020/7/22 16:26
# @Author  :Harry
import csv

def read_csv(file_name):
    data_list=[]
    with open(file_name,"r+",encoding="utf-8") as f:
        data = csv.reader(f)
        print(data)
        for d in data:
            print("d->",d)
            data_list.append(d[0])
    return data_list

# data = read_csv()
# print(data)