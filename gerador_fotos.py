import random
import csv

lat1 = -1.305349
lon1 = -66.735202
lat2 = -1.098787
lon2 = -52.685900
lat3 = -9.355730
lon3 = -69.558837
lat4 = -10.068487
lon4 = -51.342952

min_lat = min(lat1, lat2, lat3, lat4)
max_lat = max(lat1, lat2, lat3, lat4)
min_lon = min(lon1, lon2, lon3, lon4)
max_lon = max(lon1, lon2, lon3, lon4)

num_coords = 150000
coords = []
for i in range(num_coords):
    lat = random.uniform(min_lat, max_lat)
    lon = random.uniform(min_lon, max_lon)
    sat = random.choice(['ST1', 'ST2', 'ST3', 'ST4', 'ST5'])
    dist = 0
    coords.append((lat, lon, sat, dist))

with open('fotos.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'latitude', 'longitude', 'sat', 'dist'])
    for i, coord in enumerate(coords, start=1):
        writer.writerow([i, coord[0], coord[1], coord[2], coord[3]])

print('Coordenadas geradas!!')

