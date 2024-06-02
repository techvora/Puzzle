from django.urls import path
from .views import *

urlpatterns = [
    path('solve/', sudoku_solver, name='sudoku_solver'),
    path('puzzles/', display_puzzles, name='display_puzzles'),
    path('solution/<int:pk>/', sudoku_solution, name='sudoku_solution'),
]