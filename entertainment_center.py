import fresh_tomatoes
import media

# Movies

wall_street = media.Movie("Wall Street (1987)",
                        "A young and impatient stockbroker is willing to do anything to get to the top,"
                        "including trading on illegal inside information taken through a ruthless and greedy"
                        "corporate raider who takes the youth under his wing.",
                        "http://ecx.images-amazon.com/images/I/51PSMDDFG1L.jpg", # noqa
                        "https://www.youtube.com/watch?v=7b4BcbhGggM") # noqa

inside_job = media.Movie("Inside Job",
                        "Takes a closer look at what brought about the financial meltdown.",
                        "http://solarmovie.one/wp-content/uploads/2015/08/405px-OfficialInsideJob_Poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=FzrBurlJUNk")  # noqa

margin_call = media.Movie("Margin Call",
                        "Follows the key people at an investment bank,"
                        "over a 24-hour period, during the early stages of the financial crisis.",
                        "http://resizing.flixster.com/zQEsRSKNDL-9x65czqmBcP-Xrrg=/800x1200/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/77/11177758_ori.jpg", # noqa
                        "https://www.youtube.com/watch?v=uj4QrAcwVi0") # noqa

capitalism_a_love_story = media.Movie("Capitalism: A Love Story",
                        "An examination of the social costs of corporate interests"
                        "pursuing profits at the expense of the public good.",
                        "http://ecx.images-amazon.com/images/I/71GSnvWC2GL._SL1500_.jpg", # noqa
                        "https://www.youtube.com/watch?v=CkTkYQkG13w") # noqa

barbarians_at_the_gate = media.Movie("Barbarians at the Gate",
                        "The president of a major tobacco company decides to buy the company himself,"
                        "but a bidding war ensues as other companies make their own offers.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/9/95/BarbariansAtTheGateDVDCover.jpg/250px-BarbariansAtTheGateDVDCover.jpg", # noqa
                        "https://www.youtube.com/watch?v=9FmcrpMO72Q") # noqa
the_wolf_of_wall_street = media.Movie("The Wolf of Wall Street",
                        "Jordan Belfort is a Long Island penny stockbroker who"
                        "served 22 months in prison for defrauding investors in a massive 1990s"
                        "securities scam that involved widespread corruption on Wall Street"
                        "and in the corporate banking world, including shoe designer Steve Madden.",
                        "http://ia.media-imdb.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_SX640_SY720_.jpg", # noqa
                        "https://www.youtube.com/watch?v=idAVRvQeYAE") # noqa

the_big_short = media.Movie("The Big Short",
                        "Based on the book by Michael Lewis"
                        "(writer of Moneyball, Liar's Poker and Flash Boys, among others),"
                        "the true story of a handful of investors who bet against the US mortgage market in 2006-7.",
                        "http://cdn3-www.comingsoon.net/assets/uploads/gallery/the-big-short/tbs_1-sht_teaser.jpg", # noqa
                        "https://www.youtube.com/watch?v=vgqG3ITMv1Q") # noqa

# TvShows

wall_street_warriors = media.TvShow("Wall Street Warriors",
                        "season1, 2, 3",
                        "http://ecx.images-amazon.com/images/I/51uYlndI-IL.jpg", # noqa
                        "https://www.youtube.com/watch?v=nyRiuv4EDB4")# noqa

traders = media.TvShow("Traders",
                        "season1, 2, 3, 4, 5",
                        "http://www.gstatic.com/tv/thumb/tvbanners/184285/p184285_b_v8_ad.jpg", # noqa
                        "https://www.youtube.com/watch?v=n5RbftJr5CA") # noqa


movies_and_tvshows = [wall_street, inside_job, margin_call, capitalism_a_love_story, barbarians_at_the_gate, the_wolf_of_wall_street, the_big_short, wall_street_warriors, traders,]


fresh_tomatoes.open_movies_page(movies_and_tvshows)
