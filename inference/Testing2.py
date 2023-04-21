#from inference import infer
import csv

# with open('input_file.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         print(row)

import pandas as pd
import subprocess
#import elasticsearch 
df = pd.read_csv('input_file2.csv')
#print(df)
for index, row in df.iterrows():
    # Do something with the row data
    print('.\inference\infer.py -q "'+row['QueryString']+'" -rt bm25 t5 -n 5' )
    #cmd = ['python', '.\inference\infer.py -q '+row['QueryString']+' -rt bm25 t5 -n 5']
    #output = subprocess.check_output(cmd)

