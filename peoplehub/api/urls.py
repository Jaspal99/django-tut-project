from django.urls import path
from . import views

urlpatterns = [
    path('singleobj/<int:id>/',views.SingleObjAPIView.as_view()),
    path('multipleobj/',views.MultiObjAPIView.as_view())
]