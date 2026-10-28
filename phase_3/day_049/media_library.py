# Day 49 27/10/26

class MediaItem:
    def __init__(self, item_id, year, title):
        self.item_id = item_id
        self.year = year
        self.title = title
    
    
    def display_info(self):
        print(f"\nItem ID: {self.item_id}\nYear: {self.year}\nTitle: {self.title}")


class Book(MediaItem):
    def __init__(self, item_id, year, title, author, pages):
        super().__init__(item_id, year, title)
        self.author = author
        self.pages = pages
    
    
    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}\nPages: {self.pages}")


class Movie(MediaItem):
    def __init__(self, item_id, year, title, director, duration):
        super().__init__(item_id, year, title)
        self.director = director
        self.duration = duration
    
    
    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}\nDuration: {self.duration}")


class VideoGame(MediaItem):
    def __init__(self, item_id, year, title, platform, genre):
        super().__init__(item_id, year, title)
        self.platform = platform
        self.genre = genre
    
    
    def display_info(self):
        super().display_info()
        print(f"Platform: {self.platform}\nGenre: {self.genre}")


class MediaLibrary:
    def __init__(self):
        self.media = []
    
    
    def add_media_item(self):
        i_id, y, t = len(self.media) + 1, 0, ""
        
        while True:
            try:
                y = int(input("\nYear: "))
                
                if y > 0:
                    break
                
                print("\nOnly positive integer numbers.")
            except ValueError:
                print("\nOnly numbers!")
        
        while not t.strip():
            t = input("\nTitle: ")
        
        ch = 0
        
        while True:
            try:
                ch = int(input("\nWhat type of media do you wanna add?\n1. Book\n2. Movie\n3. Videogame\n\nChoose: "))
                
                if 1 <= ch <= 3:
                    break
                
                print("\nChoose between 1 and 3!")
            except ValueError:
                print("\nOnly numbers!")
        
        if ch == 1:
            a, p = "", 0
            
            while not a.strip():
                a = input("\nAuthor: ")
            
            while True:
                try:
                    p = int(input("\nPages: "))
                    
                    if p > 0:
                        break
                    
                    print("\nOnly positive numbers!")
                except ValueError:
                    print("\nOnly numbers!")
            
            temp = Book(i_id, y, t, a, p)
            self.media.append(temp)
        elif ch == 2:
            di, du = "", 0
            
            while not di.strip():
                di = input("\nDirector: ")
            
            while True:
                try:
                    du = int(input("\nDuration (minutes): "))
                    
                    if du > 0:
                        break
                    
                    print("\nOnly positive numbers!")
                except ValueError:
                    print("\nOnly numbers!")
            
            temp = Movie(i_id, y, t, di, du)
            self.media.append(temp)
        else:
            pl, g = "", ""
            
            while not pl.strip():
                pl = input("\nPlatform: ")
            
            while not g.strip():
                g = input("\nGenre: ")
            
            temp = VideoGame(i_id, y, t, pl, g)
            self.media.append(temp)
        
        print("\nMedia was added successfully!")
    
    
    def display(self):
        if len(self.media) == 0:
            return print("\nNo media found!")
        
        for m in self.media:
            m.display_info()
    
    
    def search_title(self):
        if len(self.media) == 0:
            return print("\nNo media found!")
        
        t, flag = "", False
        
        while not t.strip():
            t = input("\nTitle: ")
        
        for m in self.media:
            if t.lower() == m.title.lower():
                flag = True
                m.display_info()
        
        if not flag:
            print(f"No media with title {t} was found!")
        
    
    def display_books(self):
        if len(self.media) == 0:
            return print("\nNo media found!")
        
        flag = False
        
        for m in self.media:
            if isinstance(m, Book):
                flag = True
                m.display_info()
        
        if not flag:
            print("\nNo books were found!")
        
    
    def display_movies(self):
        if len(self.media) == 0:
            return print("\nNo media found!")
        
        flag = False
        
        for m in self.media:
            if isinstance(m, Movie):
                flag = True
                m.display_info()
        
        if not flag:
            print("\nNo movies were found!")
    
    
    def display_videogames(self):
        if len(self.media) == 0:
            return print("\nNo media found!")
        
        flag = False
        
        for m in self.media:
            if isinstance(m, VideoGame):
                flag = True
                m.display_info()
        
        if not flag:
            print("\nNo videogames were found!")


def main():
    print("========== MEDIA LIBRARY ==========")
    
    media_library = MediaLibrary()
    
    while True:
        num = get_num("\n1. Add media item\n2. Display media\n3. Search based on title\n4. Display books\n5. Display movies\n6. Display videogames\n7. Exit\n\nChoose: ")
        
        match(num):
            case 1:
                media_library.add_media_item()
            case 2:
                media_library.display()
            case 3:
                media_library.search_title()
            case 4:
                media_library.display_books()
            case 5:
                media_library.display_movies()
            case 6:
                media_library.display_videogames()
            case 7:
                break
    
    print("\nGoodbye!")


def get_num(p):
    while True:
        try:
            n = int(input(p))
            
            if 1 <= n <= 7:
                return n
            
            print("\nOnly integers between 1 and 7!")
        except ValueError:
            print("\nOnly numbers!")


main()
