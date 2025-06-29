import unittest
from intern_manager import InternManager

class TestInternManager(unittest.TestCase):
    def setUp(self):
        self.manager = InternManager()

    def test_add_intern(self):
        self.assertTrue(self.manager.add_intern("Alice"))
        self.assertFalse(self.manager.add_intern("Alice"))  # Duplicate

    def test_remove_intern(self):
        self.manager.add_intern("Bob")
        self.assertTrue(self.manager.remove_intern("Bob"))
        self.assertFalse(self.manager.remove_intern("Bob"))  # Already removed

    def test_get_intern(self):
        self.manager.add_intern("Carol")
        self.manager.add_intern("Dave")
        intern_list = self.manager.get_intern_list()
        self.assertIn("Carol", intern_list)
        self.assertIn("Dave", intern_list)

    def test_clear_intern(self):
        self.manager.add_intern("Eve")
        self.assertTrue(self.manager.clear_interns())
        self.assertEqual(self.manager.get_intern_list(), [])

    def test_find_intern(self):
        self.manager.add_intern("Frank")
        self.assertTrue(self.manager.find_intern("Frank"))
        self.assertFalse(self.manager.find_intern("Grace"))

if __name__ == '__main__':
    unittest.main()