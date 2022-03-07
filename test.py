import unittest
import pathlib as pl
import os
import shutil


class TestFilter(unittest.TestCase):
    def test_creo_archivos(self):
        shutil.rmtree('regiones', ignore_errors=True)

        os.system("python3 filter_region.py pcm_donaciones.csv")
        path = pl.Path("regiones/lima.csv")
        self.assertTrue(path.is_file())
        self.assertTrue(path.parent.is_dir())

    

if __name__ == '__main__':
    unittest.main()
