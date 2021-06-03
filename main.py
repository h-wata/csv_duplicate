#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import pandas as pd
import glob

csv_files = glob.glob("./*.csv")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

for csv_file in csv_files: 
    print("File Name : {}".format(csv_file))
    data = pd.read_csv(csv_file, encoding='cp932', header=None)

    print("重複業の抽出を実行します")
    is_duplicated = data.duplicated(subset=[0, 1, 3, 5, 7, 8, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
    print(data[is_duplicated])

var = input("Please Input Enter")