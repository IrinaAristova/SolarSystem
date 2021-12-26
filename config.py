import configparser
import argparse
import textwrap
from flyobj import *



class Config:
    width = 0
    height = 0
    starts = 0
    display = (0, 0)
    stopOnCollision = True
    star_colors = []
    generators = []

    def __init__(self):
        parser = argparse.ArgumentParser(description='Solar system simulator',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent('''\
                Keys used:
                    q or ESC     = Exit
                    p or SPACE   = Pause
                    f            = Toggle fullscreen (if supported)
            '''))

        parser.add_argument('-f', '--file', 
            dest='file', 
            default='System.ini',
            help='configuration file')

        args = parser.parse_args()

        self.config = configparser.ConfigParser()
        self.config.read(args.file)

        sys = self.config['System']
        self.width = int(sys.get("WIN_WIDTH", 1500))
        self.height = int(sys.get("WIN_HEIGHT", 800))

        self.display = (self.width, self.height)


        self.space_color = sys.get("SPACE_COLOR")

        self.onCollision = sys.get("ON_COLLISION", "join")

        gens = sys.get("GENERATORS")
        if gens != None:
            self.generators = gens.split(',')



    def getSystem(self):
        s = []

        for i in self.config.sections():
            if i != "System" and not(i in set(self.generators)):
                obj = FlyObject(i, 
                    int (self.config[i]["Mass"]), 
                    float (self.config[i]["X"]), 
                    float (self.config[i]["Y"]), 
                    float (self.config[i]["VX"]), 
                    float (self.config[i]["VY"]))
                
                obj.initSurface(int (self.config[i]["R"]), 
                    self.config[i]["color"],
                    self.space_color)
                
                s.append(obj)

        return s

    def getDisplay(self):
        return self.display

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getSpaceColor(self):
        return self.space_color

