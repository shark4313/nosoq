def queryset_to_list_of_dicts(queryset):
    if queryset:
        from django.forms.models import model_to_dict
        list = []
        for item in queryset:
            item = model_to_dict(item)
            list.append(item)
        return list
    return None
