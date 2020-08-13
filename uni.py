import random
random.seed
import pyperclip
Numbers = random.randint(10 , 99)
print('Please choose a option')
print('1. Cities 2. Countries, 3. Animals')
option = input()
Colors = ['Red', 'White', 'Black', 'Green', 'Orange']
Symbols = ['?', '!', '$', '#', '@']
PW = ''
if option == '1':
    print("Do you want North or South California classification? ")
    CitiesOption = input()
    if CitiesOption == "North" or CitiesOption == "north":
        NorthCities = ['SanJose', 'Fresno', 'OakLand', 'Modesto', 'Fremont']
        PW = (random.choice(Colors) + random.choice(NorthCities) + (str(Numbers)) + random.choice(Symbols))
        print(PW)
        pyperclip.copy(PW)
    if CitiesOption == 'South' or CitiesOption == 'south':
        SouthCities = ['LosAngeles', 'SanDiego', 'Burbank', 'Glendale', 'Tujunga']
        PW = (random.choice(Colors) + random.choice(SouthCities) + (str(Numbers)) + random.choice(Symbols))
        print(PW)
        pyperclip.copy(PW)

if option == '2':
    Countries = ['Colombia', 'Finland', 'Armenia', 'Germany', 'England']
    PW = (random.choice(Colors) + random.choice(Countries) + (str(Numbers)) + random.choice(Symbols))
    print(PW)
    pyperclip.copy(PW)
if option == '3':
    Animals = ['Cheetah', 'Penguin', 'Octopus', 'Monkey', 'Panther']
    PW = (random.choice(Colors)+random.choice(Animals)+(str(Numbers))+random.choice(Symbols))
    print(PW)
    pyperclip.copy(PW)

input('Press ENTER to exit')
