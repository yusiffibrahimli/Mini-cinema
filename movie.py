class Hours:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f'{self.start_time}{self.end_time}'
    
class Movie:
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        self.name = name
        self.director = director
        self.year = year
        self.genre = genre
        self.duration = duration
        self.imdb = float(imdb)
        self.hours = list(hours)
        self.price = price

    def show_info(self):
        hours=[]
        for i in self.hours:
            dict = {
                'baslama vaxti': i.start_time,
                'bitme vaxti': i.end_time
            }
        hours.append(dict)
        # print(hours)

        return '''
        Movie name : {}
        Movie directory : {}
        Movie year : {}
        Movie genre : {}
        Movie duration : {}
        Movie imdb : {}
        Hours : {}
        Movie price : {}

'''.format(self.name,self.director,self.year,self.genre,self.duration,self.imdb,hours,self.price)
   
    def year_info(self):
        try:
            if int(self.year) < 2000:  
                return 'Old category'
            else:
                return 'New category'
        except ValueError:
            return "Please enter a valid year."

    def rating_info(self):
        try:
            if self.imdb < 6.0:
                return 'E'
            elif 6.0 <= self.imdb < 7.0:
                return 'D'
            elif 7.0 <= self.imdb < 8.0:
                return 'C'
            elif 8.0 <= self.imdb < 9.0:
                return 'B'
            elif 9.0 <= self.imdb <= 10.0:  
                return 'A'  
        except ValueError:
            return 'Not found'

        
    def duration_info(self):
        try:
            if int(self.duration) < 120:  
                return 'Short movie'
            
            else:
                return 'Long movie'
            
        except ValueError:
            return "Please enter a valid minute."
