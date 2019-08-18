import unittest
import json
from handler import list_posts, get_post


class TestHandler(unittest.TestCase):
    """ Tests handler methods """

    def test_list_posts(self):
        """ Tests list_posts """
        res = list_posts(None, None)
        self.assertEquals(200, res['statusCode'])
        self.assertTrue(len(res['body']) > 0)

if __name__ == '__main__':
    unittest.main()
