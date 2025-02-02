Below is a step‐by‐step walkthrough for each problem in HW2—covering 2’s complement conversions, SOP (sum of products) derivations from truth tables, thermometer‐to‐binary encoding, and finally K‐Map simplifications.

---

## 1) 2’s Complement Conversions

You have five rows of data to fill out; each row provides a partial specification (decimal, binary, or hex). You must fill in all four columns:

1. **Base‐10** (decimal interpretation, signed for negatives)
2. **Positive Binary** (the unsigned/magnitude binary in 8 bits)
3. **Hexadecimal** (8‐bit form, typically prefixed as `0x??`)
4. **2’s Complement** (the signed 8‐bit representation)

Below is one consistent way to fill in each row.

> **Important**: 2’s complement for a *negative* decimal \(n\) in 8 bits is computed by:
>
> 1. Convert \(|n|\) to binary (8 bits).
> 2. Invert (flip) all bits.
> 3. Add 1.

For a *positive* decimal, the “2’s complement” column is simply the same as the “positive binary” (since its sign bit = 0).

### Row 1

- **Given**: Base‐10 = \(-12\)

| **Base‐10** | **Positive Binary** | **Hex** | **2’s Complement** |
|-------------|---------------------|---------|--------------------|
| -12         | 00001100           | 0x0C    | 11110100           |

Explanation:

- \(|-12| = 12 \ \rightarrow\) `00001100` in binary (8 bits)
- Invert `00001100` → `11110011`, add `1` → `11110100`

---

### Row 2

- **Given**: Positive Binary = `00010101`
  (leading `0` → positive number)

| **Base‐10** | **Positive Binary** | **Hex** | **2’s Complement** |
|-------------|---------------------|---------|--------------------|
| 21          | 00010101           | 0x15    | 00010101           |

Explanation:

- `00010101` in decimal is \(16 + 4 + 1 = 21\).
- Hex for `00010101` is `0x15`.
- Because it is positive, its 2’s complement is identical to the positive binary.

---

### Row 3

- **Given**: Hex = `0x84`
  Interpreted in 8‐bit 2’s complement as a *negative* number because the most significant bit (1) is set.

| **Base‐10** | **Positive Binary** | **Hex** | **2’s Complement** |
|-------------|---------------------|---------|--------------------|
| -124        | 01111100           | 0x84    | 10000100           |

Explanation:

- `0x84` = `10000100` in binary.
- To find decimal value if signed:
  - 2’s complement of `10000100` → invert = `01111011` → add `1` = `01111100` (decimal 124).
  - Hence the value is \(-124\).
- So the “positive binary” (magnitude only) is `01111100`.
- The 2’s complement form is the same `10000100` that was given.

---

### Row 4

- **Given**: `11110001` (presumably the 2’s complement form)

| **Base‐10** | **Positive Binary** | **Hex** | **2’s Complement** |
|-------------|---------------------|---------|--------------------|
| -15         | 00001111           | 0x0F    | 11110001           |

Explanation:

- Interpreting `11110001` as signed 8 bits:
  - Invert = `00001110` (14 decimal) → add `1` = `00001111` (15 decimal).
  - So it represents \(-15\).

---

### Row 5

- **Given**: `00001001` (leading `0` → positive number)

| **Base‐10** | **Positive Binary** | **Hex** | **2’s Complement** |
|-------------|---------------------|---------|--------------------|
| 9           | 00001001           | 0x09    | 00001001           |

Explanation:

- `00001001` is decimal 9.
- Hex = `0x09`.
- Positive → 2’s complement is the same bits.

---

## 2) 2’s Complement Practice Tools

