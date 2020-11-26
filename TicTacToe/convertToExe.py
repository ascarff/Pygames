import cx_Freeze

executables = [cx_Freeze.Executable("tictactoe.py")]

cx_Freeze.setup(
    name="tictactoe",
    options={"build_exe": {"packages":["pygame"], "include_files":["X.png", "O.png", "tictactopening.png"]} },

    executables = executables
)

