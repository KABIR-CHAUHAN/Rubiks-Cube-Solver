import tkinter as tk
from tkinter import messagebox, simpledialog
import kociemba

LETTER_TO_FACELET = {
    'w': 'U',   # Up (white)
    'y': 'D',   # Down (yellow)
    'b': 'F',   # Front (blue)
    'o': 'R',   # Right (orange)
    'g': 'B',   # Back (green)
    'r': 'L'    # Left (red)
}

FACE_NAMES = ['U', 'R', 'F', 'D', 'L', 'B']
FACE_POS = {
    'U': (3, 0),
    'L': (0, 3),
    'F': (3, 3),
    'R': (6, 3),
    'B': (9, 3),
    'D': (3, 6)
}
FACELET_TO_COLOR = {
    'U': 'white', 'R': 'orange', 'F': 'blue', 'D': 'yellow', 'L': 'red', 'B': 'green'
}

class RubiksCubeGUI:
    def __init__(self, master, cube_letters):
        self.master = master
        master.title("Rubik's Cube Solver")
        self.cube_letters = cube_letters
        self.squares = {}
        self.draw_cube()
        solve_btn = tk.Button(master, text="Solve Cube", command=self.solve_cube, bg="lightgreen")
        solve_btn.grid(row=11, column=3, columnspan=4)
        self.solution_label = tk.Label(master, text="", fg="green")
        self.solution_label.grid(row=12, column=0, columnspan=12)

    def draw_cube(self):
        k = 0
        for face in FACE_NAMES:
            off_x, off_y = FACE_POS[face]
            for i in range(3):
                for j in range(3):
                    facelet = self.cube_letters[k]
                    color = FACELET_TO_COLOR[LETTER_TO_FACELET[facelet]]
                    x, y = off_x + j, off_y + i
                    btn = tk.Label(self.master, width=4, height=2, bg=color, relief='solid', bd=1)
                    btn.grid(row=y + 2, column=x)
                    k += 1

    def solve_cube(self):
        facelet_str = ''.join([LETTER_TO_FACELET[ch] for ch in self.cube_letters])
        print("Cube string for kociemba:", facelet_str)
        try:
            solution = kociemba.solve(facelet_str)
            self.solution_label.config(text=f"Solution: {solution}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid cube input!\n{e}")

def ask_for_letters():
    example = (
        "Enter 54 letters for stickers (NO SPACES):\n"
        "w=white (Up), y=yellow (Down), b=blue (Front), o=orange (Right), "
        "g=green (Back), r=red (Left)\n"
        "Order: U (top), R, F, D (bottom), L, B (each as 9 stickers, row by row)\n"
        "Example (solved): wwwwwwwww ooooooooo bbbbbbbbb yyyyyyyyy rrrrrrrrr ggggggggg\n"
        "Paste your cube letters below (total 54):"
    )
    s = simpledialog.askstring("Cube Input", example)
    if not s:
        return None
    letters = [ch for ch in s.lower() if ch in 'wboyrg']
    if len(letters) != 54:
        messagebox.showerror("Error", "You must enter exactly 54 letters!")
        return None
    return letters

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    cube_letters = ask_for_letters()
    if cube_letters:
        root.deiconify()
        app = RubiksCubeGUI(root, cube_letters)
        root.mainloop()
    else:
        print("No valid input provided.")
