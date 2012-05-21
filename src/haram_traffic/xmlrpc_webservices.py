from SimpleXMLRPCServer import SimpleXMLRPCDispatcher

from models import TrafficStatus

dispatcher = SimpleXMLRPCDispatcher(encoding=u'UTF-8', allow_none=True)

class Services(object):
    
    def report_haram_state(self, lat, lon, state):
        TrafficStatus.objects.create(lat=lat, lon=lon, value=state)
        return 'status saved'
    
    def get_state(self, lat, lon, delta=0.001):
        from collections import Counter
        from datetime import datetime, timedelta
        now = datetime.now()
        # specifying defined area
        states = TrafficStatus.objects.filter(lon__gt=(lon - delta))
        states = states.filter(lat__gt=(lat - delta))
        states = states.filter(lon__lt=(lon + delta))
        states = states.filter(lat__lt=(lat + delta))
        # specifying within timedelta of one hour 
        states = states.filter(time__lt=now).filter(time__gt=(now-timedelta(hours=1)))
        values = [state.value for state in states]
        occurrences = Counter(values)
        highly_probable = occurrences.most_common(1)
        if highly_probable: return highly_probable[0][0]
        return 'no state defined'
    
dispatcher.register_instance(Services())



