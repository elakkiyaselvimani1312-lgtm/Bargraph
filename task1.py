import pandas as pd
import matplotlib.pyplot as plt

# Read dataset correctly
data = pd.read_csv(
    "API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv",
    skiprows=4
)

# Take first 10 countries
countries = data['Country Name'].head(10)

# Population values for 2022
population = data['2022'].head(10)

# Create bar chart
plt.figure(figsize=(10,5))
plt.bar(countries, population)

# Labels and title
plt.title("Population Distribution")
plt.xlabel("Countries")
plt.ylabel("Population")

# Rotate country names
plt.xticks(rotation=45)

# Show graph
plt.show()