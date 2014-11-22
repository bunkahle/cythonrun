import math, time


def great_circle(lon1,lat1,lon2,lat2):
    radius = 3956 #miles
    x = math.pi/180.0

    a = (90.0-lat1)*(x)
    b = (90.0-lat2)*(x)
    theta = (lon2-lon1)*(x)
    c = math.acos((math.cos(a)*math.cos(b)) +
                  (math.sin(a)*math.sin(b)*math.cos(theta)))
    return radius*c

def main():
    lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826
    num = 500000
    for i in range(num):
        x = great_circle(lon1, lat1, lon2, lat2)
    return x

if __name__ == '__main__':
    start_time = time.clock()
    main()
    print time.clock() - start_time, "seconds execution time."
