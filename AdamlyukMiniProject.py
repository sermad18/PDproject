#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[5]:



data = pd.read_excel('3-5.xlsx', sheet_name=None)
albums_artists = data['Альбомы'].merge(data['Артисты'], left_on='ID Исполнителя', right_on='ID', suffixes=('_album', '_artist'))
albums_artists_tracks = albums_artists.merge(data['Треки'], left_on='ID_album', right_on='ID альбома')

u2_tracks = albums_artists_tracks.query('Имя == "U2"')

u2_total_cost = u2_tracks['Стоимость'].sum()
print(f"Общая стоимость песен группы U2 составляет {u2_total_cost} рублей.")


# In[9]:


## задача 2 
rolling = albums_artists_tracks[albums_art ists_tracks['Имя'] == 'The Rolling Stones']
bytesroling = rolling['Размер'].sum()
megarolling = int(bytesroling/(1024*1024))
print(megarolling)


# In[20]:


## задача 3 
Cobain = albums_artists_tracks[albums_artists_tracks['Имя'] == 'Nirvana']
Smells = Cobain.groupby('ID альбома')['Длительность'].sum()
dlit = Smells.max()
otvet = dlit/(1000*60)
print(int(otvet))


# In[24]:


## Задача 4 
Peppers = albums_artists_tracks[albums_artists_tracks['Имя'] == 'Red Hot Chili Peppers']
Californ = Peppers.groupby('ID альбома')['Стоимость'].sum()
rockeshnik = Californ.min()
rockeshnik


# In[28]:


## Задача 5 
Queen = albums_artists_tracks[albums_artists_tracks['Имя'] == 'Queen']
King = Queen.groupby('ID альбома')['Размер'].sum()
Grindcore = King.max()
godsaves = int(Grindcore/(1024*1024))
godsaves


# In[29]:


## задача 6 
artists = albums_artists_tracks.groupby('Имя')['Размер'].sum()
obla = artists.max()
megabytes = int(obla/(1024*1024))
megabytes


# In[34]:


## Задача 7 
genres = pd.read_excel('3-5.xlsx', sheet_name='Жанры')
albums_artists_tracks_genres = pd.merge(albums_artists_tracks, genres, left_on='ID жанра', right_on='ID', suffixes=('', '_genre'))
blues = albums_artists_tracks_genres[albums_artists_tracks_genres['Название_genre'] == 'Blues']
artist_costs = blues.groupby('Имя')['Стоимость'].sum()
cheapest_artist_cost = artist_costs.min()
cheapest_artist_name = artist_costs.idxmin()
print(cheapest_artist_name , cheapest_artist_cost)


# In[36]:


import matplotlib.pyplot as mp 


# In[46]:


## Задача 8 
genre_money = albums_artists_tracks_genres.groupby('Название_genre')['Стоимость'].sum()
mp.figure(figsize = (15, 10))
mp.bar(genre_money.index , genre_money.values)
mp.xlabel('Жанры')
mp.ylabel('Суммарная стоимость песен')
mp.xticks(rotation = 60)
mp.show()


# In[ ]:




