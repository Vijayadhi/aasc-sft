from django.urls import path
from .views import generatecummulative

urlpatterns = [
    # path('manage_internals/', manage_internal, name='index'),
    # path('add_score/', add_score, name='add_score'),
    path('generatecummulative/', generatecummulative, ),
    # path('processmarklist/', generatecummulative, name="processmarklist"),

]
