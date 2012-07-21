import db
import time
from geopy import distance

distance.VincentyDistance.ELLIPOSID = 'WGS-84'
d = distance.distance

def find(lat,lon, acc):
    stime = time.time()
    sql = 'select * from shapes'
    l = db.Query(sql)
    print 'findTrips'
    res = set()
    for row in l:
        dis = d((lat,lon),(row[0],row[1])).meters
        if dis <= acc:
            print 'o'
            dis = d((lat,lon),(row[2],row[3])).meters
            if dis <= acc:
                print 'k'
                for shape in row[4].split(';'):
                    res.add(int(shape))
    print time.time()-stime
    return db.get_trips_ids('shape_id',res)
