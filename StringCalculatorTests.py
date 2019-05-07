import unittest
import StringCalculator

class testStringCalculator(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(StringCalculator.Add(''), 0, 'Should return 0')

    def testAdd(self):
        self.assertEqual(StringCalculator.Add('1,4,6'), 11, 'Should return 11')

    def testNewLine(self):
        self.assertEqual(StringCalculator.Add('1\n,4,10'), 15, 'Should return 15')
        self.assertEqual(StringCalculator.Add('1,\n4,10'), 15, 'Should return 15')

    def testDelimiter(self):
        self.assertEqual(StringCalculator.Add('//;\n7;8;9'), 24, 'Should return 24')
        self.assertNotEqual(StringCalculator.Add('//&\n4&5&6'), 0, 'Should not return 0')

    def testNegatives(self):
        with self.assertRaises(Exception):
            StringCalculator.Add('4,-6,8')
        with self.assertRaises(Exception):
            StringCalculator.Add('//*\n1*2*-3')

    def testAbove1000(self):
        self.assertEqual(StringCalculator.Add('3,5000,6'), 9, "Should return 12")
        self.assertNotEqual(StringCalculator.Add('4,1001'), 1005, "Should not return 1005")

    def testDelimiterLength(self):
        self.assertEqual(StringCalculator.Add('//xxx\n7xxx8xxx9'), 24, 'Should return 24')
        self.assertNotEqual(StringCalculator.Add('//abc\n4abc5abc6'), 0, 'Should not return 0')

    def testMultipleDelimiters(self):
        self.assertEqual(StringCalculator.Add('//@,;,v\n7@8;9v4'), 28, 'Should return 28')
        self.assertNotEqual(StringCalculator.Add('//?,@,#\n4?5@6#7'), 0, 'Should not return 0')

    def testMultipleDelimiterLengths(self):
        self.assertEqual(StringCalculator.Add('//xxx,abc\n5xxx6abc7'), 18, 'Should return 18')
        self.assertNotEqual(StringCalculator.Add('//***,axy\n5***6axy7'), 0, 'Should not return 0')


if __name__ == '__main__':
    unittest.main()
