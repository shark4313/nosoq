
def queryset_to_list_of_dicts(queryset):
    if queryset:
        from django.forms.models import model_to_dict
        list = []
        for item in queryset:
            item = model_to_dict(item)
            list.append(item)
        return list
    return None

def get_id_from_session(token):
    from django.contrib.sessions.backends.db import Session
    try:
        s = Session.objects.get(session_key=token)
        id = s.get_decoded()['user_id']
        return id
    except Session.DoesNotExist:
        return False

