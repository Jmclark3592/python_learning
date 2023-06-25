cars = ['bmw', 'audi', 'toyota']

print(cars[0].title()) #prints Honda

cars.append('subaru') #adds to back of list ['honda', 'yamaha', 'suzuki', ducati]
cars.insert(0, 'subaru') #adds to the front of the list
del cars[0] #removes index 1 from the list and the program (irretreivable)
popped_car = cars.pop(0) #moves index 1 to popped_motorcycle as a variable to be used again
popped_car = cars.pop() #moves the last item on the list to popped_motorcycle as a variable
cars.sort() #puts list in alphabetical order (permanently)
cars.reverse() #reverses current order of a list