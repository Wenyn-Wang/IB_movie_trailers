import webbrowser

class Video():
    def __init__(self, movie_title, poster_image, trailer_youtube):
        print("Video Constructor Called")
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

class Movie(Video):
    """This class provides a way to store movie related information."""

    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        print("Movie Constructor Called")
        Video.__init__(self, movie_title, poster_image, trailer_youtube)
        self.storyline = movie_storyline

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """This class provides a way to store TvShow related information."""
    def __init__(self, movie_title, current_season_and_episode, poster_image,
                 trailer_youtube):
        print("TvShow Constructor Called")
        Video.__init__(self, movie_title, poster_image, trailer_youtube)
        self.current_season_and_episode = current_season_and_episode

    def show_sources(self):
        webbrowser.open(self.trailer_youtube_url)
        
    
