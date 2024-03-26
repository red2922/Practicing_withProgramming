class advance_camera:
    def __init__(self, coordinate, direction):
        self.place = coordinate
        self.dir = direction

    def get_coords(self):
        return self.place

    def get_dir(self):
        return self.dir

    def set_coords(self,new):
        self.place = new

    def set_dir(self,new):
        self.dir = new