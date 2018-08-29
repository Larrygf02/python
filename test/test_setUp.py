import unittest

class WidgetTestCase(unittest.TestCase):
	def setUp(self):
		self.widget = Widget('The widget')

	def test_default_widget_size(self):
		self.assertEqual(self.widget.size(),(50,50),'Incorrecto valor por defecto')

if __name__ == '__main__':
	unittest.main()