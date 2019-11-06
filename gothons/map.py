import scenes
class Map(object) :

    scenes = {
    'central_corridor' : scenes.CentralCorridor(),
    'laser_weapon_armory' : scenes.LaserWeaponArmory(),
    'the_bridge' : scenes.TheBridge(),
    'escape_pod' : scenes.EscapePod(),
    'death' : scenes.Death(),
    'finished' : scenes.Finish()

    }

    def __init__(self, start_scene) :
        self.start_scene = start_scene

    def next_scene(self, scene_name) :

        return Map.scenes.get(scene_name)

    def opening_scene(self) :

        return self.next_scene(self.start_scene)
