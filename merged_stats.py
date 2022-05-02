##########################################

import pandas as pd
import numpy as np

# First let's import the data
json_df = pd.read_csv("merged_StreamingHistory.csv")

# Now to compute stats!

# Average Listen Time Per Song
song_arr = json_df["msPlayed"]
song_count = 0
length_total = 0
for lengths in song_arr:
    song_count += 1
    length_total += lengths
avg_listen_time_ms = length_total / song_count
avg_listen_time_minutes = avg_listen_time_ms / 60000 #since there are 60,000 milliseconds in a minute!
# print("Average Listen Time Per Song (in minutes):", avg_listen_time_minutes)

# Longest Song
longest_song_ms = json_df["msPlayed"].max()
longest_song_data = json_df.loc[json_df["msPlayed"] == longest_song_ms]
print("Longest Song Listen Time Data:", longest_song_data)
# I know this song isnt actually the longest, as a I know this is only 5 minute song, and
# there are other songs nearing 9 minutes. I think it tracked this song for longer than 9 minutes due to 
# it possibly being replayed mid-song (AKA I replayed the song before it actually ended).

# Shortest Song
shortest_song_ms = json_df["msPlayed"].min()
shortest_song_data = json_df.loc[json_df["msPlayed"] == shortest_song_ms]
print("Shortest Song Listen Time Data:", shortest_song_data)
# the reason why there are so many of these is due to the fact of me skipping over a number of songs at once
# for example, I would listen to a "spotify radio" for so long it would turn to songs I didnt know, so I would imediately skip them.

# Average Letters Per Song Title
track_arr = json_df["trackName"]
title_count = 0
total_letters = 0
for titles in track_arr:
    title_count += 1
    for letters in titles:
        total_letters += 1
avg_letters_per_title = total_letters / title_count
print("Average Letters Per Song Title:", avg_letters_per_title)

# Average Letters per Artist Name
artist_arr = json_df["artistName"]
artist_count = 0
total_letters = 0
for artist in artist_arr:
    artist_count += 1
    for letters in artist:
        total_letters += 1
avg_letters_per_artist = total_letters / title_count
print("Average Letters Per Artist Name:", avg_letters_per_artist)

# Top Artists
top_15_artists = artist_arr.value_counts().head(15)
print("My Top 15 Spotify Artists Based Off Songs Listened To:")
print(top_15_artists)