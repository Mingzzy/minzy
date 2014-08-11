from datetime import timedelta, datetime, tzinfo


class KST(tzinfo):

    def utcoffset(self, dt):
        return timedelta(hours=9)

    def dst(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return "(UTC+09:00)"


class Database(object):

    def __init__(self):
        self.database = [

            {
                'id': 1,
                'title': "likelion",
                'contents': "likelion2 homepage",
                'url': "http://likelion.net/",
                'time': "2014-08-04 14:16:53.839000+09:00",
                'likecount': 0,
            }]

    def maxid(self):
        _id = -1
        for item in self.database:
            if _id < item['id']:
                _id = item['id']
        return _id

    def newid(self):
        return self.maxid() + 1

    def select(self, _id):
        for key, value in enumerate(self.database):
            if str(value['id']) == _id:
                return value

    def update(self, _id, item):
        for key, value in enumerate(self.database):
            if str(value['id']) == _id:
                self.database[key] = item
                break

    def delete(self, _id):
        for key, value in enumerate(self.database):
            if str(value['id']) == _id:
                self.database.pop(key)
                break

    def put(self, storage):
        self.database.append(storage)

    def out(self):
        return self.database

    def get_entries_10(self):
        return self.database[:10]

    def timezone(self):
        kst = KST()
        now = datetime.now(kst)
        return now
