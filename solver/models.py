from django.db import models

class SudokuPuzzle(models.Model):
    puzzle = models.TextField()
    solution = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    solved_at = models.DateTimeField(blank=True, null=True)

    # def __str__(self):
    #     return self.puzzle