import random
random.seed
Numbers = random.randint(10 , 99)
print('Please choose a option')
print('1. Cities 2. Countries, 3. Animals')
option = input()
Colors = ['Red', 'White', 'Black', 'Green', 'Orange']
Symbols = ['?', '!', '$', '#', '@']
if option == '1':
    print("Do you want North or South California classification? ")
    CitiesOption = input()
    if CitiesOption == "North" or CitiesOption == "north":
        NorthCities = ['SanJose', 'Fresno', 'OakLand', 'Modesto', 'Fremont']
        print(random.choice(Colors)+random.choice(NorthCities)+(str(Numbers))+random.choice(Symbols))
    if CitiesOption == 'South' or CitiesOption == 'south':
        SouthCities = ['LosAngeles', 'SanDiego', 'Burbank', 'Glendale', 'Tujunga']
        print(random.choice(Colors) + random.choice(SouthCities)+(str(Numbers))+random.choice(Symbols))

if option == '2':
    Countries = ['Colombia', 'Finland', 'Armenia', 'Germany', 'England']
    print(random.choice(Colors)+random.choice(Countries)+(str(Numbers))+random.choice(Symbols))

if option == '3':
    Animals = ['Cheetah', 'Penguin', 'Octopus', 'Monkey', 'Panther']
    print(random.choice(Colors) + random.choice(Animals) + (str(Numbers)) + random.choice(Symbols))