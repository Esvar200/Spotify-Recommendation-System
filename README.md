# Spotify Recommendation System

**Spotify Recommendation System** is a web-based application that recommends songs based on the genre selected by the user. By utilizing cosine similarity, the model finds and suggests the most relevant tracks from the dataset, making it easy for users to discover new music.

## Key Features

- **Genre-Based Recommendations**: Users can select a genre, and the system will recommend songs that best match the selected genre.
- **Cosine Similarity**: The model uses cosine similarity to compare songs and identify the most relevant recommendations.
- **Web Interface**: A simple and interactive web interface built with Flask, allowing users to easily interact with the recommendation system.

## Technologies Used

- **Python**: The core programming language for the project.
- **sklearn**: Used for implementing Count Vectorizer and cosine similarity.
- **Flask**: A lightweight web framework for building the web interface.
- **HTML**: For structuring the web pages.

## How to Run the Project

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/Spotify_Recommendation_System.git
    cd Spotify_Recommendation_System
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Machine Learning Script**:
    ```bash
    python ML.py
    ```

4. **Run the Flask App**:
    ```bash
    python web.py
    ```

5. **Access the Web Interface**:
   - Open your web browser and go to `http://localhost:5000`.
   - Select a genre from the dropdown menu and click "Recommend" to see the list of suggested songs.

## File Structure

- **`ML.py`**: Handles the machine learning tasks, including generating recommendations using cosine similarity.
- **`web.py`**: The main Flask application file that serves the web interface.
- **`templates/`**: Contains the HTML files for the web interface.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any feature enhancements or bug fixes.


---
