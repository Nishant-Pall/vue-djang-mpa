import json
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from core.models import GameScore


def record_score(request):
    data = json.loads(request.body)

    user_name = data["user-name"]
    game = data["game"]
    score = data["score"]

    new_score = GameScore(user_name=user_name, game=game, score=score)

    return JsonResponse({"success": True})


class HomeView(TemplateView):
    template_name = "home.html"


class MathGameView(TemplateView):
    template_name = "math-game.html"


class AnagramGameView(TemplateView):
    template_name = "anagram-game.html"
