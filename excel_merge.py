# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import glob




#create DataFrame object of score
all_data = pd.DataFrame()
df = pd.read_excel(r"PATH\a.xlsx")
all_data = all_data.append(df,ignore_index=True)
	
#create DataFrame ibject of gender	
gender = pd.read_excel("gender.xlsx")

#merge grade and score
match = pd.merge(all_data,gender,how="left")

'''
pandas.DataFrame.merge(obja,objb,how="",on=""...)
pandas.DataFrame.to_excel("output.xlsx")

these are very useful functions.

more features will be pushed soon...
'''

#output the merged file
match.to_excel("merged_a.xlsx")