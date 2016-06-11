import os
import unittest
import pychemia
from pychemia.test import has_local_mongo
import logging

class SearcherTest(unittest.TestCase):

    def test_harmony(self):
        """
        Tests (pychemia.searcher.harmony) with NonCollinearMagMoms   :
        """
        logging.basicConfig(level=logging.DEBUG)
        if not pychemia.HAS_PYMONGO:
            print('Could not load pymongo, leaving now')
            return
        else:
            if not has_local_mongo():
                return

        pychemia.pcm_log.debug('HarmonySearch')

        source = 'pychemia/test/data/vasp_02'
        assert os.path.isfile(source + os.sep + 'INCAR')
        assert os.path.isfile(source + os.sep + 'POSCAR')
        popu = pychemia.population.NonCollinearMagMoms('test', source, debug=True)
        searcher = pychemia.searcher.HarmonySearch(popu, generation_size=16, stabilization_limit=5)
        searcher.run()
        popu.pcdb.clean()


    def test_firefly(self):
        """
        Tests (pychemia.searcher.firefly) with NonCollinearMagMoms   :
        """
        logging.basicConfig(level=logging.DEBUG)
        if not pychemia.HAS_PYMONGO:
            print('Could not load pymongo, leaving now')
            return
        else:
            if not has_local_mongo():
                return

        pychemia.pcm_log.debug('HarmonySearch')

        source = 'pychemia/test/data/vasp_02'
        assert os.path.isfile(source + os.sep + 'INCAR')
        assert os.path.isfile(source + os.sep + 'POSCAR')
        popu = pychemia.population.NonCollinearMagMoms('test', source, debug=True)
        searcher = pychemia.searcher.FireFly(popu, generation_size=16, stabilization_limit=5)
        searcher.run()
        popu.pcdb.clean()


    def test_genetic(self):
        """
        Tests (pychemia.searcher.genetic) with NonCollinearMagMoms   :
        """
        logging.basicConfig(level=logging.DEBUG)
        if not pychemia.HAS_PYMONGO:
            print('Could not load pymongo, leaving now')
            return
        else:
            if not has_local_mongo():
                return

        pychemia.pcm_log.debug('HarmonySearch')

        source = 'pychemia/test/data/vasp_02'
        assert os.path.isfile(source + os.sep + 'INCAR')
        assert os.path.isfile(source + os.sep + 'POSCAR')
        popu = pychemia.population.NonCollinearMagMoms('test', source, debug=True)
        searcher = pychemia.searcher.GeneticAlgorithm(popu, generation_size=16, stabilization_limit=5)
        searcher.run()
        popu.pcdb.clean()
