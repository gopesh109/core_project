from django.http import JsonResponse
from shared_utils.health import get_health

def health_check(request):
    health_data = get_health()
    return JsonResponse(health_data)
