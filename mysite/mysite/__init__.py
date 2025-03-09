class StringReverser:
    def reverse_string(self, string):
        return string[::-1]



class StringReverserTestCase(TestCase):
    def test_reverse_string(self):
        reverser = StringReverser()
        self.assertEqual(reverser.reverse_string('hello'), 'olleh')


class StringReverserTest(TestCase):
    def test_reverse_string(self):
        reverser = StringReverser()
        self.assertEqual(reverser.reverse_string('hello'), 'olleh')


