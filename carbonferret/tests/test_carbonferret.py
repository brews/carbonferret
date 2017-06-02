import unittest
import carbonferret as cf
from os import path


class DummyResponse:

    def __init__(self, payload):
        self.text = payload


class DummySession:

    def __init__(self, testhtml):
        self.response = DummyResponse(testhtml)

    def get(self, url_endpoint, params):
        return self.response


class TestCarbonferret(unittest.TestCase):

    def setUp(self):
        # testresponse.html was taken from calib.org/marine on 2017-05-02
        here = path.abspath(path.dirname(__file__))
        testhtml_path = path.join(here, 'testresponse.html')
        with open(testhtml_path) as fl:
            testhtml_string = fl.read()
        self.testhtml_string = testhtml_string
        self.dummysession = DummySession(testhtml_string)

    # @unittest.skip('Test not written')
    def test_find_near(self):
        victim = cf.find_near(lat=0, lon=0, n=2, session=self.dummysession)
        # Just testing a couple key values, not everything.
        goals = {'MapNo': [1221, 1222],
                'Lon': [-5.7416, -5.7416],
                'Lat': [-15.9409, -15.9409],
                'DeltaR': [361, 294]}
        for k, v in goals.items():
            self.assertTrue(all(victim[k].values == v))


if __name__ == '__main__':
    unittest.main()
