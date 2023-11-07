from parse1.parse_obj1 import Book

def main():
    print(2)
    python_course = Book('https://play.google.com/store/books?hl=ru&gl=US')
    print(3)
    python_course.get_html()
    python_course.parse()
    python_course.save_json('books.json')


if __name__ == "__main__":
    main()