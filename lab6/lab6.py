
"""
OLCHLT
 
"""
my_name = "Bilgehan Dede"
my_id = "114102502701"
my_email = "b.dede1999@gtu.edu.tr"

def problem0():
    class p0:
        def __init__(self, x):
            self.hilal = x

        def get_value(self):
            return self.hilal

        def set_value(self, x):
            self.hilal = x

    return p0

def problem1():
    class p1:
        def __init__(self, x):
            if isinstance(x, int):
                self.hilal = x
            else:
                self.hilal = 0

        def get_value(self):
            return self.hilal

        def set_value(self, x):
            if isinstance(x, int):
                self.hilal = x

    return p1

def problem2():
    class p2:
        def __init__(self, x, y):
            self.panda = x
            self.hilos = y

        def get_area(self):
            return self.panda * self.hilos

        def get_perimeter(self):
            return (2 *self.panda) + (2* self.hilos)

    return p2

def problem3():
    class Grades:
        def __init__(self):
            self.tokuc_kafa = []

        def add_grade(self, panda):
            self.tokuc_kafa.append(panda)

        def remove_grade(self, panda):
            if panda in self.tokuc_kafa:
                self.tokuc_kafa.remove(panda)

        def get_min(self):
            return (min(self.tokuc_kafa, default=0.0))

        def get_max(self):
            return (max(self.tokuc_kafa, default=0.0))

        def get_mean(self):
            if not self.tokuc_kafa:
                return 0
            return (sum(self.tokuc_kafa) / len(self.tokuc_kafa))

        def get_median(self):
            sort_hilos = sorted(self.tokuc_kafa)
            length = len(sort_hilos)

            if length == 0:
                return 0

            mid = length // 2

            if length % 2 == 0:
                return ((sort_hilos[mid - 1] + sort_hilos[mid]) / 2)
            else:
                return (sort_hilos[mid])

    return Grades

def problem4():
    class Movie:
        def __init__(self, movie_name, director, year, rating=0.0, length=0):
            self.movie_name = movie_name
            self.director = director
            self.year = year
            self.rating = rating
            self.length = length

        def get_movie_name(self):
            return self.movie_name

        def get_director(self):
            return self.director

        def get_year(self):
            return self.year

        def get_rating(self):
            return self.rating

        def get_length(self):
            return self.length

        def set_rating(self, x):
            if 0 <= x <= 10.0:
                self.rating = x

        def set_length(self, x):
            if 0 <= x <= 500:
                self.length = x

    return Movie

def problem5():
    class MovieCatalog:
        Movie = problem4()
        def __init__(self, filename):
            self.movies = []
            self.load_movies(filename)

        def load_movies(self, filename):
            Movie = problem4()
            with open(filename, 'r') as file: # ingilizce karakter bazlı okuma mevcuttur!!!
                lines = file.readlines()
        
                for line in lines:
                    # '\n' karakterini temizle
                    line = line.strip()
        
                    # Satırı virgüllerle ayır
                    movie_data = line.split(',')
                    movie_data = [field.strip() for field in movie_data]
                    movie_name, director, year, rating, length = movie_data
                    year = int(year)
                    rating = float(rating)
                    length = int(length)
                    movie_instance = Movie(movie_name, director, year, rating, length)
                    self.movies.append(movie_instance)

        def add_movie(self, movie_name, director, year, rating=0.0, length=0):
            Movie = problem4()
            existing_movies = [movie.get_movie_name() for movie in self.movies]
            if movie_name not in existing_movies:
                new_movie = Movie(movie_name, director, year, rating, length)
                self.movies.append(new_movie)

        def remove_movie(self, movie_name):
            for movie in self.movies:
                if movie.get_movie_name() == movie_name:
                    self.movies.remove(movie)

        def get_oldest(self):
            if not self.movies:
                return None
        
            oldest_movie = self.movies[0]
            for movie in self.movies[1:]:
                if movie.get_year() < oldest_movie.get_year():
                    oldest_movie = movie
        
            return oldest_movie.get_movie_name()

        def get_lowest_ranking(self):
            if not self.movies:
                return None
        
            lowest_ranking_movie = self.movies[0]
            for movie in self.movies[1:]:
                if movie.get_rating() < lowest_ranking_movie.get_rating():
                    lowest_ranking_movie = movie
        
            return lowest_ranking_movie.get_movie_name()

        def get_highest_ranking(self):
            if not self.movies:
                return None
        
            highest_ranking_movie = self.movies[0]
            for movie in self.movies[1:]:
                if movie.get_rating() > highest_ranking_movie.get_rating():
                    highest_ranking_movie = movie
        
            return highest_ranking_movie.get_movie_name()

        def get_by_director(self, director):
            director_movies = [movie.get_movie_name() for movie in self.movies if movie.get_director() == director]
            return director_movies

    return MovieCatalog