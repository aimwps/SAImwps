

# save the website in a variable
#western_url = "https://www.imdb.com/search/title/?genres=western&genres=Adventure&explore=title_type,genres&ref_=adv_explore_rhs"
western_url = "https://www.imdb.com/search/title/?genres=western,adventure&sort=user_rating,desc&explore=title_type,genres"
# request url
page = requests.get(url=western_url)

# create a BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

#page title
title = soup.find('title')
display(title.string)
# data['title'] = title.string

#release date
date_container = soup.find_all(class_='lister-item-year text-muted unbold')
d = [title.get_text() for title in date_container]
d = [title.split('\n') for title in d]
#display(d)
date = [title[0] for title in d]





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
# display(title)
chart_number = [title[1] for title in titles] #split by \n
# display(chart_number)
titles_names = [title[2] for title in titles] #split by \n
# display(titles_names)

#duration
duration_area = [movie.find('p', class_="text-muted") for movie in movie_list]
durations= []
for d in duration_area:
    duration = d.find('span', class_="runtime")
    if duration == None:
        durations.append("NaN")
    else:
         durations.append(duration.get_text()[0:2])


#all movies
movie_list = soup.find_all(class_="lister-item-content")
# get list of the links for each actor name for each movie
actor_links_by_movie = [movie.select('a[href*="/name"]') for movie in movie_list]
#Get the text from each link using a nested list comprehension
actor_names_by_movie = [[href_link.get_text() for href_link in movie_list] for movie_list in actor_links_by_movie]
director = [movie_director[0] for movie_director in actor_names_by_movie]
actors = [", ".join(actors[1:]) for actors in actor_names_by_movie]



df = pd.DataFrame({'Chart Number': chart_number,
                    'Title': titles_names,
                    'Release Date': date,
                    'Duration': durations,
                    'Genre': genre,
                    'Rating': rating,
                    'Director': director,
                    'Actors': actors})
df
