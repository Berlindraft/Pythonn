
# Dictiony number 3
asean_countries = {
    'brunei': ['bandar seri begawan', 445373, 5765],
    'cambodia': ['phnom penh', 17100000, 181035],
    'indonesia': ['jakarta', 273753191, 1904569],
    'laos': ['vientiane', 7351000, 236800],
    'malaysia': ['kuala lumpur', 33181072, 330803],
    'myanmar': ['naypyidaw', 54339766, 676578],
    'philippines': ['manila', 114097000, 300000],
    'singapore': ['singapore', 5612000, 728.6],
    'thailand': ['bangkok', 71510000, 513120],
    'vietnam': ['hanoi', 100862980, 331212]
}

# Display menu
while True:
    print('\nMENU')
    print('[ 1 ] Display all ASEAN countries')
    print('[ 2 ] Filter countries by population size')
    print('[ 3 ] Calculate population density for each country')
    print('[ 4 ] Calculate mean population across all countries')
    print('[ 5 ] Find ASEAN countries by name substring')
    print('[ 6 ] EXIT')
    choice = int(input('Enter your choice: ').strip())

    if choice == 1:
        # Display all ASEAN countries with population and area
        for country, data in asean_countries.items():
            print(f"{country.capitalize()}: Capital: {data[0]}, Population: {data[1]}, Area: {data[2]} km²")

    elif choice == 2:
        # Filter countries by population size
        threshold = int(input("Enter the population threshold: ").strip())
        filtered = filter(lambda item: item[1][1] > threshold, asean_countries.items())
        for country, data in filtered:
            print(f"{country.capitalize()} - Population: {data[1]}")

    elif choice == 3:
        # Calculate population density for each country (population/area)
        population_density = map(lambda item: (item[0], item[1][1] / item[1][2]), asean_countries.items())
        for country, density in population_density:
            print(f"{country.capitalize()} - Population Density: {density:.2f} people per km²")

    elif choice == 4:
        # Calculate mean population across all ASEAN countries
        populations = [data[1] for data in asean_countries.values()]
        mean_population = sum(populations) / len(populations)
        print(f"Mean Population across all ASEAN countries: {mean_population:.2f}")


    elif choice == 5:
        # Find ASEAN countries by name substring
        substring = input("Enter a substring to search for: ").strip().lower()
        filtered_countries = filter(lambda item: substring in item[0].lower(), asean_countries.items())
        for country, data in filtered_countries:
            print(f"{country.capitalize()} - Capital: {data[0]}")

    elif choice == 6:
        print('Exiting the program.')
        break

    else:
        print('Invalid choice. Please try again.')