from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path ('',views.home,name='home'),
    path('product/',views.all_product,name='product'),
    path('question/<slug:slug>', views.question_detail , name = 'question_detail'),
    path('question/new/', views.question_create,name = 'question_create'),
    path('question/<slug:slug>/edit/',views.question_update,name = 'question_update'),
    path('question/<slug:slug>/delete/',views.question_delete,name = 'question_delete'),
]