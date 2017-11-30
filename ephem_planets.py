import ephem
import datetime

planets_list = ["Mars", "Moon", "Jupiter", "Neptune", "Sun"]

def planet_ephem(planet_name):
    if planet_name.capitalize() in planets_list:
        current_date = datetime.datetime.now().strftime("%y/%m/%d")
        Planet = getattr(ephem, planet_name)
        planet = Planet(current_date)
        return ephem.constellation(planet)

if __name__ == '__main__':
    print(planet_ephem(input("Сообщите название планеты на английском: \n")))

 #ephem.Mars
