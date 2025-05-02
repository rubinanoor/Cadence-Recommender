# Cadence - Music Recommendation System

**Cadence** is a music recommendation system that provides song suggestions based on the song and artist provided by the user. Using **KMeans clustering** and features like danceability, loudness, and energy, this app offers personalized music recommendations. The backend is powered by **Flask**, and the frontend is built using **HTML/CSS**.

## Features

- **Music Recommendations**: Get similar song recommendations by providing a song name and artist.
- **KMeans Clustering**: Songs are grouped based on their musical features using KMeans clustering.
- **Flask Backend**: Handles the recommendation logic and serves the app's frontend.
- **Responsive UI**: Simple, user-friendly interface for easy interaction.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/cadence-music-recommender.git
   cd cadence-music-recommender
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**
   ```bash
   python app.py
   ```

   The app will be accessible at `http://127.0.0.1:5000`.

## Usage

1. **Open the app** in your browser by visiting `http://127.0.0.1:5000`.
2. **Enter a song name and artist** in the input fields and click on "Get Recommendations".
3. **View the recommendations** displayed below the form.

## Project Structure

```
├── app.py                # Flask application
├── model.py              # Contains logic for song recommendations
├── static/               # Static files (CSS, JS, images)
├── templates/            # HTML templates (frontend)
├── requirements.txt      # Python dependencies
└── README.md             # Project description and documentation
```

## Technologies Used

- **Flask**: Web framework for the backend.
- **KMeans**: Machine learning model for clustering songs based on musical features.
- **HTML/CSS**: Frontend technologies for the user interface.


