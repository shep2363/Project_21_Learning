import random


color_list = ['red', 'green', 'purple', 'black', 'orange', 'yellow', 'light blue']
speed_list = ['super slow', 'very slow', 'slow', 'slow fast', 'fast', 'very fast', 'super fast']
#Make 30 green aliens
aliens = []

for alien_number in range(30):
    color = random.choice(color_list)
    point = random.randint(5,50)
    speed = random.choice(speed_list)
    new_alien = {'color': color,
                 'point': point, 
                 'speed': speed}
    aliens.append(new_alien)

 
for alien in aliens[:5]:
    print(alien)

print(f'Total number of aliens: {len(aliens)}')







        