print('Welcome to SKY traveling servieces ...')

print('[1] To view available Cities to travel ')
print('[2] To enter the city you want to travel and the view the cost ')
print('[3] To exit')

def view_cities():
    listCity = {'paris': 323, 'Istanbul': 56, 'cairo': 45,  'London':44, 'Beijing': 55}

    print(f'the available Tickets are for {listCity}')

def city_travel():
    listCity = {'paris': 323, 'Istanbul': 56, 'cairo': 45,  'London':33, 'Beijing': 55}
    city=input(' entr the city you want to travel :')
    tickets=int(input(' Number of Tiketes :'))
    print(f'Ticket price to london is { listCity[city]*tickets}')


mapchosse={
    1:view_cities,
    2:city_travel}
once=True
while once:
    choose=int(input("enter chosee"))
    if choose==3:
        once=False
    mapchosse.get(choose)()

