# app/routes.py
from flask import render_template, request, jsonify
from app import app, get_db_connection

# Home route
@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    conn.close()
    return render_template('index.html', movies=movies)

# Movie details route
@app.route('/movie/<int:movie_id>', methods=['GET'])
def movie_details(movie_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
    movie = cursor.fetchone()
    conn.close()
    return render_template('movie_details.html', movie=movie)

# API route to fetch movies by genre
@app.route('/api/movies/<genre>', methods=['GET'])
def get_movies_by_genre(genre):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies WHERE genre = ?", (genre,))
    movies = cursor.fetchall()
    conn.close()
    movies_list = [dict(movie) for movie in movies]
    return jsonify(movies_list)