from django.urls import path
from blog import views
  # ✅ CORRECT: import from the same folder

urlpatterns = [
    path('', views.post_list, name='post_list'),  # ✅ Routes the root URL to your view
]
