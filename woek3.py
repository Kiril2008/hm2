from functools import total_ordering
from datetime import datetime


###1

@total_ordering
class Movie:
    def __init__(self, title, year, rating, genre):
        self.title = title
        self.year = year
        self.rating = rating
        self.genre = genre

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.rating}"

    def __repr__(self):
        return f"Movie('{self.title}', {self.year}, {self.rating}, '{self.genre}')"

    def __eq__(self, other):
        return self.rating == other.rating and self.year == other.year

    def __lt__(self, other):
        if self.rating == other.rating:
            return self.year < other.year
        return self.rating < other.rating

    def __hash__(self):
        return hash((self.title, self.year, self.rating, self.genre))

    def __format__(self, format_spec):
        if format_spec == "short":
            return f"{self.title} - {self.rating}"
        return str(self)

    @property
    def age(self):
        return datetime.now().year - self.year


# тест
movies = [
    Movie("Інтерстеллар", 2014, 8.6, "Фантастика"),
    Movie("Темний лицар", 2008, 9.0, "Бойовик"),
    Movie("Форест Гамп", 1994, 8.8, "Драма"),
    Movie("Матриця", 1999, 8.7, "Фантастика"),
    Movie("Титанік", 1997, 7.8, "Романтика")
]

print("Фільми до сортування:")
for movie in movies:
    print(movie)

movies.sort(reverse=True)

print("\nФільми після сортування:")
for movie in movies:
    print(movie)

print("\nПорівняння:")
print(movies[0] > movies[-1])

print("\nФорматування:")
print(f"{movies[0]:short}")

print("\nВік фільму:")
print(f"{movies[2].age} років")



#####3 
import random

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __setitem__(self, index, song):
        self.songs[index] = song

    def __delitem__(self, index):
        del self.songs[index]

    def __contains__(self, song):
        return any(song.lower() in s["title"].lower() for s in self.songs)

    def __iter__(self):
        return iter(self.songs)

    def __str__(self):
        return f"Playlist '{self.name}' ({len(self)} songs)"

    def __bool__(self):
        return len(self.songs) > 0

    def add_song(self, artist, title, duration):
        self.songs.append({
            "artist": artist,
            "title": title,
            "duration": duration
        })

    def remove_song(self, song_title):
        self.songs = [s for s in self.songs if s["title"] != song_title]

    def shuffle(self):
        random.shuffle(self.songs)

    def get_total_duration(self):
        return sum(s["duration"] for s in self.songs)

    def find_by_artist(self, artist):
        return [s for s in self.songs if s["artist"].lower() == artist.lower()]


playlist = Playlist("Мій плейлист")
playlist.add_song("Queen", "Bohemian Rhapsody", 5.55)
playlist.add_song("The Beatles", "Hey Jude", 7.11)
playlist.add_song("Led Zeppelin", "Stairway to Heaven", 8.02)
playlist.add_song("Queen", "We Will Rock You", 2.02)

print(playlist)
print(len(playlist))
print(playlist[0])
print(playlist[-2:])

print("Queen" in playlist)

print(playlist.get_total_duration())

for i, song in enumerate(playlist):
    print(i+1, song)

print(playlist.find_by_artist("Queen"))