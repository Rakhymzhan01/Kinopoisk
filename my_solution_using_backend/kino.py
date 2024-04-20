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

def generate_html_page(movie_info):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{movie_info['Title']} - Movie Info</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #000;
                color: #fff;
            }}
            .container {{
                max-width: 800px;
                margin: 20px auto;
                padding: 20px;
                background-color: #111;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            }}
            img {{
                max-width: 100%;
                height: auto;
                display: block;
                margin: 0 auto;
                border-radius: 10px;
            }}
            h1, h2, h3, h4, h5, h6 {{
                margin-top: 0;
            }}
            p {{
                margin-bottom: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{movie_info['Title']} ({movie_info['Year']})</h1>
            <img src="{movie_info['Poster']}" alt="{movie_info['Title']} Poster">
            <p><strong>Genre:</strong> {movie_info['Genre']}</p>
            <p><strong>Director:</strong> {movie_info['Director']}</p>
            <p><strong>Actors:</strong> {movie_info['Actors']}</p>
            <p><strong>Plot:</strong> {movie_info['Plot']}</p>
        </div>
    </body>
    </html>
    """
    return html_template

api_key = '711716bd'
movie_title = 'the matrix'
movie_data = search_movie(movie_title, api_key)
movie_info = extract_movie_info(movie_data)

if movie_info:
    html_page = generate_html_page(movie_info)
    with open('movie_info.html', 'w') as f:
        f.write(html_page)
    print("HTML page generated successfully.")
else:
    print("Failed to generate HTML page.")
