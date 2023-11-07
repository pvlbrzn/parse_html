from .base import ParserBase



class GoogleBook(ParserBase):
    def parse(self):
        container = self.html.select_one(
            "#yDmH0d > c-wiz.SSPGKf.glB9Ve.K1b9Kc > div > div > div.N4FjMb.Z97G4e > c-wiz > div"
        )
        items = container.select(".hP61id")
        for item in items:
            name_box = item.select_one(".Epkrse ")
            price_box = item.select(".VfPpfd ")
            self.data.append(
                {"name": name_box.text, "price": [lesson_box.text for lesson_box in price_box] }
            )


class GoogleGames(ParserBase):
    def parse(self):
        container = self.html.select_one(
            "#yDmH0d > c-wiz.SSPGKf.glB9Ve > div > div > div.N4FjMb.Z97G4e > c-wiz > div > c-wiz > c-wiz:nth-child(2) > c-wiz"
        )
        items = container.select(".j2FCNc")
        for item in items:
            name_box = item.select_one(".sT93pb.DdYX5.OnEJge")
            type_box = item.select_one(".sT93pb.w2kbF")
            self.data.append(
                {"name": name_box.text, "genre": type_box.text}
            )


class GoogleMovies(ParserBase):
    def parse(self):
        container = self.html.select_one(
            "#yDmH0d > c-wiz.SSPGKf.glB9Ve > div > div > div.N4FjMb.Z97G4e > c-wiz > div > c-wiz"
        )
        items = container.select(".hP61id")
        for item in items:
            name_box = item.select_one(".Epkrse")
            grade_box = item.select_one(".LrNMN")
            self.data.append(
                {"name": name_box.text, "grade": [lesson_box.text for lesson_box in grade_box]}
            )


class GoogleChild(ParserBase):
    def parse(self):
        conteiner = self.html.select_one(
            "#yDmH0d > c-wiz.SSPGKf.glB9Ve > div > div > div.N4FjMb.Z97G4e > c-wiz > div"
        )
        items = conteiner.select(".VfPpkd-WsjYwc")
        for item in items:
            name_box = item.select_one(".Epkrse ")
            rating_box = item.select_one(".LrNMN")
            if name_box != None and rating_box != None:
                self.data.append({"name": name_box.text, "rating": [rating.text for rating in rating_box]})
            else:
                continue   