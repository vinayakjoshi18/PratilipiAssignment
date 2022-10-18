import pandas as pd
import numpy as np

md_df = pd.read_csv('./metadata.csv')

md_ids = md_df["pratilipi_id"].to_numpy() 
md_cn = md_df["category_name"].to_numpy()
md_rt = md_df["reading_time"].to_numpy()
md_ud = md_df["updated_at"].to_numpy()
md_pd = md_df["published_at"].to_numpy()
md_aids = md_df["author_id"].to_numpy()

u_ids = list(set(md_ids))
u_cn = []
u_rt = []
u_ud = []
u_pd = []
temp_cat = []

temp_inside = []

u_id_ct_2 = []
for unique_id in u_ids:
  for i in range(len(md_ids)):
    if(md_ids[i] == unique_id):
      temp_aids = md_aids[i] 
      temp_rt = md_rt[i]
      temp_ud = md_ud[i]
      temp_pd = md_pd[i]
      if(md_cn[i] not in temp_cat):
        temp_cat.append(md_cn[i])
  my_string = ';'.join(temp_cat)
  temp_inside.append(unique_id)
  temp_inside.append(my_string)
  temp_inside.append(temp_aids)
  temp_inside.append(temp_rt)
  temp_inside.append(temp_ud)
  temp_inside.append(temp_pd)
  u_id_ct_2.append(temp_inside)
  temp_inside.clear()
  temp_cat.clear()
print(len(u_id_ct_2))

l0 = []
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []

for i in range(len(u_ids)):
  l0.append(u_id_ct_2[i][0])
  l1.append(u_id_ct_2[i][1])
  l2.append(u_id_ct_2[i][2])
  l3.append(u_id_ct_2[i][3])
  l4.append(u_id_ct_2[i][4])
  l5.append(u_id_ct_2[i][5])

df = pd.DataFrame()
df['author_id'] = l2
df['pratilipi_id'] = l0
df['category_names'] = l1
df['reading_time'] = l3
df['updated_at'] = l4
df['published_at'] = l5

df.to_csv("merged_rows.csv")
