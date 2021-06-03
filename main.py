#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import pandas as pd
import sys

args = sys.argv

print(args[1])

data = pd.read_csv(args[1], encoding='cp932', header=None)
# print(data)

print("重複業の抽出")
is_duplicated = data.duplicated()
print(is_duplicated)
print(data[is_duplicated])
