
#dictionary number 2
gdp_growth_2023 = {
    'usa': {
        'q1': 1.8,
        'q2': 2.1,
        'q3': 2.3,
        'q4': 2.0
    },
    'germany': {
        'q1': 0.0,
        'q2': -0.3,
        'q3': -0.1,
        'q4': 0.2
    },
    'china': {
        'q1': 4.5,
        'q2': 6.3,
        'q3': 4.9,
        'q4': 5.2
    },
    'india': {
        'q1': 6.1,
        'q2': 7.8,
        'q3': 6.3,
        'q4': 6.5
    },
    'brazil': {
        'q1': 1.9,
        'q2': 3.0,
        'q3': 2.5,
        'q4': 2.7
    },
    'uk': {
        'q1': 0.1,
        'q2': 0.2,
        'q3': 0.3,
        'q4': 0.4
    },
    'japan': {
        'q1': 2.7,
        'q2': 4.8,
        'q3': 4.0,
        'q4': 4.2
    },
    'south korea': {
        'q1': 0.3,
        'q2': 0.9,
        'q3': 1.1,
        'q4': 1.2
    },
    'canada': {
        'q1': 0.8,
        'q2': -0.2,
        'q3': 0.4,
        'q4': 0.6
    },
    'australia': {
        'q1': 0.2,
        'q2': 0.4,
        'q3': 0.6,
        'q4': 0.5
    }
}
# Display menu
while True:
    print('\nMENU')
    print('[ 1 ] Display all GDP growth')
    print('[ 2 ] Filter countries by GDP growth in a specific quarter')
    print('[ 3 ] Calculate average GDP growth for each country')
    print('[ 4 ] Calculate overall mean GDP growth across all countries')
    print('[ 5 ] Sort countries by average GDP growth')
    print('[ 6 ] EXIT')
    choice = int(input('Enter your choice: ').strip())

    if choice == 1:
        # Display GDP Growth for all quarters
        for country, growth in gdp_growth_2023.items():
            print(
                f"{country.capitalize()}: Q1: {growth['q1']}%, Q2: {growth['q2']}%, Q3: {growth['q3']}%, Q4: {growth['q4']}%")

    elif choice == 2:
        # Filter by GDP growth in a specific quarter
        quarter = input("Enter the quarter (q1, q2, q3, q4): ").strip().lower()
        threshold = float(input("Enter the GDP growth threshold: ").strip())
        filtered = filter(lambda item: item[1][quarter] > threshold, gdp_growth_2023.items())
        for country, growth in filtered:
            print(f"{country.capitalize()} - {quarter.upper()}: {growth[quarter]}%")

    elif choice == 3:
        # Calculate average GDP growth for each country
        average_growth = map(lambda item: (item[0], sum(item[1].values()) / 4), gdp_growth_2023.items())
        for country, avg_growth in average_growth:
            print(f"{country.capitalize()} - Average GDP Growth: {avg_growth:.2f}%")

    elif choice == 4:
        # Calculate overall mean GDP growth
        all_gdp_growth = [sum(growth.values()) / 4 for growth in gdp_growth_2023.values()]
        overall_mean = sum(all_gdp_growth) / len(all_gdp_growth)
        print(f"Overall Mean GDP Growth: {overall_mean:.2f}%")

    elif choice == 5:
        # Sort countries by average GDP growth
        sorted_countries = sorted(gdp_growth_2023.items(), key=lambda item: sum(item[1].values()) / 4, reverse=True)
        for country, growth in sorted_countries:
            avg_growth = sum(growth.values()) / 4
            print(f"{country.capitalize()} - Average GDP Growth: {avg_growth:.2f}%")


    elif choice == 6:
        print('Exiting the program.')
        break
    else:
        print('Invalid choice. Please try again.')

