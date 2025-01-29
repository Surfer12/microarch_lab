
Lab Two :

Build Carryout: circuit in same schematic as 'sum' circuit.

Make symbol for Carryout

Create new schematic and drop heirarchy into it you created

Test Symbol.


To create tool's symbol into gdoc : select bitmap to clipboard and paste into gdoc.




Last redmost - circut schematic









Review floating point representation. Floating-point representation is a fundamental method for approximating real numbers on computers, especially crucial for handling numbers with fractional components, extremely large magnitudes, or infinitesimally small values.  This representation is essential in scientific computing, engineering, and virtually all areas of software development that require real number calculations.

The representation is structured around three key components: a sign bit, an exponent, and a significand (also known as mantissa).

The **sign bit** is a single bit that denotes the number's sign.  By convention, a '0' indicates a positive number or zero, while a '1' signifies a negative number. This is a straightforward binary encoding of the number's polarity.

The **exponent** field determines the scale or magnitude of the number. It represents the power to which the base (typically 2 in binary floating-point) is raised.  To accommodate both positive and negative exponents, a bias is added to the actual exponent value. This is known as the biased exponent.  For example, in single-precision IEEE 754 floating-point, an 8-bit exponent field uses a bias of 127.  Thus, an exponent value of 128 represents an actual exponent of 1 (128 - 127 = 1), and an exponent value of 126 represents an actual exponent of -1 (126 - 127 = -1).

The **significand** (or mantissa) represents the precision of the number. It is the fractional part that is multiplied by the base raised to the power of the exponent. In most floating-point formats, the significand is normalized, meaning it's represented in a form where there's an implicit leading '1' to the left of the binary point (except for the special case of zero and denormalized numbers). This implicit leading '1' is not actually stored, providing one extra bit of precision.  The stored significand is thus only the fractional part after the binary point.

In summary, the binary floating-point representation can be mathematically expressed as:

```
(-1)^sign * (1 + significand) * 2^(exponent - bias)
```

Numerically in binary, this is represented as:


TODO: INSERT BINARY REPRESENTATION

TODO: Find simulator and text/editor for associated with spice that does not include hidden unicode characters or way to remove from Cursor. 


 
Where:
* `sign` is the sign bit (0 for positive, 1 for negative).
* `significand` is the fractional part stored in the significand field. The '1+' accounts for the implicit leading '1'.
* `exponent` is the value stored in the exponent field.
* `bias` is the exponent bias (e.g., 127 for single-precision IEEE 754).

This formula illustrates how the three components work together to represent a wide range of real numbers with varying precision and scale within the constraints of a fixed number of bits.  Understanding this representation is crucial for anyone working with numerical computation on computers.

Iterative speed of LT SPICE is fastest for debug + analysis

Gate name

Truth Table 

Symbol

Notation

Notation : A * B = OUT

AND Gate
'''
image
'''
