# udacity_project_movie_trailer

This script takes as input a list of movies, generates an html file displaying those movies and automatically opens it in the browser.

To use, clone the files on your computer, open the command line and navigate to the files. Then, execute the file entertainment_center.py

    python entertainment_center.py

An html file will be created and opened. To edit the movies displayed, open the file
To show the website, execute the file entertainment_center.py in the command line.

To add or change movies, open the file entertainement_center.py. Adding or deleting a movie requires two steps:

1. Add or delete the movie information

    million_dollar_baby = media.Movie(
        "Million Dollar Baby",
        "A determined woman works with a hardened boxing trainer to become a professional.",
        "https://upload.wikimedia.org/wikipedia/en/d/d3/Million_Dollar_Baby_poster.jpg",
        "https://www.youtube.com/watch?v=5_RsHRmIRBY"
        )

2. Add or delete the movie in the "movies" list

    movies = [toy_story, million_dollar_baby, lagaan, three_idiots]

This project is part of the udacity full stack web developper course.
