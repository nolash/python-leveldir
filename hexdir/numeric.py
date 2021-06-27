# standard imports
import math
import os

# local imports
from .base import LevelDir


class NumDir(LevelDir):

    def __init__(self, root_path, thresholds=[1000]):
        super(NumDir, self).__init__(root_path, len(thresholds), 8)
        fi = os.stat(self.master_file)
        self.thresholds = thresholds
        self.entry_length = 8


    def to_dirpath(self, n): 
        c = n 
        x = 0
        d = []
        for t in self.thresholds:
            x = math.floor(c / t)
            y = x * t
            d.append(str(y))
            c -= y
        return os.path.join(self.path, *d) 
      

    def to_filepath(self, n):
        path = self.to_dirpath(n)
        return os.path.join(path, str(n))


    def add(self, n, content, prefix=b''):
        path = to_filepath(n)
        f = open(path, 'wb')
        f.write(content)

        f = open(self.master_file, 'ab')
        f.write(n.to_bytes(8, byteorder('big')))
        f.close()
