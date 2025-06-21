#Luluh Almogbil
'''
* Use only **lists and tuples**.


# Bonus

## Movie Ratings Analysis

Scenario:
You have just been hired as a data analyst at a movie streaming platform. Your manager has given you a list of movies, each with a tuple containing the movie title, release year, and user ratings. The platform allows users to rate movies on a scale of 1 to 10. Your manager wants you to create a Python program that:

1. Accepts a list of movies, with each movie represented as a tuple containing the movie title, release year, and a list of user ratings.
2. Calculates the average rating for each movie.
3. Filters out movies with an average rating lower than 6.0.
5. Displays the  movies, along with their title, release year, and average rating.

Example input:
```
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
```

Expected output:
```
1. The Shawshank Redemption (1994) - Avergae rating: 9.17 ★
2. The Godfather (1972) - Avergae rating: 8.83 ★
3. The Dark Knight (2008) - Avergae rating: 8.83 ★
4. Schindler's List (1993) - Avergae rating: 7.83 ★
5. Pulp Fiction (1994) - Avergae rating: 7.17 ★
```

**Challenge: Display the movies sorted by the average rating.**
'''
# movies = [
#     ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
#     ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
#     ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
#     ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
#     ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
#     ("The Room", 2003, [1, 2, 3, 4, 5, 1])
# ]

movies =[]

print(" Welcome to the Movie Ratings App!")
print("Enter your movies one by one. Type 'exit' to stop.\n")

while True:
    title = input("Movie title (or 'exit' to finish): ").strip()
    if title.lower() == "exit":
        break

    year = int(input("release year: "))
    ratingstext = input("Ratings (comma-separated, like 8,9,10): ")
    ratings = ratingstext.split(",")
    

    clean_ratings = []
    for r in ratings:
        if r.strip().isdigit():
            clean_ratings.append(int(r.strip())) # to convert my rating to integer not string
    
    # adds the movie as a tuple
    movies.append((title, year, clean_ratings))
    print("movie added!\n")

#outside my while

movies_with_avg = []
for movie in movies:
    title = movie[0]
    year = movie[1]
    ratings = movie[2]
    
    if ratings:
        avg = sum(ratings) / len(ratings)
    else:
        avg = 0
    
    movies_with_avg.append((title, year, avg))

#filter out my movies
topmovies = []
for movie in movies_with_avg:
    if movie[2] >= 6.0:
        topmovies.append(movie)

# Sorting in decsending order (highest first)
def get_rating(movie):
    return movie[2]  #will return the ratings only and ignore other elemnts

topmovies_sorted = sorted(topmovies, key=get_rating, reverse=True)

print("\nTop Rated Movies:\n")

if topmovies_sorted:
    for index, movie in enumerate(topmovies_sorted, start=1):
        title = movie[0]
        year = movie[1]
        avg = round(movie[2], 2)
        print(f"{index}. {title} ({year}) - Average Rating: {avg} ★")
else:
    print(" Unfortunately there are no movies with average rating of 6.0 or above.")
