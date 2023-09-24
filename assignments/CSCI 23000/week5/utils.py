def get_budget(movie_data: str, movie_name: str):
    # Split the movie data into a list of movies
    movies = movie_data.split("; ")

    # Loop through each movie
    for movie in movies:
        # Split the movie into a list of attributes
        attributes = movie.split(", ")

        # Check if the movie name matches the movie we're looking for
        if attributes[0] == movie_name:
            # Return the budget
            return int(attributes[2])

    # If we get here, the movie wasn't found
    return None


def get_total_budget(movie_data: str):
    # Split the movie data into a list of movies
    movies = movie_data.split("; ")

    # Initialize the total budget
    total_budget = 0

    # Loop through each movie
    for movie in movies:
        # Split the movie into a list of attributes
        attributes = movie.split(", ")

        # Add the budget to the total budget
        total_budget += int(attributes[2])

    # Return the total budget
    return total_budget
