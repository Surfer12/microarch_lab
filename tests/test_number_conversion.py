import unittest

# Import the functions from the number_conversion module
# Adjust the import path if necessary based on your project structure
from conversions.python.number_conversion import decimal_to_binary, binary_to_decimal, fraction_to_binary


class TestNumberConversion(unittest.TestCase):
    def test_decimal_to_binary_positive(self):
        # Test positive number conversion with specified bit length
        self.assertEqual(decimal_to_binary(5, 8), '00000101')
        self.assertEqual(decimal_to_binary(0, 8), '00000000')
        self.assertEqual(decimal_to_binary(255, 8), '11111111')
        self.assertEqual(decimal_to_binary(127, 8), '01111111')

    def test_decimal_to_binary_negative(self):
        # Test negative numbers for two's complement conversion in an 8-bit field
        self.assertEqual(decimal_to_binary(-5, 8), '11111011')
        self.assertEqual(decimal_to_binary(-1, 8), '11111111')
        self.assertEqual(decimal_to_binary(-128, 8), '10000000')
        # For a larger bit length, test for correctness
        self.assertEqual(decimal_to_binary(-5, 16)[-8:], '11111011')

    def test_binary_to_decimal_positive(self):
        # Test conversion from binary to decimal for positive numbers
        self.assertEqual(binary_to_decimal('00000101'), 5)
        self.assertEqual(binary_to_decimal('00000000'), 0)
        self.assertEqual(binary_to_decimal('01111111'), 127)

    def test_binary_to_decimal_negative(self):
        # Test conversion from binary to decimal for negative numbers
        self.assertEqual(binary_to_decimal('11111011'), -5)
        self.assertEqual(binary_to_decimal('11111111'), -1)
        self.assertEqual(binary_to_decimal('10000000'), -128)

    def test_round_trip(self):
        # Test round-trip conversion for a list of numbers with a given bit length
        for number in [0, 1, 10, -1, -10, 127, -128, 255, -255]:
            # Use a bit length that can accommodate the magnitude
            bit_length = 16
            binary_str = decimal_to_binary(number, bit_length)
            result = binary_to_decimal(binary_str)
            self.assertEqual(result, number, f"Round-trip failed for {number} using {binary_str}")

    def test_fraction_to_binary(self):
        # Test fraction to binary conversion
        self.assertEqual(fraction_to_binary(0.25, 8), '01')  # 0.25 should give '01'
        self.assertEqual(fraction_to_binary(0.5, 8), '1')     # 0.5 should give '1'
        self.assertEqual(fraction_to_binary(0.75, 8), '11')   # 0.75 should give '11'

    def test_fraction_invalid(self):
        # Test that negative fractions raise an error
        with self.assertRaises(ValueError):
            fraction_to_binary(-0.1, 8)

    def test_binary_string_format(self):
        # Test that the binary string has exactly the specified number of digits and only contains '0' and '1'
        for number in range(0, 256):
            bit_length = 8
            bin_str = decimal_to_binary(number, bit_length)
            self.assertEqual(len(bin_str), bit_length, f"Binary representation of {number} should be {bit_length} digits long")
            self.assertTrue(all(ch in '01' for ch in bin_str), f"Binary representation of {number} contains invalid characters")

        # Also test for negative numbers in 8 bits
        for number in range(-128, 0):
            bit_length = 8
            bin_str = decimal_to_binary(number, bit_length)
            self.assertEqual(len(bin_str), bit_length, f"Binary representation of {number} should be {bit_length} digits long")
            self.assertTrue(all(ch in '01' for ch in bin_str), f"Binary representation of {number} contains invalid characters")

    def test_digit_transition(self):
        # test critical transition points for digit changes
        # For 4-bit representation: 7 should be '0111' and 8 should be '1000'
        self.assertEqual(decimal_to_binary(7, 4), '0111', "7 in 4-bit should be '0111'")
        self.assertEqual(decimal_to_binary(8, 4), '1000', "8 in 4-bit should be '1000'")

        # For 5-bit representation: 15 should be '01111' and 16 should be '10000'
        self.assertEqual(decimal_to_binary(15, 5), '01111', "15 in 5-bit should be '01111'")
        self.assertEqual(decimal_to_binary(16, 5), '10000', "16 in 5-bit should be '10000'")


if __name__ == '__main__':
    unittest.main()