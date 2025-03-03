import pandas as pd

snl = pd.read_csv('https://github.com/gdv/foundationsCS/raw/main/students/ex-data/snldb/snl_title.csv')
#print(snl.head())

snl_titlenotnull = snl[snl['title'].notnull()]

snl_titlenotnull.set_index(['sid','eid'], inplace=True)

snl_titlenotnull.sort_index(inplace=True)

selected_rows = snl_titlenotnull.loc[[3, 4]]

print(selected_rows[selected_rows['titleType'] == 'Sketch'])