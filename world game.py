def stat_Stop():
    start = input(' do you want to start (Y/N) : ')
    if start.upper() == "N":
        return False
    if start.upper() == "Y":
        return True

    if start.upper() != "N" and start.upper() != "Y":
        print("error ... write again")
        return stat_Stop()

print("""
   welcome to the world game  |
   IF YOU WANT to know the play 
   enter the Capital for esch country |
""")
city = {"iraq": "baghdad", "egypt": "cairo", "china": "beiging", "jordan": "amman"}

start=stat_Stop()
loop=True
while start and loop:
    try:
        countr = input("Enter country name : ")
        print(f'The  Capital of {countr} is {city[countr]}')
        if not stat_Stop():
            loop = False
    except:
        print("countr is not found in data base ...")

if loop==False:
    print("Thank you to use World Expert have a nice day ")
else:
   print("we hope to try the game later")





