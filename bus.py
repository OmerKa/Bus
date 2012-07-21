import place
import calendar
import routs


class user:
    def __init__(self, lat, lon, acc, bus_num):
        self.lat = lat
        self.lon = lon
        self.acc = acc
        self.bus_num = bus_num

    def find(self):
        t1 = routs.find(self.bus_num)
        print len(t1)
        t2 = calendar.find('sunday')
        print len(t2)
        t3 = place.find(self.lat,self.lon,self.acc)
        print len(t3)
        return set(t1).intersection(set(t2)).intersection(set(t3))
    
res = user(32.303212,34.900451,100,921)
r = res.find()
print len(r)
