import webbrowser

class Movie():
    #Defines the behaviour of each movie shown in the html page
    VALID_RATINGS = [ "G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, director):
    #Initialises the functions and aspects for each part of the movies html page   
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director

    def show_trailer(self):
        # Tells python to open the url containing the YouTube trailer
        webbrowser.open(self.trailer_youtube_url)
