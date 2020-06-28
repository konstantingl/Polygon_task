import csv
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def main():

    #Load data about restaurants
    id1,x1,y1 = load_data('place_zone_coordinates.csv')

    coord_list = list(zip(x1,y1))
    coord_list_tuples = [coord_list[i:i + 4] for i in range(0,len(coord_list),4)]
    coord_list_lists = []
    for i in range(len(coord_list_tuples)):
        coord_list = [element for element in coord_list_tuples[i]]
        coord_list_lists.append(coord_list)

    #Create polygons
    polygons = []
    for coords in coord_list_lists:
        print (coords)
        polygon = Polygon(coords)
        polygons.append(polygon)

    #Load data about users
    id2,x2,y2 = load_data('users_coordinates.csv')
    users_coords = list(zip(x2,y2))
    users_data = {id2: user_coords for id2,user_coords in zip(id2,users_coords)}

    #Check if users' coordinates are in the polygon
    available_places = [['id','number_of_places_available']]
    for key in users_data:
        count = 0
        for polygon in polygons:
            if polygon.contains(Point(users_data[key])):
                count =+ 1
        available_places.append(list((key,count)))
    print(available_places)

    #Write csv file with output
    with open('result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(available_places)


def load_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        id = []
        x = []
        y = []

        for row in reader:
            id.append(int(row[0]))
            x.append(float(row[1]))
            y.append(float(row[2]))


    return (id,x,y)

if __name__ == "__main__":
    main()
