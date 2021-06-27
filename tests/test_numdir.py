# standard imports
import unittest
import tempfile
import shutil
import logging
import os

# local imports
from leveldir.numeric import NumDir


logging.basicConfig(level=logging.DEBUG)
logg = logging.getLogger()



class NumDirTest(unittest.TestCase):

    def setUp(self):
        self.dir = tempfile.mkdtemp() 


    def tearDown(self):
        shutil.rmtree(self.dir)
        logg.debug('cleaned numdir root {}'.format(self.dir))


    def test_path(self):
        self.numdir = NumDir(os.path.join(self.dir, 'n'), [1000, 100])
        logg.debug('setup numdir root {}'.format(self.dir))
        path = self.numdir.to_filepath(1337)
        path_parts = []
        logg.debug(path)
        (path, three) = os.path.split(path)
        (path, two) = os.path.split(path)
        (path, one) = os.path.split(path)
        self.assertEqual(three, '1337')
        self.assertEqual(two, '300')
        self.assertEqual(one, '1000')


    def test_invalid_thresholds(self):
        with self.assertRaises(ValueError):
            self.numdir = NumDir(os.path.join(self.dir, 'n'), [100, 1000])

        with self.assertRaises(ValueError):
            self.numdir = NumDir(os.path.join(self.dir, 'n'), [])



if __name__ == '__main__':
    unittest.main()
