from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
def product_detail(request, product_id):
    return HttpResponse(f"Ürün Detayı: {product_id}")

def category_products(request, category_id):
    return HttpResponse(f"Kategori Ürünleri: {category_id}")

def cart_view(request):
    return HttpResponse("Sepet")

def add_to_cart(request, product_id):
    return HttpResponse(f"{product_id} ürünü sepete eklendi")

def remove_from_cart(request, product_id):
    return HttpResponse(f"{product_id} ürünü sepetten çıkarıldı")

def checkout(request):
    return HttpResponse("Ödeme Sayfası")

def order_history(request):
    return HttpResponse("Sipariş Geçmişi")

def favorite_list(request):
    return HttpResponse("Favoriler")

def add_favorite(request, product_id):
    return HttpResponse(f"{product_id} favorilere eklendi")

def remove_favorite(request, product_id):
    return HttpResponse(f"{product_id} favorilerden çıkarıldı")

def signup_view(request):
    return HttpResponse("Kayıt Ol")
def home(request):
    return HttpResponse
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),  # store uygulamasındaki url'leri dahil eder
]
