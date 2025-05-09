import os

e = {
        "SKULL": "💀",
        "CANDY": "🍬",
        "MUSHROOM": "🍄",
        "MIRROR": "🪞",
        "LEFT": "🠔",
        "UP": "🠕 ",
        "RIGHT": "🠖",
        "DOWN": "🠗 ",
        "END": "🏁",
        "START": "🐹"
}


s = 0
t = 0
G = {}
costo = float('inf')

def appendNode(xm, ym, xm2, ym2, x, y, G, c):
    if xm2 >= 0 and xm2 <= x:
        if ym2 >= 0 and ym2 <= y:
            G[(ym, xm)].append((ym2, xm2, c))

def dfs(v, c, visited):
    global costo
    global s, t, G
    visited.add(v)

    if v == t:
        if c <= costo:
            print("trovato diocaro")
            costo = c
            return

    # TODO: check skull

    if v == s:
        return

    for u in v:
        if u not in visited:
            dfs((u[0], u[1]), visited, u[2]+c)

class Solution:
    inputFolder = os.path.join("soluzioni", "input", "6")
    outputFolder = os.path.join("soluzioni", "output", "6")

    
    @staticmethod
    def solve(y: int, x: int, grid: list[list[int]]) -> int:
        """
        Scrivi la tua soluzione qui
        """
        global s, t, G

        # costruisci grafo senza collegarlo
        for ym in range(y):
            for xm in range(x):
                c = grid[ym][xm]
                G[(ym, xm)] = []
                # imposto i riferimenti
                if c == e["START"]:
                    s = G[(ym, xm)]
                elif c == e["END"]:
                    t = G[(ym, xm)]

        # collega il grafo
        for ym in range(y):
            for xm in range(x):
                c = grid[ym][xm]
                if c == e["MUSHROOM"]:
                    appendNode(xm, ym, xm-2, ym, x, y, G, 0)
                    appendNode(xm, ym, xm, ym-2, x, y, G, 0)
                    appendNode(xm, ym, xm+2, ym, x, y, G, 0)
                    appendNode(xm, ym, xm, ym+2, x, y, G, 0)

                elif c == e["SKULL"]:
                    # quando visito vedo se sono in uno skull!!!!!
                    pass
                elif c == e["CANDY"]:
                    appendNode(xm, ym, xm-1, ym, x, y, G, 0)
                    appendNode(xm, ym, xm, ym-1, x, y, G, 0)
                    appendNode(xm, ym, xm+1, ym, x, y, G, 0)
                    appendNode(xm, ym, xm, ym+1, x, y, G, 0)
                    appendNode(xm, ym, xm-1, ym-1, x, y, G, 0)
                    appendNode(xm, ym, xm+1, ym+1, x, y, G, 0)
                    appendNode(xm, ym, xm+1, ym-1, x, y, G, 0)
                    appendNode(xm, ym, xm-1, ym+1, x, y, G, 0)
                elif c == e["MIRROR"]:
                    appendNode(xm, ym, ym, xm, x, y, G, 0)
                elif c == e["RIGHT"]:
                    appendNode(xm, ym, x, ym, x, y, G, 0)
                    pass
                elif c == e["LEFT"]:
                    appendNode(xm, ym, 0, ym, x, y, G, 0)
                elif c == e["DOWN"]:
                    appendNode(xm, ym, xm, y, x, y, G, 0)
                elif c == e["UP"]:
                    appendNode(xm, ym, xm, 0, x, y, G, 0)
                elif c == "--" or c == e["START"]:
                    appendNode(xm, ym, xm-1, ym, x, y, G, 1)
                    appendNode(xm, ym, xm, ym-1, x, y, G, 1)
                    appendNode(xm, ym, xm+1, ym, x, y, G, 1)
                    appendNode(xm, ym, xm, ym+1, x, y, G, 1)
        
        # VISITA!!!!
        visited = set()
        dfs(s, 0, visited) 
        return costo


    @staticmethod
    def loadInput(i: int) -> str:
        """
        Carica il file di input i-esimo, contenuto all'interno della cartella dei file input.
        Questo metodo deve restituire il valore da passare al metodo solve.
        """
        files = os.listdir(Solution.inputFolder)
        files.sort()

        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            grid = []
            for i, line in enumerate(file):
                if i == 0:
                    startY, startX = line.strip().split(" ")
                else:
                    grid.append(line.strip().split(", "))

        return int(startY), int(startX), grid

    @staticmethod
    def loadOutput(i: int) -> str:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            for line in file:
                return int(line.strip())
