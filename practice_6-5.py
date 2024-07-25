#6-5 Rivers
rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china'}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print("\nRivers:")
for river in rivers.keys():
    print(f"- {river.title()}")
print("\nCountries:")
for country in rivers.values():
    print(f"- {country.title()}")

    


#6-6 Polling

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}    

people = ['jen', 'sarah', 'edward', 'phil', 'colden', 'john', 'brandon', 'jane']

for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take the poll!")



#Practice

names = ['Colden', 'John', 'Brandon', 'Jane', 'Jen', 'Sarah', 'Edward', 'Phil']

for name in names:
    if name.lower() in favorite_languages.keys():
        print(f"Thank you for taking the poll, {name.title()}!")
    else:
        print(f"{name.title()}, please take the poll!")

        