import requests

# Test connection
response = requests.get('http://www.google.com')
print(response.status_code)

# Retrieve current astronauts
response = requests.get('http://api.open-notify.org/astros.json')
data = response.json()

print("There are currently", data["number"], "people in space:")

for person in data["people"]:
    print(person["name"], "is on", person["craft"])

# Test Star Wars API
response = requests.get('https://swapi.dev/api/people/1/')
print(response.status_code)

# Print raw response
print(response.text)

# Format Star Wars response
data = response.json()

print("\n--- STAR WARS CHARACTER ---")
print("Name:", data["name"])
print("Height:", data["height"], "cm")
print("Weight:", data["mass"], "kg")
print("Hair Color:", data["hair_color"])
print("Eye Color:", data["eye_color"])
print("Birth Year:", data["birth_year"])
print("Gender:", data["gender"])