from django import forms
from .models import SudokuPuzzle

class SudokuForm(forms.ModelForm):
    class Meta:
        model = SudokuPuzzle
        fields = ['puzzle']
        widgets = {
            'puzzle': forms.Textarea(attrs={'rows': 9, 'cols': 18}),
        }
