import app
import unittest

class TestBand (unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(app.subtract(156156,156),156000)
        self.assertLess(app.subtract(5465454656565,6541541544),5458999999999)
        self.assertNotEqual(app.subtract(454164565484,9959),4541)
        self.assertEqual(app.subtract(10000000,1),9999999)
        with self.assertRaises(TypeError):
            app.subtract("Hello, world!",2)

    def test_add(self):
        self.assertEqual(app.add(889498484,65564894),955063378)
        self.assertGreater(app.add(5465969696565,6541211544),54589131150)
        self.assertTrue(app.add(35673567,995959595)==1031633162)
        self.assertFalse(app.add(10000000,1)==99999)
        with self.assertRaises(TypeError):
            app.add("Hello, world!",12312312321)
    
    def test_multiply(self):
        self.assertEqual(app.multiply(404505,25),10112625)
        self.assertGreaterEqual(app.multiply(8080,22),122568)
        self.assertLessEqual(app.multiply(9000,173),1789526)
        self.assertEqual(app.multiply(32197,1905),61335285)
        with self.assertRaises(TypeError):
            app.multiply("Hello, world!",98787898.67)
    
    def test_divide(self):
        self.assertEqual(int(app.divide(15454530,515151)),30)
        self.assertNotEqual(int(app.divide(5465454656565,25)),136636366400000)
        self.assertEqual(int(app.divide(5334820,56156)),95)
        self.assertNotEqual(int(app.divide(1606214421,8498489)),355)
        with self.assertRaises(TypeError):
            app.divide("Hello, world!",745795649.98)

if __name__ == '__main__':
    unittest.main()