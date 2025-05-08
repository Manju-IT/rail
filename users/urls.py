from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'


urlpatterns = [
    path('', views.UserHomePage, name='user-base'),
    path('Machine-learning', views.MachineLearningPage, name='machine-learning'),
    path('predict', views.PredictPage, name='predict'),
    path('dataset-view', views.DatasetView, name='dataset-view'),

     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)