import webbrowser


class Movie():
    """Contains attributes of movies and method to show the trailer

    Attributes:
        title: string of the movie title.
        storyline: string of the movie storyline.
        poster_image_url: string of the url of a poster image for the movie.
        trailer_youtube_url: string of the url of the trailer on youtube.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Inits Movie and sets all attributes"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens the movie trailer"""
        webbrowser.open(self.trailer_youtube_url)
