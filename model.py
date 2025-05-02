import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

# Load dataset containing song information and audio features
df = pd.read_csv('songs.csv')  

# Define the features to be used for clustering
features = ['danceability', 'loudness', 'acousticness',
            'instrumentalness', 'valence', 'energy']

# Drop rows where any of the selected features are missing (NaN)
df = df.dropna(subset=features)

# Normalize the feature values to a range of 0 to 1 for better clustering
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(df[features])

# Apply KMeans clustering to group songs into 5 clusters based on audio features
kmeans = KMeans(n_clusters=5, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)  # Assign each song to a cluster

# Define a function to recommend songs based on a given track and artist
def recommend_songs(track_name, artist_name):
    # Clean user input by trimming and converting to lowercase for comparison
    track_name = track_name.strip().lower()
    artist_name = artist_name.strip().lower()

    # Find the song in the dataset that matches the input track and artist name
    match = df[(df['track_name'].str.lower() == track_name) &
               (df['artist_name'].str.lower() == artist_name)]

    # If song not found, return empty list
    if match.empty:
        return []

    # Get cluster of the input song
    input_index = match.index[0]
    input_cluster = df.loc[input_index, 'cluster']

    # Find other songs in the same cluster, excluding input song itself
    recommendations = df[(df['cluster'] == input_cluster) & (df.index != input_index)]

    # Randomly sample 20 songs from the same cluster and return as a list of dictionaries
    return recommendations[['track_name', 'artist_name']].sample(20).to_dict(orient='records')
