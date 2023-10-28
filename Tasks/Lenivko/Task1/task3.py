# This program converts the km\h into m\sec.

speed = int(input('Enter your speed, please ' ))
conv_speed = (speed * 1000) / 3600
print(f'{speed} km/h equals {round(conv_speed, 2)} m/sec')