from django.urls import path, include
from . import views
app_name='sale'
urlpatterns=[
    path('',views. allProdCat,name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>', views.ProDetail,name='prodCatdetail'),
    path('search_app',include('search_app.urls')),

]