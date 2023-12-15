#!/usr/bin/env python3

#Book in book.py has the title and page_count passed into __init__, and values can be set to new instance.
#Book in book.py prints "page_count must be an integer" if page_count is not an integer.
#Book in book.py outputs "Flipping the page...wow, you read fast!" when method turn_page() is called

class Book:
    def __init__(self, title=None, page_count=0):
        self.title = title
        self.page_count = page_count
    
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    
        