#!/usr/bin/python3
"""Square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Size of the square"""
        return super().width

    @size.setter
    def size(self, size):
        """Set size of the square"""
        super(Square, type(self)).width.fset(self, size)
        super(Square, type(self)).height.fset(self, size)

    def __str__(self):
        """Return string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Updates the rectangle with the given args"""
        if args and len(args) > 0:
            if len(args) >= 2:
                x = list(args)
                x.insert(2, args[1])
                x = tuple(x)
                args = x
        else:
            if 'size' in kwargs.keys():
                kwargs['width'] = kwargs.pop('size')
                kwargs['height'] = kwargs['width']
        super(Square, self).update(*args, **kwargs)
