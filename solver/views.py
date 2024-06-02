from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import SudokuForm
from .models import SudokuPuzzle
from .solver import solve_sudoku, parse_puzzle


def save_puzzle(request):
    puzzle_text = """
    # Puzzle text here
    """

    solution_text = """
    # Solution text here
    """

    puzzle = SudokuPuzzle(puzzle=puzzle_text.strip(), solution=solution_text.strip())
    puzzle.save()



def display_puzzles(request):
    puzzles = SudokuPuzzle.objects.all()
    return render(request, 'solver/puzzles.html', {'puzzles': puzzles})



def sudoku_solver(request):
    if request.method == 'POST':
        form = SudokuForm(request.POST)
        if form.is_valid():
            puzzle_instance = form.save(commit=False)
            puzzle_board = parse_puzzle(puzzle_instance.puzzle)
            if solve_sudoku(puzzle_board):
                puzzle_instance.solution = '\n'.join([' '.join(map(str, row)) for row in puzzle_board])
                puzzle_instance.solved_at = timezone.now()
            else:
                puzzle_instance.solution = "No solution exists"
                puzzle_instance.solved_at = timezone.now()
            puzzle_instance.save()
            return redirect('sudoku_solution', pk=puzzle_instance.pk)
    else:
        form = SudokuForm()
    return render(request, 'solver/solver.html', {'form': form})

def sudoku_solution(request, pk):
    puzzle_instance = get_object_or_404(SudokuPuzzle, pk=pk)
    return render(request, 'solver/solution.html', {'puzzle': puzzle_instance})
