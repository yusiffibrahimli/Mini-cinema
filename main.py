from mall import *
from human import Worker, NormalPerson
from movie import * 
from money import *
print("""
Write your personal information
      
Worker or any employer ? - 1
Normal person ? - 2
"""
)

try:
    person_selection = int(input("Your selection: "))
    
except :
    exit("Enter valid value")

if person_selection == 1:
    person = Worker()
    print(person.who())

elif person_selection == 2:
    person = NormalPerson()
    print(person.who())
else:
    exit('Wrong input')

print("""
1 - Ganjlik Mall
2 - Deniz Mall
3 - Aygun Mall
4 - Nizami Mall
5 - Ganca Mall
"""
)

try:
    mall_selection = int(input("Your selection: "))
    
except :
    exit("Enter valid value")

ganjlik = GanjlikMall('Genclik',6,7)
deniz = DenizMoll('Bulvar',6,7)
aygun = AygunMoll('Neftciler',6,7)
nizami = NizamiMoll('Nizami',6,7)
gence = GancaMoll('Gence',6,7)


if mall_selection == 1:
    print(ganjlik.hours_info())
    ganjlik.age_info(age=int(input()))
    ganjlik.vaccinate_info(status=input('Vaksinasiya Active/: '))
    
elif mall_selection == 2:
    print(deniz.hours_info())
    deniz.age_info(age=int(input()))
    deniz.vaccinate_info(status=input('Vaksinasiya Active/: '))

elif mall_selection == 3:
    print(aygun.hours_info())
    aygun.age_info(age=int(input()))
    aygun.vaccinate_info(status=input('Vaksinasiya Active/: '))

elif mall_selection == 4:
    print(nizami.hours_info())
    nizami.age_info(age=int(input()))
    nizami.vaccinate_info(status=input('Vaksinasiya Active/: '))


elif mall_selection == 5:
    print(gence.hours_info())
    gence.age_info(age=int(input()))
    gence.vaccinate_info(status=input('Vaksinasiya Active/: '))

else:
    exit('Wrong input')

seans1 = Hours('10:00','12:00')
seans2 = Hours('12:00','14:00')
seans3 = Hours('14:00','16:00')
seans4 = Hours('18:00','20:00')

film1 = Movie("Inception","Christopher Nolan", "2010", "Sci-Fi, Action", 148, 8.8, [seans1,seans4], 7)
film2 = Movie("The Shawshank Redemption","Frank Darabont", "1994", "Drama", 142, 9.3,[seans2,seans4], 4)
film3 = Movie("The Godfather","Francis Ford Coppola", "1972", "Crime, Drama", 175 , 9.2,[seans1,seans2] ,6)
film4 = Movie("Pulp Fiction","Quentin Tarantino", "1994", "Crime, Drama", 154 , 8.9,[seans3,seans4],10)
film5 = Movie("Forrest Gump","Robert Zemeckis", "1994", "Drama, Romance", 142 , 8.8,[seans1,seans4],9)
film6 = Movie("The Dark Knight","Christopher Nolan", "2008", "Action, Drama", 152 , 9.1,[seans2,seans3],8)

print("""
Inception - 1
The Shawshank Redemption - 2
The Godfather - 3
Pulp Fiction - 4
Forrest Gump - 5
The Dark Knight - 6
""")

secim = int(input('Seciminiz: '))

if secim == 1:
    print(film1.show_info())
    print(film1.year_info())
    print(film1.rating_info())
    print(film1.duration_info())


    for i in range(len(film1.hours)):
        print(str(f'{film1.hours[i].start_time}'), str(film1.hours[i].end_time))
    secim = int(input('Seans secin : '))
    if secim == 1:
        print(film1.hours[i-1].start_time,film1.hours[i-1].end_time)
    elif secim == 2:
        print(film1.hours[i].start_time,film1.hours[i].end_time)

    answer = input("Do you want to buy a ticket? (Yes/No): ")
    if answer.lower() == "yes":
        try:
            amount = input("Please enter the amount of money you want to spend: ")
            print(Money(amount).get_money())
            print(Money(amount).set_money(film1))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    else:
        print("Okay, have a nice day!")
    
