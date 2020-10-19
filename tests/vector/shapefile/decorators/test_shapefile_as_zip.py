#!-*-coding:utf-8-*-

import os
from vectorio.compress import Zip
from vectorio.vector import Shapefile, ShapefileCompressed, Geojson


class TestShapefileAsZip:

    def setup_method(self):
        self.gjs = '{"type": "FeatureCollection","features": [{"type": "Feature","properties": {},"geometry": {"type": "Polygon","coordinates": [[[-47.63671875,-11.436955216143177],[-49.5703125,-12.983147716796566],[-45.74707031249999,-12.554563528593656],[-47.63671875,-11.436955216143177]]]}}]}'
        self.out_path = '/tmp/test2.zip'
        self.out_shp = '/tmp/test2.shp'

    def test_write(self):
        gj = Geojson()
        shape = ShapefileCompressed(Shapefile(), compress_engine=Zip())
        self.out_path = shape.write(gj.datasource(self.gjs), self.out_path)
        assert self.out_path.endswith('.zip')
        assert bool(shape.collection(shape.datasource(self.out_path)))
        assert os.path.exists(self.out_shp) is False
        assert os.path.exists(self.out_shp.replace('.shp', '.dbf')) is False
        assert os.path.exists(self.out_shp.replace('.shp', '.shx')) is False
        assert os.path.exists(self.out_shp.replace('.shp', '.prj')) is False

    def teardown_method(self):
        if os.path.exists(self.out_path):
            os.remove(self.out_path)
