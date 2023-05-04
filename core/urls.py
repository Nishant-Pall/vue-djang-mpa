from django.urls import path
from core.views import HomeView, MathGameView, AnagramGameView, record_score

app_name = "core"
urlpatterns = [
    path("", HomeView.as_view(), name="homepage"),
    path("math-game/", MathGameView.as_view(), name="math-game"),
    path("anagram-game/", AnagramGameView.as_view(), name="anagram-game"),
    path("record-score/", record_score, name="record-score"),
]
