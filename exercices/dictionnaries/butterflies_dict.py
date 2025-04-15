
butterflies = {'Monarch': 5,'Painted Lady': 2, 'Bronze Copeper': 12, 'Orange Sulphur': 7}

def new_sighting(butterflies, sighting):
    butterflies[sighting] = butterflies.get(sighting, 0) + 1



new_sighting(butterflies, 'Butterfly')

for key in butterflies:
    print(f'{key}: {butterflies[key]}')

# print()
