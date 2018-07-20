import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://images-na.ssl-images-amazon.com/images/I/91q0UP6%2BUTL._SY606_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                        "John Lasseter")

# print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://images-na.ssl-images-amazon.com/images/I/61OUGpUfAyL._SY679_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                     "James Cameron")

# avatar.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://img.moviepostershop.com/the-school-of-rock-movie-poster-2003-1020191888.jpg",
                             "https://www.youtube.com/watch?v=oP7kExN8LFA"
                             "Richard Linklater")

le_scaphandre_et_le_papillon = media.Movie("Le Scaphandre et Le Papillon",
                                           "A man relives his final moments and gains an appreciation for life",
                                           "https://m.media-amazon.com/images/M/MV5BMTc3MjkzMDkxN15BMl5BanBnXkFtZTcwODAyMTU1MQ@@._V1_UY268_CR0,0,182,268_AL_.jpg",
                                           "https://www.youtube.com/watch?v=CecAbmELolY"
                                           "Julian Schnabbel")

Avengers = media.Movie("Avengers Assemble",
                       "Heroes unite to save the world",
                       "https://m.media-amazon.com/images/M/MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmYjU5ZGI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8"
                       "Joss Whedon")

movies = [toy_story, avatar, school_of_rock, le_scaphandre_et_le_papillon, Avengers]

fresh_tomatoes.open_movies_page(movies)
