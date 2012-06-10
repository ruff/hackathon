import csv


def find_mpg(request):
    reader = csv.reader(open('transscraper/static/data/mpg.csv'),delimiter=',')
    car_data_found = False
    for row in reader:
        if (row[1].count(request.car_make) != 0):
            if (row[3].count(request.car_model) != 0):
                car_data = row
                car_data_found = True
                break
    
    if ( car_data_found == True ) :
        return car_data[11]
    else :
        return 21