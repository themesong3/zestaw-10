class Ebook():
    """ When creating new Ebook object, pass the following arguments:
    1. author   2. title   3. number of pages """

    def __init__(self, author, title, pages):
        self.author = author
        self.titel = title
        self.pages = pages
        self.current_page = 1
        self.is_open = False

    def open_book(self):
        self.is_open = True
    
    def close_book(self):
        self.is_open = False


    def show_page(self):
        if self.is_open:
            print(f"You are on page {self.current_page}")
        else:
            print("Book is closed")
    
    def jump_to_page(self, page_to_jump_to):
        if self.is_open:
            if page_to_jump_to > 0 and page_to_jump_to < self.pages:
                self.current_page = page_to_jump_to
            else:
                print(f"Can not jump to that page (book has {self.pages} pages)")
        else:
            print("Book is closed")

    def next_page(self):
        if self.is_open:
            if self.current_page < self.pages:
                self.current_page += 1
            else:
                print("You are on the last page !")
        else:
            print("Book is closed")
    
    def previous_page(self):
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
            else:
                print("You are on the first page !")
        else:
            print("Book is closed")

    def show_info(self):
        if self.is_open:
            print(f"Author: {self.author}")
            print(f"Title: {self.titel}")
            print(f"Pages: {self.pages}")
            print(f"current_page: {self.current_page}")
        else:
            print("Book is closed")

makbet = Ebook("William S.", "Manbet", 100)
makbet.open_book()
makbet.show_info()
makbet.jump_to_page(100)
makbet.next_page()
makbet.jump_to_page(47)
makbet.previous_page()
makbet.show_page()