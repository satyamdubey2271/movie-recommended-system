
import streamlit as st
import pickle
import pandas as pd
import numpy as np

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

with open('similarity_parts1.pkl','rb') as f:
  parts1 = pickle.load(f)

with open('similarity_parts2.pkl','rb') as f:
  parts2 = pickle.load(f)

with open('similarity_parts1.pkl','rb') as f:
  parts3 = pickle.load(f)

with open('similarity_parts1.pkl','rb') as f:
  parts4 = pickle.load(f)

with open('similarity_parts1.pkl','rb') as f:
  parts5 = pickle.load(f)

with open('similarity_parts1.pkl','rb') as f:
  parts6 = pickle.load(f)
similarity = np.concatenate((parts1,parts2))

def recommend(movie):
  movie_index = new_df[new_df['title']== movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  return movies.iloc[[i[0] for i in movies_list]].title

  st.title("movie recommender system")

  option = st.selectbox("pick a movie:",movies['title].values)

  if st.button('recommend'):
    for name in recommend(option):
      st.write(name)
