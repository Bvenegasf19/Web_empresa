from . import views
from django.urls import path

urlpatterns = [    
    path('<int:page_id>/<slug:page_slug>/', views.page, name='page')
]