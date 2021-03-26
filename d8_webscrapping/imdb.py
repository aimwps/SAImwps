import requests
from bs4 import BeautifulSoup
import datetime as dt
import pandas as pd
import numpy as np


# save the website in a variablehttps://www.imdb.com/search/title/?genres=adventure&genres=Adventure&explore=title_type,genres&ref_=adv_explore_rhs"

# save the website in a variable
#western_url = "https://www.imdb.com/search/title/?genres=western&genres=Adventure&explore=title_type,genres&ref_=adv_explore_rhs"
western_url = "https://www.imdb.com/search/title/?genres=western,adventure&sort=user_rating,desc&explore=title_type,genres"
# request url
page = requests.get(url=western_url)

# create a BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

#page title
title = soup.find('title')
#display(title.string)
# data['title'] = title.string


#get duration
dur_container = soup.find_all(class_='lister-item-content')
dur = [title.get_text() for title in dur_container]
dur = [title.split('\n') for title in dur]
#display(dur)
duration = [title[9] for title in dur]
#display(duration)

#get rating
ratings_container = soup.find_all(class_='ratings-bar')
rat = [title.get_text() for title in ratings_container]
rat = [title.split('\n') for title in rat]
rating = [title[3] for title in rat]




#get genre
genre_container = soup.find_all(class_='genre')
gr = [title.get_text() for title in genre_container]
gr = [title.split('\n') for title in gr]
genre = [title[1] for title in gr]



#get titles
titles_container = soup.find_all(class_= "lister-item-header")
# display(titles_container)
titles = [title.get_text() for title in titles_container ] #loop to getText in days_container
# display(titles)
titles = [title.split('\n') for title in titles] #split by \n
# display(titles)
chart_number = [title[1] for title in titles] #split by \n
# display(chart_number)
titles_names = [title[2] for title in titles] #split by \n
# display(titles_names)
published_year = [title[3] for title in titles]
# display(titles)

df = pd.DataFrame({'Chart Number': chart_number,
                    'Title': titles_names,
                    'Published Year': published_year,
                    'Duration': duration,
                    'Genre': genre,
                    'Rating': rating})


#all movies
movie_list = soup.find_all(class_="lister-item-content")

# get list of the links for each actor name for each movie
actor_links_by_movie = [movie.select('a[href*="/name"]') for movie in movie_list]

#Get the text from each link using a nested list comprehension
actor_names_by_movie = [[href_link.get_text() for href_link in movie_list] for movie_list in actor_links_by_movie]

#checks the data before adding to pandas shows the amount of actors named in each movie
for movie in actor_names_by_movie:
    print(f"len: {len(movie)} | {movie}")
print(f"length of actor_names_by movie:{len(actor_names_by_movie)}")







# # for movie in actor_links_by_movie:
# #     print(movie)
#
# movie_ppl = []
# ppl_list = []
# for movie in movie_list:
#     actor_list_for_movie = movie.select('a[href*="/name"]')
#     movie_ppl.append(actor_list_for_movie)
#
# for movie in movie_ppl:
#     just_names = []
#     for ppl in movie:
#         just_names.append(ppl.get_text())
#     ppl_list.append(just_names)
#
#
# # for movie in ppl_list:
# #     print(movie)
#
#
# #span[data-testid="PercentageValue"]')
