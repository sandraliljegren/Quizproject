from django.urls import path
from quiz import views

urlpatterns = [
		path("", views.start, name="start_page"),
		path("quiz/<int:quiz_number>/", views.quiz, name="quiz_page"),
		path("quiz/<int:quiz_number>/question/<int:question_number>/", views.question, name="question_page"),
		path("quiz/<int:quiz_number>/results/", views.results, name="results_page"),	
		]