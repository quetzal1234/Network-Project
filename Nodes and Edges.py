name = input('Please type your name and press Enter.')
print('Hi', name, 'this program will tell you the shortest route to your desired destination in the zoo.')
while True:
    print('Your input options are: Bird House, Polar Bear Point, Sea Lion Sound, Insectarium, Rivers Edge, Quit')
    command = input('Type the location of your choice and press Enter.')
    if len(command) < 1: #check prevents a crash
        continue
    #command = (command[ ]) #print(type(command) == str) in Python
    else:
        if command in ['quit', 'Quit']:
            print('All done now, bye!')
            break #exit the loop, which will quit the program
        elif command in ['bird house', 'Bird House']:
            length = 5
            print('The shortest distance to your location is', length, 'meters.')
        elif command in ['polar bear point', 'Polar Bear Point']:
            length = 12
            print('The shortest distance to your location is', length, 'meters.')
        elif command in ['rivers edge', 'Rivers edge']:
            length = 15
            print('The shortest distance to your location is', length, 'meters.')
        elif command in ['sea lion sound', 'Sea Lion Sound']:
            length = 24
            print('The shortest distance to your location is', length, 'meters.')
        elif command in ['insectarium', 'Insectarium']:
            length = 29
            print('The shortest distance to your location is', length, 'meters.')
        else:
            print('Unrecognized option! Please try again.')
            continue #restart at the top of the loop.
