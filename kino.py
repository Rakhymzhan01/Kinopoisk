import requests

def search_movie(title, api_key):
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data


def extract_movie_info(movie_data):
    if movie_data['Response'] == 'True':
        title = movie_data['Title']
        year = movie_data['Year']
        genre = movie_data['Genre']
        director = movie_data['Director']
        actors = movie_data['Actors']
        plot = movie_data['Plot']
        poster_url = movie_data['Poster']

        return {
            'Title': title,
            'Year': year,
            'Genre': genre,
            'Director': director,
            'Actors': actors,
            'Plot': plot,
            'Poster': poster_url
        }
    else:
        print("Movie not found or error occurred.")
        return None


api_key = '711716bd'
movie_title = 'The Matrix'
movie_data = search_movie(movie_title, api_key)

movie_info = extract_movie_info(movie_data)

if movie_info:
    print("Title:", movie_info['Title'])
    print("Year:", movie_info['Year'])
    print("Genre:", movie_info['Genre'])
    print("Director:", movie_info['Director'])
    print("Actors:", movie_info['Actors'])
    print("Plot:", movie_info['Plot'])
    print("Poster URL:", movie_info['Poster'])
