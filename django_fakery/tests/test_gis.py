import sys
from unittest import skipIf

from django.test import TestCase
from django.contrib.gis import geos
from django_fakery import factory


PYPY3 = hasattr(sys, 'pypy_version_info') and sys.version_info.major >= 3


@skipIf(PYPY3, "Psycopg2cffi does not support Python3")
class GisTest(TestCase):
    def test_gis_fields(self):
        gigis = factory.make('tests.Pizzeria')
        self.assertTrue(isinstance(gigis.hq, geos.Point))
        self.assertTrue(isinstance(gigis.directions, geos.LineString))
        self.assertTrue(isinstance(gigis.floor_plan, geos.Polygon))
        self.assertTrue(isinstance(gigis.locations, geos.MultiPoint))
        self.assertTrue(isinstance(gigis.routes, geos.MultiLineString))
        self.assertTrue(isinstance(gigis.delivery_areas, geos.MultiPolygon))
        self.assertTrue(isinstance(gigis.all_the_things, geos.GeometryCollection))