# Raymund Zyron Abella BSIT 2-B

# Dictionary of countries with GDP growth rates
countries = {
    "Ireland": 5.28,
    "Greece": 2.75,
    "Spain": 2.2,
    "Portugal": 2.97,
    "France": 0.77,
    "Italy": 0.99,
    "Germany": -0.33,
    "Netherlands": 0.88,
    "Poland": 0.66,
    "Sweden": -0.55,
}

# 1. Filter countries with positive growth rate
positive_growth = list(filter(lambda country: country[1] > 0, countries.items()))

# 2. Filter countries with GDP growth rate above 2%
above_2_percent = list(filter(lambda c: c[1] > 2, countries.items()))

# 3. Filter countries with GDP growth rate below 1%
below_1_percent = list(filter(lambda c: c[1] < 1, countries.items()))

# 4. Increase GDP Growth by 10% for economic projections
projected_growth = list(map(lambda c: (c[0], c[1] * 1.10), countries.items()))

# 5. Classify countries based on growth rate
# Function to classify countries based on growth rate
def classify_countries(growth):
    if growth > 2:
        return "High Growth"
    elif 0 < growth <= 2:
        return "Moderate Growth"
    else:
        return "Negative Growth"

# Using map to classify countries based on growth rate
# Using map to classify countries based on growth rate and storing it as a list of tuples
classified_countries = list(map(lambda item: (item[0], classify_countries(item[1])), countries.items()))
classification = list(map(lambda item: (item[0], 'High Growth' if item[1] > 2 else 'Moderate Growth' if 0 < item[1] <= 2 else 'Negative Growth'), countries.items()))
# Printing results
print("Classified countries based on growth rate:", classification)
# Printing results
print("Countries with positive growth rate:", positive_growth)
print("Countries with GDP growth rate above 2%:", above_2_percent)
print("Countries with GDP growth rate below 1%:", below_1_percent)
print("Projected growth rates:", projected_growth)
print("Classified countries based on growth rate:", classified_countries)


# Raymund Zyron Abella BSIT 2-B

countries = {
    "Ireland": 5.28,
    "Greece": 2.75,
    "Spain": 2.2,
    "Portugal": 2.97,
    "France": 0.77,
    "Italy": 0.99,
    "Germany": -0.33,
    "Netherlands": 0.88,
    "Poland": 0.66,
    "Sweden": -0.55,
}
# filter countries with positive growth rate
positive_gr = dict(filter(lambda country: country[1] > 0, countries.items()))
# filter countries with growth rate above 2 percent
gr_above2 = list(filter(lambda country: country[1] > 2, countries.items()))
# filter countries with growth rate below 1 percent
gr_below1 = list(filter(lambda country: country[1] < 1, countries.items()))
# shows the projected growth rate of 10 percent of the countries growth rate
projected_gr = list(map(lambda country: (country[0], country[1] * 1.1), countries.items()))
# classifies the countires based on the growth rate percentage
classified_countries = list(map(lambda country: (country[0], 'High Growth' if country[1] > 2 else 'Moderate Growth' if 0 < country[1] <= 2 else 'Negative Growth'), countries.items()))
print("===============================================")
print("Countries with positive growth rate: \n")
for y in positive_gr:
    print(y, positive_gr[y])
print(positive_gr)
print(countries["Sweden"])
# print("===============================================")
# print("Countries with growth rate above 2%: \n", gr_above2)
# print("===============================================")
# print("Countries with growth rate above 1%: \n", gr_below1)
# print("===============================================")
# print("Increased GDP for economic projections: \n", projected_gr)
# print("===============================================")
# print("Classification of Countries based on growth rate: \n", classified_countries)
