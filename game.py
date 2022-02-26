print("""
   welcome to the world game  |
   IF YOU WANT to know the play 
   enter the Capital for esch country |
""")
city = {"iraq": "baghdad", "egypt": "cairo", "china": "beiging", "jordan": "amman"}
star = input(' do you want to start (Y/N) : ')
start=True
while start and star.upper()=='Y':
   try:
       countr = input("Enter country name : ")
       print(f'The  Capital of {countr} is {city[countr]}')
       star = input(' do you want to start (Y/N) : ')
       if star.upper() == "N":
           start = False
   except:
       print("error ...try agine")

if star==False:
    print("Thank you to use World Expert have a nice day ")
else:
   print("we hope to try the game later")