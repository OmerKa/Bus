from geopy import distance
import math
distance.VincentyDistance.ELLIPOSID = 'WGS-84'
d = distance.distance

import sqlite3

def CalcDistance(start, end):
    m = math.sqrt(((start[0] - end[0]) **2) + ((start[1]-end[1]) **2))
    print m
    return m

conn = sqlite3.connect('./DB/tranz.sqlite')

def findTrips(lat,lon, acc):
    print 'findTrips'
    res = set()
    c = conn.execute('select * from shapes')
    l = c.fetchall()
    print len(l)
    for row in l:
		#dis = d((lat,lon),(row[0],row[1])).meters
        print ((lat,lon),row[0],row[1])
        dis = CalcDistance((lat,lon),(row[0],row[1]))
        if dis <= acc:
            print 'o'
			#dis = d((lat,lon),(row[2],row[3])).meters
            dis = CalcDistance((lat,lon),(row[2],row[3]))
            if dis <= acc:
                print 'k'
                for shape in row[4].split(';'):
                    res.add(int(shape))
	print res
	return res

def getRoutsFromShapes(shapes):
	print('Shapes:' + str(len(shapes)))
	res = set()
	for trip in shapes:
		sql = 'select route_id from trips where shape_id like ' + str(trip)
		print sql
		c = conn.execute(sql)
		l = c.fetchall()
		for row in l:
			res.add(row[0])
	return res

def getBusFromRoutes(routes):
	print routes
	print 'Routes:' + str(len(routes))
	res = set()
	for route in routes:
		sql = 'select bus_num from routes where id like ' + str(route)
		print sql
		c = conn.execute(sql)
		l = c.fetchall()
		for row in l:
			res.add(row[0])
	return res

def find(lat,lon,acc):
	return getBusFromRoutes(getRoutsFromShapes(findTrips(lat,lon,acc)))

print find(32.303212,34.900451,100)
