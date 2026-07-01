import psutil
import unittest

class TestHealthCheck(unittest.TestCase):
    def test_cpu_percent(self):
        self.assertIsInstance(psutil.cpu_percent(), float)

    def test_memory_percent(self):
        self.assertIsInstance(psutil.virtual_memory().percent, float)

    def test_disk_percent(self):
        self.assertIsInstance(psutil.disk_usage('/').percent, float)

if __name__ == '__main__':
    unittest.main()
