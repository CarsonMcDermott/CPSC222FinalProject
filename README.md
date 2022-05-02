### CPSC222 
### Final Project
### Jaylene Baltazar, Carson McDermott
### May 2022

This is our final project! We have chosen to analyze our spotify data, this spans from 06/26/21 to 01/29/22. In total, we have 32 weeks worth of data. 
Our project starts out with some simple stats regarding our data set. One of these attributes that we took interest in was the top 15 artists. We used the spotify API from class to determine what genre they were from. 

Data cleaning was perfromed to organize the days into weeks and a .groupby was on artistName to get the percentage of pop per week. (to be used in hypothesis testing 1)

Both Carson and I have bar and pie charts to visualize our top artists by number of streams and also by most popular genre, respectively.

For hypothesis tests, we started by looking at our individual data, then both of them combined. 

Our kNN classifier takes in the length of a song (in milliseconds) from our data and predict the artist it's mostlikely to belong to and also the genre that goes along with it. 