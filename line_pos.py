import sqlite3
import csv

conn = sqlite3.connect('./DB/tranz.sqlite')
conn.text_factory = str
c = conn.cursor()

conStr = lambda x: [str(r) for r in x]

def import_trips_csv():
    f = csv.reader(open('./RwaData/trips.txt'))
    res = {}
    f.next()
    for row in f:
        res[row[2]] = (tuple(row))
    return res

trips = import_trips_csv()

def Query(sql):
	print sql
	c.execute(sql)
	l = c.fetchall()
	print len(l)
	return l

def GetFirst(l):
	return [r[0] for r in l]

def getRoutesIds(bus_line):
	sql = 'select id from routes where bus_num = {0}'.format(bus_line)
	c.execute(sql)
	l = c.fetchall()
	return [r[0] for r in l]

def getTripsIdsfromRoutes(routes_ids):
    sql = 'select service_id from trips where route_id in {0}'.format(tuple(routes_ids))
    l = GetFirst(Query(sql))
    return l

def getServiceIdsFromTripsIds(trips_ids):
    sql = 'select service_id from trips where id in {0}'.format(tuple(trips_ids))
    #l = GetFirst(Query(sql))
    getService = lambda x: trips[x][1]
    l = []
    for i in trips_ids:
        l.append(getService(i))
    return l

def getServiceIdsinDay(fullService_ids, day):
	sql = 'select service_id from calendar where {0} = 1 and service_id in {1}'.format(day,tuple(fullService_ids))
	print sql
	c.execute(sql)
	l = c.fetchall()
	return [r[0] for r in l]

def getShapesIdsfromIds(ids):
    print len(ids)
    print len(trips)
    sql = 'select distinct shape_id from trips where id in {0}'.format(tuple(ids))
    #l = GetFirst(Query(sql))
    l = set()
    getShape = lambda x: trips[x][4]
    for i in ids:
        l.add(getShape(i))
    return l

def getTripIds(colum,value):
    sql = 'select distinct id from trips where {0} in {1}'.format(colum,tuple(value))
    return conStr(GetFirst(Query(sql)))

trip_ids = getTripIds('Route_id',getRoutesIds(921))
service_ids = getServiceIdsFromTripsIds(trip_ids)
service_ids = getServiceIdsinDay(service_ids, 'sunday')
trip_ids = getTripIds('Service_id',service_ids)
pl = getShapesIdsfromIds(trip_ids)
print len(pl)

c.close()
conn.close()
