import sys
import engine, map, scenes

if __name__ == "__main__" :

    a_map = map.Map('central_corridor')
    a_game = engine.Engine(a_map)
    a_game.play()