elif secim == 2:
    print(film2.show_info())
    print(film2.year_info())
    print(film2.rating_info())
    print(film2.duration_info())

    for i in range(len(film1.hours)):
        print(str(f'{film1.hours[i].start_time}'), str(film1.hours[i].end_time))
    secim = int(input('Seans secin : '))
    if secim == 1:
        print(film1.hours[i-1].start_time,film1.hours[i-1].end_time)
    elif secim == 2:
        print(film1.hours[i].start_time,film1.hours[i].end_time)

    answer = input("Do you want to buy a ticket? (Yes/No): ")
    if answer.lower() == "yes":
        try:
            amount = input("Please enter the amount of money you want to spend: ")
            print(Money(amount).get_money())
            print(Money(amount).set_money(film1))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    else:
        print("Okay, have a nice day!")        

elif secim == 3:
    print(film3.show_info())
    print(film3.year_info())
    print(film3.rating_info())
    print(film3.duration_info())

    for i in range(len(film1.hours)):
        print(str(f'{film1.hours[i].start_time}'), str(film1.hours[i].end_time))
    secim = int(input('Seans secin : '))
    if secim == 1:
        print(film1.hours[i-1].start_time,film1.hours[i-1].end_time)
    elif secim == 2:
        print(film1.hours[i].start_time,film1.hours[i].end_time)

    answer = input("Do you want to buy a ticket? (Yes/No): ")
    if answer.lower() == "yes":
        try:
            amount = input("Please enter the amount of money you want to spend: ")
            print(Money(amount).get_money())
            print(Money(amount).set_money(film1))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    else:
        print("Okay, have a nice day!")

elif secim == 4:
    print(film4.show_info())
    print(film4.year_info())
    print(film4.rating_info())
    print(film4.duration_info())

    for i in range(len(film1.hours)):
        print(str(f'{film1.hours[i].start_time}'), str(film1.hours[i].end_time))
    secim = int(input('Seans secin : '))
    if secim == 1:
        print(film1.hours[i-1].start_time,film1.hours[i-1].end_time)
    elif secim == 2:
        print(film1.hours[i].start_time,film1.hours[i].end_time)

    answer = input("Do you want to buy a ticket? (Yes/No): ")
    if answer.lower() == "yes":
        try:
            amount = input("Please enter the amount of money you want to spend: ")
            print(Money(amount).get_money())
            print(Money(amount).set_money(film1))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    else:
        print("Okay, have a nice day!")
    
elif secim == 5:
    print(film5.show_info())
    print(film5.year_info())
    print(film5.rating_info())
    print(film5.duration_info())

    for i in range(len(film1.hours)):
        print(str(f'{film1.hours[i].start_time}'), str(film1.hours[i].end_time))

    secim = int(input('Seans secin : '))
    if secim == 1:
        print(film1.hours[i-1].start_time,film1.hours[i-1].end_time)
    elif secim == 2:
        print(film1.hours[i].start_time,film1.hours[i].end_time)

    answer = input("Do you want to buy a ticket? (Yes/No): ")
    if answer.lower() == "yes":
        try:
            amount = input("Please enter the amount of money you want to spend: ")
            print(Money(amount).get_money())
            print(Money(amount).set_money(film1))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    else:
        print("Okay, have a nice day!")

elif secim == 6:
    print(film6.show_info())
    print(film6.year_info())
    print(film6.rating_info())
    print(film6.duration_info())

    for i in range(len(film1.hours)):
        print(str(f'{film1.hours[i].start_time}'), str(film1.hours[i].end_time))
    secim = int(input('Seans secin : '))
    if secim == 1:
        print(film1.hours[i-1].start_time,film1.hours[i-1].end_time)
    elif secim == 2:
        print(film1.hours[i].start_time,film1.hours[i].end_time)

    answer = input("Do you want to buy a ticket? (Yes/No): ")
    if answer.lower() == "yes":
        try:
            amount = input("Please enter the amount of money you want to spend: ")
            print(Money(amount).get_money())
            print(Money(amount).set_money(film1))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    else:
        print("Okay, have a nice day!")

