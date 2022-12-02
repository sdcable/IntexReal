from django.urls import path, include
from .views import index
from .views import suggestions
from .views import personal
from .views import clientindex
from .views import addDiaryPageView
from .views import addEntryPageView 
from .views import addEntryDestination
from .views import addClientPageView
from .views import updateClientPageView
from .views import showDiariesPageView
from .views import showEntryPageView
from .views import addDailyDiary
from .views import editEntryPageView
from .views import updateEntryPageView
from .views import addFoodTest
from .views import serumViz
from .views import nutViz
from .views import deleteEntry
from .views import viewFood
from .views import addFoods

urlpatterns = [
    path("suggestions/", suggestions, name="suggestions"),
    path("personal/", personal, name="personal"),
    path("clientindex/", clientindex, name="clientindex"),
    path("addDiary/", addDiaryPageView, name="addDiary"),
    path("addDailyDiary/", addDailyDiary, name="addDailyDiary"),
    path("addEntryDestination/", addEntryDestination, name="addEntryDestination"),
    path("addClient/", addClientPageView, name='addClient'),
    path("updateClient/<str:clientusername>/", updateClientPageView, name='updateClient'),
    path("showDiaries/<str:username>", showDiariesPageView, name="showDiaries"),
    path("showEntry/<int:diary_id>/", showEntryPageView, name="showEntry"),
    path("editEntry/<int:journal_id>/", editEntryPageView, name="editEntry"),
    path("updateEntry/", updateEntryPageView, name='updateEntry'),
    path("addEntry/<int:diary_id>", addEntryPageView, name='addEntry'),
    path("addFoodTest/", addFoodTest, name='addFoodTest'),
    path("serumVisualization/<str:username>/", serumViz, name='serumViz'),
    path("nutrientVisualization/<int:diary_id>/<str:username>/", nutViz, name="nutViz"),
    path("deleteEntry/<int:journal_id>", deleteEntry, name='deleteEntry'),
    path("addFoods/", addFoods, name='addFoods'),
    path("viewFood/", viewFood, name='viewFood'),

    path("", index, name="index"),
]
