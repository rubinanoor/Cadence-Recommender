from flask import Flask, request, jsonify, render_template

# Import the recommendation function from your ML model 
from model import recommend_songs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    song = request.form.get('song')
    artist = request.form.get('artist')

    # Call the recommend_songs function with user input
    results = recommend_songs(song, artist)

    # If no results returned, send error message as JSON
    if not results:
        return jsonify({'error': 'Song not found. Please check the spelling.'})

    # If results found, return as JSON response
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True) 