If you need additional practice, many online calculators exist (e.g., [Exploring Binary’s converter](https://www.exploringbinary.com/twos-complement-converter/)). Just verify the calculator’s convention to ensure it is computing *negative* two’s complement in the same way.

---

## 3) Sum‐of‐Products from Truth Tables

### (3a) Two‐Input Table

| A | B | Out |
|---|---|-----|
| 0 | 0 | 0   |
| 0 | 1 | 1   |
| 1 | 0 | 0   |
| 1 | 1 | 1   |

Observe that `Out = 1` whenever \(B=1\).
**SOP**:
\[
\text{Out} = B
\]
(You can also see it as \(\overline{A}B + AB = B\).)

---

### (3b) Three‐Input Table

| A | B | C | Out |
|---|---|---|-----|
| 0 | 0 | 0 | 0   |
| 0 | 0 | 1 | 0   |
| 0 | 1 | 0 | 0   |
| 0 | 1 | 1 | 1   |
| 1 | 0 | 0 | 0   |
| 1 | 0 | 1 | 0   |
| 1 | 1 | 0 | 1   |
| 1 | 1 | 1 | 1   |

The output is 1 for minterms:

- \(A=0,\,B=1,\,C=1\) → \(\overline{A}BC\)
- \(A=1,\,B=1,\,C=0\) → \(AB\overline{C}\)
- \(A=1,\,B=1,\,C=1\) → \(ABC\)

**Sum‐of‐Products**:
\[
\text{Out}
= \overline{A} B C \;+\; A B \overline{C} \;+\; A B C
\]
Sometimes factored:
\[
\text{Out}
= \overline{A} B C \;+\; A B(\overline{C} + C)
= \overline{A} B C \;+\; A B.
\]

---

### (3c/d) 3‐Bit Thermometer Code → Binary

**Thermometer Code** (3 bits) counts:

```
000 → 001 → 011 → 111
```

Interpreting that as 0, 1, 2, 3 in decimal (then presumably wraps around).

- `000₂` → 0 decimal → output `00₂`
- `001₂` → 1 decimal → output `01₂`
- `011₂` → 2 decimal → output `10₂`
- `111₂` → 3 decimal → output `11₂`

Any other 3‐bit combination is a “don’t care” (X) for this particular problem. You would build a truth table with inputs \(T_2, T_1, T_0\) (the thermometer bits) and outputs \(\text{X}_1, \text{X}_0\) (the 2‐bit binary). Rows that aren’t 000, 001, 011, or 111 get `X` for output.

Example partial table:

| T2 | T1 | T0 | (X1 X0) |
|----|----|----|---------|
|  0 |  0 |  0 | 00      |
|  0 |  0 |  1 | 01      |
|  0 |  1 |  0 | X  (don’t care) |
|  0 |  1 |  1 | 10      |
|  1 |  0 |  0 | X  (don’t care) |
|  1 |  0 |  1 | X  (don’t care) |
|  1 |  1 |  0 | X  (don’t care) |
|  1 |  1 |  1 | 11      |

Then you can do one K‐Map for \(\text{X}_1\) and another for \(\text{X}_0\). Because of the “don’t cares” in unused rows, the minimal expressions often simplify nicely.

---

## 4) K‐Map Minimization

You use K‐Maps on each of the truth tables given:

1. **(4a)**: The same 3‐input table from #3(b) but now specifically *reduce it via K‐Maps* (you’ll get the same minimal form \(B + A C\) or similar).
2. **(4b)**: The 4‐input table for \(A,B,C,D\).
   - Fill a 16‐cell K‐Map (rows often labeled by \(A B\), columns by \(C D\), or the other way around).
   - Identify largest prime implicants (circles) to get the minimal Sum‐of‐Products.
3. **(4c)**: The thermometer‐code logic from #3(c) can also be minimized with K‐Maps. You’ll have two K‐Maps (one for each output bit). Include don’t cares (`X`) in the map for unused input rows, which usually leads to a simpler final expression.

---

# Summary of Key Points

- **2’s Complement Table**: Make sure each final 8‐bit pattern is correct and that negative numbers show their “magnitude” in the Positive Binary column and their actual 2’s complement bit pattern in the last column.
- **SOP (Sum of Products)**: List out minterms where the output = 1. Factor if needed or if it simplifies nicely (as in \(\overline{A} B C + AB\)).
- **Thermometer Code**: Only 4 valid states; everything else is X (don’t care). That leads to compact minimal expressions when you K‐Map each output bit.
- **K‐Map Minimization**: Group as many adjacent 1‐cells (and/or don’t cares) as possible to find the minimal SOP form.

That should guide you through all parts of the assignment:

1. Completing the 2’s complement table,
2. Verifying your logic expressions in standard SOP form,
3. Converting thermometer code to binary,
4. And using K‐Maps for minimal expressions.

Good luck!
