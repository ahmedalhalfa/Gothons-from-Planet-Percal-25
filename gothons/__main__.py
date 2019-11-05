import sys
import engine, map, scenes

if __name__ == "__main__.py" :
    a_map = Map('CenteralCorridor')
    a_game = Engine(a_map)
    a_game.play()
