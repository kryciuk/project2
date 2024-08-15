from django import template

register = template.Library()


@register.filter(name="has_group")
def has_group(user, group_name):
    user_groups = user.groups.values_list("name", flat=True)
    return True if group_name in user_groups else False
