from zoo.models import *

class TestDBRace1(object):
    def setup(self):
         assert Zoo.objects.count() == 0

    def test1(self):
          obj = Zoo.objects.create(name='hyppo')
          assert Zoo.objects.count() == 1
          assert Zoo.objects.all()[0].name == 'hyppo'

class TestDBRace2(object):
    def setup(self):
        assert Zoo.objects.count() == 0

    def test1(self):
        obj = Zoo.objects.create(name='rhino')
        assert Zoo.objects.count() == 1
        assert Zoo.objects.all()[0].name == 'rhino'
       
