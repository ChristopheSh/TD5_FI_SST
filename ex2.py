#Test

from book import Book

def main():
    book = Book("TEST")
    book.insert_buy(10,10.0)
    book.insert_sell(120,12.0)
    book.insert_buy(5,10.0)
    book.insert_buy(2,11.0)
    #book.insert_call(1,10.0)
    #book.insert_sell(10,10.0)


if __name__ == "__main__":
    print("\n")
    main()

