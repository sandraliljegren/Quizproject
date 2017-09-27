from django.urls import path
from quiz import views

urlpatterns = [
		path("", views.start),
		path("quiz/<int:quiz_number>/", views.quiz),
		path("quiz/<int:quiz_number>/question/<int:question_number>/", views.question),
		path("quiz/<int:quiz_number>/results/", views.completed),	
		]