import csv


def find_mpg(request):
    return find_mpg(request.car_make,request.car_model)

def find_mpg(car_make, car_model):
    reader = csv.reader(open('static/data/mpg.csv'),delimiter=',')
    for row in reader:
        if (row[1].count(car_make) != 0):
            if (row[3].count(car_model) != 0):
                car_data = row
                break
    
    return car_data[11]