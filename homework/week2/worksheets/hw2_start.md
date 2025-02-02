CIS 240: MICROCOMPUTER ARCHITECTURE & PROGRAMMING
HW2: 2’s complement and building with gates

1. 2’s complement
Fill in this table. Do row by row like we did in class. All answers need to be
8-bits.
Row # Base-10 Positive binary Hexadecimal 2’s complement
① -1210
② 000101012
③ 0x84
④ 111100012
⑤ 000010012
2. If you need more practice, find an on-line calculator for any of these
representations and test yourself. Be careful with the 2’s complement
calculators. Some of them flip any number you put into the calculator.
Look for one that’s decimal to 2’s complement like:
<https://www.exploringbinary.com/twos-complement-converter/>
3. SOP (sum of product) from truth table. Find the logic for the digital circuit
described by the following truth tables.
a.
Inputs Output
A B Out
0 0 0
0 1 1
1 0 0
1 1 1
b.
Inputs Output
A B C Out
0 0 0 0
0 0 1 0
0 1 0 0
0 1 1 1
1 0 0 0
1 0 1 0
1 1 0 1
1 1 1 1
c. d. Make a truth table that converts 3-bit thermometer code to binary.
Thermometer code counts up:
0002 → 0012 → 0112 → 1112
In thermometer code, 0002=010, 0012=110, 0112=210, and 1112=310.
Also note that if you count up from 1112 in this particular problem,
let’s say you go back to zero. HINT: In the truth table, any row not
used can have an output of X (for don’t care).
Find the logic for your thermometer code truth table.
4. KMaps: Find the minimal logic (biggest circles).
a.
Inputs Output
A B C Out
0 0 0 0
0 0 1 0
0 1 0 1
0 1 1 1
1 0 0 0
1 0 1 1
1 1 0 1
1 1 1 1
b.
Inputs Output
A B C D Out
0 0 0 0 1
0 0 0 1 1
0 0 1 0 1
0 0 1 1 0
0 1 0 0 1
0 1 0 1 1
0 1 1 0 0
0 1 1 1 0
1 0 0 0 1
1 0 0 1 0
1 0 1 0 1
1 0 1 1 0
1 1 0 0 1
1 1 0 1 1
1 1 1 0 0
1 1 1 1 0
c. Use KMaps to find minimal logic for the truth table for the
thermometer code counter in question 3c.
