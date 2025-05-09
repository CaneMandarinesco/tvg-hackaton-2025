import os


class Solution:

    inputFolder = os.path.join("soluzioni", "input", "2")
    outputFolder = os.path.join("soluzioni", "output", "2")

    @staticmethod
    def solve(stringa: str) -> int:
        con = ""
        mul = 1
        ris = 0
        strlen = len(stringa)
        for x in range(strlen-5):
            if stringa[x] == 'c' and stringa[x+1] == 'o' and stringa[x+2] == 'n' and stringa[x+3] == '(' and stringa[x+4] != ")":
                i = x+4
                while stringa[i] != ')':
                    con += stringa[i]
                    i+=1
                ris += int(con)
                con = ""
                x = i
            elif stringa[x] == 's' and stringa[x+1] == 'u' and stringa[x+2] == 'm' and stringa[x+3] == '(' and stringa[x+4] != ")":
                i = x+4
                while stringa[i] != ')':
                    ris += int(stringa[i])
                    i+=1
                x = i
            elif stringa[x] == 'm' and stringa[x+1] == 'u' and stringa[x+2] == 'l' and stringa[x+3] == '(' and stringa[x+4] != ")":
                i = x+4
                while stringa[i] != ')':
                    mul *= int(stringa[i])
                    i+=1
                ris += mul
                mul = 1
                x = i
        return ris


    @staticmethod
    def loadInput(i: int) -> str:
        """
        Carica il file di input i-esimo, contenuto all'interno della cartella dei file input.
        Questo metodo deve restituire il valore da passare al metodo solve.
        """
        files = os.listdir(Solution.inputFolder)
        files.sort()

        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            string = ""
            for line in file:
                string += str(line.strip())
        return string

    @staticmethod
    def loadOutput(i: int) -> int:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            value = ""
            for line in file:
                value += line
        return int(value)
