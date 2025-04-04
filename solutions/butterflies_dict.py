def new_sighting(butterflies, sighting):
    butterflies[sighting] = butterflies.get(sighting, 0) + 1



butterflies = {'Monarch': 5,'Painted Lady': 2, 'Bronze Copeper': 12, 'Orange Sulphur': 7}

new_sighting(butterflies, )
for key in butterflies:
    print(f'{key}: {butterflies[key]}')

print()