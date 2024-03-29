# app/setup_db.py
import sqlite3

# Connect to the database (assuming the database file is in the instance/ folder)
conn = sqlite3.connect('instance/movies.db')
c = conn.cursor()

# Create the movies table
c.execute("""
    CREATE TABLE movies (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        genre TEXT NOT NULL,
        year INTEGER NOT NULL,
        rating REAL NOT NULL,
        description TEXT
    )
""")

# Create the users table
c.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
""")

# Create the user_ratings table
c.execute("""
    CREATE TABLE user_ratings (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        movie_id INTEGER NOT NULL,
        rating INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (movie_id) REFERENCES movies(id)
    )
""")

# Insert sample movie data
c.executescript("""
    INSERT INTO movies (title, genre, year, rating, description)
    VALUES
        ('The Shawshank Redemption', 'Drama', 1994, 9.3, 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'),
        ('The Godfather', 'Crime', 1972, 9.2, 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'),
        ('The Dark Knight', 'Action', 2008, 9.0, 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.'),
        ('Pulp Fiction', 'Crime', 1994, 8.9, 'The lives of two mob hitmen, a boxer, a gangster\'s wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'),
        ('Forrest Gump', 'Drama', 1994, 8.8, 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.');
""")

# Commit the changes and close the connection
conn.commit()
conn.close()