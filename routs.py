import db

def find(bus_line):
    sql = 'select id from routes where bus_num = {0}'.format(bus_line)
    ids = db.First(db.Query(sql))
    return db.get_trips_ids('route_id',ids)
