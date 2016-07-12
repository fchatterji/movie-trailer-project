# udacity_project_movie_trailer

This script takes as input a list of movies, generates an html file displaying those movies and automatically opens it in the browser.

To use, clone the files on your computer, open the command line and navigate to the files. Then, simply execute the file entertainment_center.py

    python entertainment_center.py

An html file, called fresh_tomatoes, will be created and opened. 

To add or change movies, open the file entertainement_center.py. Adding or deleting a movie requires two steps:

1. Instantiate the Movie class. Four parameters are needed: title, storyline, url of the poster, url of the trailer. 

    million_dollar_baby = media.Movie(
        "Million Dollar Baby",
        "A determined woman works with a hardened boxing trainer to become a professional.",
        "https://upload.wikimedia.org/wikipedia/en/d/d3/Million_Dollar_Baby_poster.jpg",
        "https://www.youtube.com/watch?v=5_RsHRmIRBY"
        )

2. Add or delete the movie in the "movies" list

    movies = [toy_story, million_dollar_baby, lagaan, three_idiots]

This project is part of the udacity full stack web developper course. It is not licensed.


Author: Florent Chatterji
