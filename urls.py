from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns =[
    path('debate_list/', views.debate_list, name='debate_list'),
    path('<int:debate_id>/', views.debate_detail, name='debate_detail'),
    path('comment/<int:pk>', views.add_comment, name='add_comment'),
    path('agree/<int:blog_id>', views.agree, name="agree"),
]