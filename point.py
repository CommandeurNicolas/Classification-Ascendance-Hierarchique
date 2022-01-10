class Point:
    def __init__(self,label,x,y):
        self.label = label
        self.x = x
        self.y = y
    def __repr__(self):
        return f'{self.label} -> x:{self.x} y:{self.y}'
    def __str__(self) -> str:
        return f'{self.label} -> x:{self.x} y:{self.y}'