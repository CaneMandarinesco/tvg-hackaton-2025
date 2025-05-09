import os

class Solution:

    inputFolder = os.path.join("soluzioni", "input", "1")
    outputFolder = os.path.join("soluzioni", "output", "1")
    exe = 0

    @staticmethod
    def solve(key: str, text: str) -> str:
        """
        Scrivi la tua soluzione qui
        """
        output = ""
        i = 0
        len_key = len(key)

        for c in text:
            if i == len_key:
                i = 0
            
            val_key = ord(key[i])
            val_text = ord(c)
            if 97 <= val_text <= 122:
                val_out = val_text + (val_key - 96)
                if val_out > 122:
                    val_out -= 26
                output += chr(val_out)
                i += 1
            else:
                output += c
        return output

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
            key = ""
            for i, line in enumerate(file):
                if i == 0:
                    key = line.strip()
                else:
                    string += line

        return key, string

    @staticmethod
    def loadOutput(i: int) -> str:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            string = ""
            for line in file:
                string += line
        return string
