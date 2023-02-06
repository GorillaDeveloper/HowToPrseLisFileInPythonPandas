# step 1
 
import os
 
import pandas as pd

# step 2
 
path = 'data/SymbolsShortLongName'
# step 3
 
files = [f for f in os.listdir(path) if f.endswith('.lis')]
# step 4
 
for file in files:
 
    file_path = os.path.join(path, file)
 
    file_path = file_path.replace("\\", '/' )
# step 5
 
    with open(file_path, 'r') as original:
 
        first_line = original.readline()
 
        if first_line != "symbolic_name|short_name|long_name|":
 
            data = original.read()
 
            with open(file_path, 'w') as modified: modified.write("symbolic_name|short_name|long_name|\n" + data)
# step 6
 
    df = pd.read_csv(file_path, delimiter="|")
 
    df = df.drop(df.columns[-1], axis=1)
 
    df.columns = ['symbolic_name','short_name','long_name']
 
    print(df)