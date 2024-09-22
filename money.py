from movie import Movie

class Money:
    def __init__(self, current_money):
        self.current_money = current_money

    def get_money(self):
        return self.current_money

    def set_money(self, movie):
        if int(self.current_money) >= movie.price:
            self.current_money = int(self.current_money) - int(movie.price)
            return(f"Bilet aldiniz. Qalan pulunuz: {self.current_money}")
        else:
            print("Pulunuz yeterli deyil")