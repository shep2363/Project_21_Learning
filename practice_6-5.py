<<<<<<< HEAD
# #6-5 Rivers
# rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china'}
# for river, country in rivers.items():
#     print(f"The {river.title()} runs through {country.title()}.")
# print("\nRivers:")
# for river in rivers.keys():
#     print(f"- {river.title()}")
# print("\nCountries:")
# for country in rivers.values():
#     print(f"- {country.title()}")

    


# 6-6 Polling
=======
import random


color_list = ['red', 'green', 'purple', 'black', 'orange', 'yellow', 'light blue']
speed_list = ['super slow', 'very slow', 'slow', 'slow fast', 'fast', 'very fast', 'super fast']
#Make 30 green aliens
aliens = []
>>>>>>> a2e0db8a96edc8ee63e4ac5edcdf9696f1f7a76f

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




<<<<<<< HEAD
# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#     for alien in aliens[:5]:
#         print(alien)
        

=======



        
>>>>>>> a2e0db8a96edc8ee63e4ac5edcdf9696f1f7a76f
