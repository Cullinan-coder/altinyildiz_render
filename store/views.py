from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Altınyıldız Clone yayında usta! 🚀")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),  # store uygulamasındaki url'leri dahil eder
]
