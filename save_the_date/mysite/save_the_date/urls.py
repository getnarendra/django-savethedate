from django.urls import path
from django.views import i18n
from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
# ]

urlpatterns = [
    # ex: /polls/
    # path("", views.index, name="index"),
    # ex: /polls/5/
    path('jsi18n/', i18n.JavaScriptCatalog.as_view(), name='jsi18n'),    
    path("date/", views.save_the_date, name="save_the_date"),
    path("date/create/", views.date_create, name="date_create"),
    path("date/delete/<int:pk>/", views.date_delete, name="date_delete"),    
    path("date/update/<int:pk>/", views.date_update, name="date_update"),    
    
    path('', views.default_view, name='default'),
    path("<int:question_id>/", views.detail, name="detail"),
    # path("questions/", views.questions_list, name="questions"),    
    path('questions/', views.questions_list, name='questions_list'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/update/<int:pk>/', views.question_update, name='question_update'),
    path('question/delete/<int:pk>/', views.question_delete, name='question_delete'),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]