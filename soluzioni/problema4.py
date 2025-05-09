import os
import pdb


class Solution:

    inputFolder = os.path.join("soluzioni", "input", "4")
    outputFolder = os.path.join("soluzioni", "output", "4")

    @staticmethod
    def solve(matrix: list[list[int]], squares: list[list[int, int, int, int]]) -> list[int]:
        Y = len(matrix)
        X = len(matrix[0])
        M = []
        for x in matrix:
            M.append(x[:])

        for y in range(Y):
            s = 0 
            for x in range(X):
                s += matrix[y][x] 
                M[y][x] = s

        output = []
        for s in squares:
            y1, x1 = s[0], s[1]
            y2, x2 = s[2], s[3]
            somma = 0
            for y in range(y1, y2+1):
                # if y >= Y: break
                x = 0
                if x1-1 == -1:
                    x = M[y][x2]
                else:
                    x = M[y][x2] - M[y][x1-1]
                somma += x
            output.append(somma)

        return output


    @staticmethod
    def loadInput(i: int) -> tuple[list[list[int]], list[list[int, int, int, int]]]:
        """
        Carica il file di input i-esimo, contenuto all'interno della cartella dei file input.
        Questo metodo deve restituire il valore da passare al metodo solve.
        """
        files = os.listdir(Solution.inputFolder)
        files.sort()

        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            matrix = []
            squares = []
            for i, line in enumerate(file):
                if i == 0:
                    j = int(line.strip())
                elif i <= j:
                    matrix.append(list(map(int, line.strip().split(","))))
                elif i > j:
                    squares.append(list(map(int, line.strip().split(","))))
        return matrix, squares

    @staticmethod
    def loadOutput(i: int) -> list[int]:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            for line in file:
                list = line.strip().split(",")
                for i in range(len(list)):
                    list[i] = int(list[i])
        return list

sol = Solution()
x = sol.loadInput(0)
r = sol.loadOutput(0)
print(sol.solve(*x))
