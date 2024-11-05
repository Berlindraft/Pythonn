#Dictionary number 1
capital_data = {
    'usa': {
        'capital': 'washington, d.c.',
        'population': 692683,
        'area_km2': 177.0
    },
    'france': {
        'capital': 'paris',
        'population': 2148327,
        'area_km2': 105.4
    },
    'japan': {
        'capital': 'tokyo',
        'population': 13929286,
        'area_km2': 2194.07
    },
    'germany': {
        'capital': 'berlin',
        'population': 3669491,
        'area_km2': 891.8
    },
    'canada': {
        'capital': 'ottawa',
        'population': 1013242,
        'area_km2': 2778.13
    },
    'australia': {
        'capital': 'canberra',
        'population': 462213,
        'area_km2': 814.2
    },
    'brazil': {
        'capital': 'brasília',
        'population': 3055149,
        'area_km2': 5802.0
    },
    'india': {
        'capital': 'new delhi',
        'population': 3187000,
        'area_km2': 1483.0
    },
    'russia': {
        'capital': 'moscow',
        'population': 12615279,
        'area_km2': 2561.5
    },
    'south africa': {
        'capital': 'pretoria',
        'population': 741651,
        'area_km2': 687.54
    }
}

# display capital
# filter by population
# calculate population density
# calculate mean population
# filter capitals by name
while True:
    print('MENU')
    print('[ 1 ] Display all capitals')
    print('[ 2 ] Filter coutnries by capital population')
    print('[ 3 ] Calculate population density of capitals')
    print('[ 4 ] calculate mean population of capitals')
    print('[ 5 ] filter capitals by name')
    print('[ 6 ] EXIT')
    choice = int(input('Enter Choice: ').strip())

    if choice == 1:
        # Display all capitals
        for country, info in capital_data.items():
            print(f"{country.capitalize()}: {info['capital'].title()}")

    elif choice == 2:
        # Filter by population
        thresh = int(input('Enter a population threshold: ').strip())
        filtered = filter(lambda item: item[1]['population'] > thresh, capital_data.items())
        for country, info in filtered:
            print(f"{country.capitalize()} - Population: {info['population']}")

    elif choice == 3:
        # Calculate population density
        population_density = map(lambda item: (item[0], item[1]['population'] / item[1]['area_km2']),
                                 capital_data.items())
        for country, density in population_density:
            print(f"{country.capitalize()} - Population Density: {density:.2f} people/km²")

    elif choice == 4:
        # Calculate mean population
        populations = [info['population'] for info in capital_data.values()]
        print(populations)
        mean_population = sum(populations) / len(populations)
        print(f"Mean Population: {mean_population:.2f}")

    elif choice == 5:
        # Filter capitals by name
        substring = input('Enter a substring to filter capital names: ').strip().lower()
        filtered = filter(lambda item: substring in item[1]['capital'].lower(), capital_data.items())
        for country, info in filtered:
            print(f"{country.capitalize()} - Capital: {info['capital'].title()}")

    elif choice == 6:
        print('Exiting the program.')
        break
    else:
        print('Invalid choice. Please try again.')