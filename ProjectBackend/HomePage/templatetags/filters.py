from django import template
from django.contrib.auth.hashers import check_password
from UserAuth.models import UserData

register = template.Library()


@register.filter
def is_auth(user, request):
    user_name = request.session.get("username")
    if user_name:
        try:
            db = UserData.objects.get(username=user_name)
            if user and db:
                return True
        except UserData.DoesNotExist:
            return False
    return False
