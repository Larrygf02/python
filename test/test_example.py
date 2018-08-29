import unittest

class TestStringMethods(unittest.TestCase):

	#Saltarse un metodo de prueba
	@unittest.skip("demonstrating skipping")
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s = 'Hola mundo'
		self.assertEqual(s.split(), ['Hola','mundo'])
		with self.assertRaises(TypeError):
			s.split(2)

if __name__ == '__main__':
	unittest.main()