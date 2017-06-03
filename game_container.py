import ticktactoe as ttt

WIDTH = 300
HEIGHT = 300
FPS = 30
game = None


def main():
    global game
    game = ttt.TTTGame(WIDTH, HEIGHT)

if __name__ == "__main__":
    main()

while True:
    game.step(FPS)