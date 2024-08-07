import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)

    if response.status_code == 200:
        planets = response.json()['bodies']

        heaviest_planet = None
        longest_orbit_planet = None
        max_mass = 0
        max_orbit_period = 0

        # Process each planet info
        for planet in planets:
            if planet['isPlanet']:
                name = planet.get('englishName', 'N/A')
                mass_value = planet.get('mass', {}).get('massValue', 'N/A')
                mass_exponent = planet.get('mass', {}).get('massExponent', 0)
                mass = mass_value * 10**mass_exponent if mass_value != 'N/A' else 'N/A'
                orbit_period = planet.get('sideralOrbit', 'N/A')

                # Print each planet's details
                print(f"Planet: {name}, Mass: {mass} kg, Orbit Period: {orbit_period} days")

                # Check for heaviest planet
                if mass != 'N/A' and mass > max_mass:
                    max_mass = mass
                    heaviest_planet = name

                # Check for planet with longest orbit period
                if orbit_period != 'N/A' and orbit_period > max_orbit_period:
                    max_orbit_period = orbit_period
                    longest_orbit_planet = name

        # Print analysis results
        print("\nAnalysis Results:")
        print(f"Heaviest Planet: {heaviest_planet}, Mass: {max_mass} kg")
        print(f"Planet with Longest Orbit Period: {longest_orbit_planet}, Orbit Period: {max_orbit_period} days")

    else:
        print(f"Failed to get data. Status code: {response.status_code}")

fetch_planet_data()

