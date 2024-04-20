from bs4 import BeautifulSoup
import requests
import json
import os


def scrape_imdb_movies():
    try:
        source = requests.get('https://www.imdb.com/list/ls055592025/')
        source.raise_for_status()

        soup = BeautifulSoup(source.text, 'lxml')
        movies = soup.find_all('div', class_="lister-item-content")

        movie_list = []

        for movie in movies:
            header = movie.find('h3', class_="lister-item-header")
            title_anchor = header.find_all('a')[0]
            title = title_anchor.text.strip() if title_anchor else 'N/A'

            year_span = header.find('span', class_="lister-item-year text-muted unbold")
            year = year_span.text.strip('()') if year_span else 'N/A'

            duration_span = movie.find('span', class_="runtime")
            duration = duration_span.text.strip() if duration_span else 'N/A'

            genre_span = movie.find('span', class_="genre")
            genre = genre_span.text.strip() if genre_span else 'N/A'

            image_div = movie.find_previous_sibling('div', class_="lister-item-image ribbonize")
            image_tag = image_div.find('img')['loadlate'] if image_div else 'N/A'

            plot = movie.find_all('p')[1].text.strip()

            # Extract the director and actors
            p_tags = movie.find_all('p', class_="text-muted text-small")
            director = "N/A"
            actors = "N/A"
            if p_tags and len(p_tags) > 1:
                director_actors_info = p_tags[1]
                director = director_actors_info.find_all('a')[0].text if director_actors_info else 'N/A'
                actor_tags = director_actors_info.find_all('a')[1:]
                actors = ', '.join(actor.text for actor in actor_tags) if actor_tags else 'N/A'

            movie_list.append({
                'title': title,
                'year': year,
                'duration': duration,
                'genre': genre,
                'image_link': image_tag,
                'plot': plot,
                'director': director,
                'actors': actors,
            })

        return movie_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def save_movie_data_to_json(movie_data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(movie_data, f, ensure_ascii=False, indent=4)


def main():
    movie_data = scrape_imdb_movies()
    if movie_data:
        file_path = '/home/rakhymzhan/Kinopoisk/imdb-project/public/movies.json'
        save_movie_data_to_json(movie_data, file_path)
        print(f"Data has been scraped and saved to {file_path}.")
    else:
        print("Failed to scrape data or no data found.")


if __name__ == "__main__":
    main()
