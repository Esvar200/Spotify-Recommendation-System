import pandas as pd
import numpy as np
import pickle
df = pd.read_csv(r"E:\ML\dataset.csv")
df.drop(df.columns[[0,1,3,6,7,8,2,10,11,12,13,14,15,16,17,18,19,20]], axis=1, inplace=True)
df = df.drop_duplicates(subset = "track_name")
df['popularity'] = df['popularity'].astype('object')
df['data'] = df[df.columns[0:]].apply(lambda x: ' '.
                join(x.dropna().astype(str)),axis = 1)
from sklearn.feature_extraction.text import CountVectorizer
v = CountVectorizer()
v = v.fit_transform(df.iloc[:8000,-1])
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(v)
df2 = pd.DataFrame(similarity, columns=df.iloc[:8000,0],index=df.iloc[:8000,0])
r = pd.DataFrame(df2.nlargest(6,'Comedy').index)
r = r[r['track_name'] != 'Comedy']

df2.to_csv("out.csv")
