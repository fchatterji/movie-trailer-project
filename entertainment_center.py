import media
import fresh_tomatoes

# Instantiate the movies
toy_story = media.Movie(
    "Toy Story",
    "A cowboy doll is profoundly threatened and jealous when a new spaceman"
    " figure supplants him as top toy in a boy's room.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )

million_dollar_baby = media.Movie(
    "Million Dollar Baby",
    "A determined woman works with a hardened boxing trainer to become a"
    " professional.",
    "https://upload.wikimedia.org/wikipedia/en/d/d3/"
    "Million_Dollar_Baby_poster.jpg",
    "https://www.youtube.com/watch?v=5_RsHRmIRBY"
    )

lagaan = media.Movie(
    "Lagaan",
    "The people of a small village in Victorian India stake their"
    " future on a game of cricket against their ruthless British rulers.",
    "https://upload.wikimedia.org/wikipedia/en/b/b6/Lagaan.jpg",
    "https://www.youtube.com/watch?v=oSIGQ0YkFxs"
    )

three_idiots = media.Movie(
    "3 idiots",
    "Two friends are searching for their long lost companion. They revisit"
    " their college days and recall the memories of their friend who "
    "inspired them to think differently, even as the rest of the world "
    "called them \"idiots\".",
    "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
    "https://www.youtube.com/watch?v=K0eDlFX9GMc"
    )

# Create a list of all movies (movies have to be manually added to this list)
movies = [toy_story, million_dollar_baby, lagaan, three_idiots]

# Generate and open the fresh_tomatoes.html file
fresh_tomatoes.open_movies_page(movies)
