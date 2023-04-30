cities = ['London', 'Paris', 'Madrid', 'Tokyo', 'Belgrad', 'Zagreb', 'Rome']

if 'Tokyo' in cities:
    print('Gal is in Tokyo')

if 'JLM' in cities:
    print('Gal is in JLM')
elif 'Paris4' in cities:
    print('Gal is in Paris')
elif 'London' in cities:
    print('Gal is in London')
else:
    print('Gal is not in JLM')

for c in cities:
    city = c + 'S!'
    print(city)

for i in range(len(cities)):
    cities[i] += 'Q?'
print(cities)
