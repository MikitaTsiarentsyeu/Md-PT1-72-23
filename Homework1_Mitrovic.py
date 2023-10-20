
import  math
import random

#Write a program that converts Celsius to Fahrenheit, ask a user for the Celsius value.

cel=int(input('Enter the value of grad in celsius: '))
fahr=(cel*1.8)+32
print('The value in Fahrenheit is ', fahr,'°')

#Write a program that calculates the area of a circle given its radius, ask a user for the radius.

radius=int(input('Enter the radius of the circle: '))
area_circle=math.pi*radius**2
print('Area of a circle is ', area_circle,'cm2')

#Write a program that converts kilometers per hour to meters per second, ask a user for the speed

speed_km=int(input('Enter the speed in km per h: '))
speed_m=round(speed_km/3.6)
print('Speed in meters per second is: ',speed_m,'meter per second')

#Write a program that converts some amount of money from USD to BYN, ask a user for the amount,
# store the ratio inside the program itself

amount_money=int(input('Enter some amount of dollars:  '))
ratio_dol_to_br=1*3.3
print('You get',ratio_dol_to_br*amount_money,'belarusian rubles')

#Write a program that generates a random number in a given range, and shows the answer to a user,
# ask a user for the left and right border.

a=random.randint(2,34)
print('The random value is: ',a)







