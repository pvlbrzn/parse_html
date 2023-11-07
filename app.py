from parse.parse_obj import GoogleBook, GoogleGames, GoogleMovies, GoogleChild



def main():
    books = GoogleBook('https://play.google.com/store/books?hl=ru&gl=US')
    books.get_html()
    books.parse()
    books.save_json('books.json')

    games = GoogleGames("https://play.google.com/store/games?hl=ru&gl=US")
    games.get_html()
    games.parse()
    games.save_json("games.json")

    movies = GoogleMovies("https://play.google.com/store/movies?hl=ru&gl=US")
    movies.get_html()
    movies.parse()
    movies.save_json("movies.json")

    kids = GoogleChild("https://play.google.com/store/apps/category/FAMILY?hl=ru&gl=US")
    kids.get_html()
    kids.parse()
    kids.save_json("kids.json")


if __name__ == "__main__":
    main()