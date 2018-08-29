import unittest

def func(x):
	return x**2

class Mytest(unittest.TestCase):
	def test(self):
		self.assertEqual(func(4), 16)

if __name__ == '__main__':
	unittest.main()