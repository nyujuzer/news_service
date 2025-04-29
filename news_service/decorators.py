from .models import API_keys
from django.http import JsonResponse

def usesAPIKey(view_func):
    def wrapper(request, *args, **kwargs):
        # Check if the API key is present in the request
        api_key = request.GET.get('api_key')
        all_keys = API_keys.objects.all().filter(key=api_key, is_active=True)
        if all_keys:
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({"apiKey":"invalid"})
    return wrapper