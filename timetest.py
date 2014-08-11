from datetime import timedelta, datetime, tzinfo

class KST(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=9)

    def dst(self, dt):
        return timedelta(0)

    def tzname(self,dt):
        return "(UTC+09:00)"
kst = KST()
now1 = datetime.now(kst)
now2 = datetime.now()
print "Content-type: text/plain;\n\n"
print now1
print now2