
class Video:

    def __init__(self, title: str, genre: str, rating: float) -> None:
        self.title = title
        self.genre = genre
        self.rating = rating

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        if not isinstance(title, (str)):
            raise TypeError(f"Title must ba string not {type(title)}")
        self._title = title

    @property
    def genre(self) -> str:
        return self._genre
    
    @genre.setter
    def genre(self, genre: str) -> None:
        if not isinstance(genre, (str)):
            raise TypeError(f"Genre must be string not {type(genre)}")
        self._genre = genre

    @property
    def rating(self) -> float:
        return self._rating
    
    @rating.setter
    def rating(self, rating: float) -> None:
        if not isinstance(rating, (float, int)):
            raise TypeError(f"Rating must be float or int not {type(rating)}")
        if not (0 <= rating <= 10):
            raise ValueError("Rating must be between 0 and 10")
        self._rating = rating

    def info(self) -> str:
        return f"Video with title {self.title}, genre {self.genre} and rating {self.rating}"

class TV_serie(Video):

    def __init__(self, title: str, genre: str, rating: float, num_episodes: int) -> None:
        super().__init__(title, genre, rating)
        self.num_episodes = num_episodes

    def info(self) -> str:
        return f"TV series with the title {self.title}, genre {self.genre}, rating {self.rating} and episodes {self.num_episodes}"
    
class Movie(Video):

    def __init__(self, title: str, genre: str, rating: float, duration: float) -> None:
        super().__init__(title, genre, rating)
        self.duration = duration
    
    def info(self) -> str:
        return f"Movie with the title {self.title}, genre {self.genre}, rating {self.rating} and duration {self.duration} minutes"
    
class Documentary(Video):

    def __init__(self, title: str, genre: str, rating: float) -> None:
        super().__init__(title, genre, rating)


pokemon = TV_serie("Pokemon", "Cartoon", 4.5, 550)
titanic = Movie("Titanic", "Romance", 4.7, 194)
code = Documentary("The Code", "Math", 4)

for video in tuple((pokemon, titanic, code)):
    print(video.info())