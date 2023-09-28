import pickle
import os
from flask import Flask, redirect, request, render_template, jsonify

app = Flask(__name__)

# Load your pre-trained movie recommendation model using pickle
file_path = 'movies_list.pkl'  # Adjust the file path as needed

movie_model={
    "Avatar": "https://images.app.goo.gl/zmbDCUheam9N7EDb8",
    "Titanic": "https://images.app.goo.gl/95qLgUmxGJpfEutt9",
    "Midnight is just a beginning": "https://images.app.goo.gl/LVvegG8J5Kyag4k96",
    "Jurassic park": "https://www.google.com/imgres?imgurl=https%3A%2F%2Frender.fineartamerica.com%2Fimages%2Frendered%2Fdefault%2Fposter%2F8%2F10%2Fbreak%2Fimages%2Fartworkimages%2Fmedium%2F3%2Fjurassic-park-lost-world-welcome-to-the-park-samantha-pease.jpg&tbnid=wnf_gxtPDakqEM&vet=1&imgrefurl=https%3A%2F%2Ffineartamerica.com%2Ffeatured%2Fjurassic-park-lost-world-welcome-to-the-park-samantha-pease.html%3Fproduct%3Dposter&docid=oC3iu0W0bBtqOM&w=600&h=750&hl=en-IN&source=sh%2Fx%2Fim%2Fm0%2F4",
    "Harry Potter": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FM%2FMV5BMGVmMWNiMDktYjQ0Mi00MWIxLTk0N2UtN2ZlYTdkN2IzNDNlXkEyXkFqcGdeQXVyODE5NzE3OTE%40._V1_.jpg&tbnid=2NwDipADR54NyM&vet=1&imgrefurl=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt1201607%2F&docid=NeIQHDLlVHZCbM&w=2000&h=3000&hl=en-IN&source=sh%2Fx%2Fim%2Fm0%2F4",
    "Furious": "https://images.app.goo.gl/BQtZFLscNvktqYX18",
    "The lovely bones": "https://images.app.goo.gl/hCQCPSGJie7DwFTW",
    "Spider man": "https://images.app.goo.gl/axkbDL2vnUDKEzDu8",
    "Batman": "https://images.app.goo.gl/ibByeAdkqXjPHPHZ9",
    "Gulliver's travel": "https://images.app.goo.gl/f9ejiDdiRQvKUAej7",
    "Pirates of the Carribean": "https://images.app.goo.gl/hRqjKWNaQmJcgB5EA",
    "Gurrasic park":"https://images.app.goo.gl/rF67W5GbnAML2eNM7"
}
if os.path.exists(file_path):
    with open(file_path, 'rb') as model_file:
        movie_model = pickle.load(model_file)

if not isinstance(movie_model, dict):
    raise ValueError("The loaded data is not in the expected format (dictionary).")

# Sample data for demonstration purposes (replace with your actual data)
movie_data = [
    {'title': 'Movie 1', 'genre': 'action', 'rating': 5},
    {'title': 'Movie 2', 'genre': 'comedy', 'rating': 4},
    # Add more movie data here
]

@app.route('/')
def home():
    return render_template('submit.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    # Your search logic here
    if query in movie_model:
        image_url = movie_model[query]
        if image_url:
            return redirect(image_url)
        else:
            return "Image URL not available for this movie."
    else:
        return "Movie not found in the dataset."
    
@app.route('/recommend', methods=['POST'])
def recommend_movies():
    user_input = request.form
    user_genre = user_input.get('genre-filter')
    user_rating = int(user_input.get('rating-filter'))

    # Filter movies based on user input (genre and rating)
    recommended_movies = []
    for movie in movie_model:
        if (user_genre == 'all' or user_genre == movie['genre']) and movie['rating'] >= user_rating:
            recommended_movies.append(movie['title'])

    return jsonify({'movies': recommended_movies})

if __name__ == '__main__':
    app.run(debug=True)
