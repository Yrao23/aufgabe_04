# -*- coding: utf-8 -*-
"""
Created on Thu May 11 16:04:39 2023

@author: yoges
"""

from numpy import sin, cos, arccos, pi

print("In dieser Program wird der Distanz zwischen zwei Flugrouten berechnet\n")

airports = {
    "Berlin":  {
        "lat": 52.365,
        "lon": 13.51,
        "zielflughaefen": ["Marrakesch", "Montreal"],
        },
    "Marrakesch": {
        "lat": 31.6,
        "lon": -8.025,
        "zielflughaefen": ["Berlin", "Lima", "Montreal"],
        },
    "Montreal": {
        "lat": 45.67,
        "lon": -74.04,
        "zielflughaefen": ["Berlin", "Marrakesch", "Lima", "Ulaanbaatar"],
        },
    "Lima": {
        "lat": -12.02,
        "lon": -77.11,
        "zielflughaefen": ["Marrakesch", "Montreal"],
        },
    "Ulaanbaatar": {
        "lat": 47.85,
        "lon": 106.76,
        "zielflughaefen": ["Montreal"],
        }
}
airports_total = (airports.keys())
print("Mögliche Startflughäfen: ", end='')
for x in airports_total:
    print(x, end=' ')
print("\n")   
start_input = (input("Bei welchem von oben genannten Flughäfen möchten Sie starten: "))
#print("\n")

if start_input in airports:
    lat1 = airports[start_input]["lat"]
    lon1 = airports[start_input]["lon"]
    zielflughaefen = airports[start_input]["zielflughaefen"]
    print("\nzielflughäfen: ", end='')
    for x in zielflughaefen:
        print(x, end=' ')
    print("\n")    
    zielflughafen_input = input("Bitte geben von oben gegebenen Zielflughäfen ihrer Zielflughafen ein: ") 
    if zielflughafen_input in zielflughaefen:
        lat2 = airports[zielflughafen_input]["lat"]
        lon2 = airports[zielflughafen_input]["lon"]
        orthod = arccos(sin(lat1*pi/180)*sin(lat2*pi/180) + cos(lat1*pi/180)*cos(lat2*pi/180)*cos(abs(lon2*pi/180-lon1*pi/180)))
        distanz = 6371*orthod
        print("\nDistanz (in km): ", round(distanz))
        print("\nDer Program hat sich beendet.")
    else: print("Fehler: eingegebener Flughafen existiert nicht oder wird vom Startflughafen nicht angeflogen!")    
else:
    print("\nFehler: unbekannter Flughafen!")
        