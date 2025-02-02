Page 1 of 6
CIS 240: MICROCOMPUTER ARCHITECTURE & PROGRAMMING
Lab 2, 3: Building with gates. Hierarchy (symbols)

This week, we will design a very important part of a computer: The Arithmetic Logic Unit (ALU). The ALU is the component of a computer responsible for performing calculations and data manipulations.

A basic, traditional computer typically consists of four main blocks:

• ALU: Performs mathematical and data manipulation operations.
• Controller: Directs the other blocks, instructing them when and what to do (the boss).
• Memory: Stores data and programs.
• I/O Block: Handles communication with the outside world, off the CPU.

Inside the ALU, you might find various circuits such as adders (for binary number addition), multipliers, dividers, subtractors, and other data manipulation units. The specific functions within an ALU depend on the computer's intended applications. While we haven't yet discussed floating-point numbers, an ALU might be designed to work with 2's complement numbers, floating-point numbers, or both.  For computers processing significant amounts of image data, the ALU might include specialized blocks for efficient linear algebra operations.

We have previously discussed 2's complement representation, but it's important to note that there are alternative methods for representing numbers in computers.  Depending on the design choices made, a computer might use representations like sign-magnitude, 1's complement, or DBNS (double-based number systems), which is a number system I have conducted research on.

This week, our focus will be on addition and subtraction. If time permits and everyone progresses quickly, we will also explore implementing a multiplier. There are numerous adder designs, but we will be constructing a ripple carry adder (RCA). While resources detailing how to build this circuit are readily available, please refrain from consulting them. This exercise is intended as design practice, so please engage in the design process independently.

**Products and Report**

The deliverable for this lab is a report documenting your design process. This report should be written as a helpful guide for future reference. Imagine that in years to come, you might be asked to design a circuit using gates and need a refresher. This report should serve as a resource to aid you in that situation. The initial part of this handout provides background information, and the specific requirements for what is due are outlined at the end.

**Part 1: Design Background**

When undertaking a design task, it is recommended to follow these steps:

1. **Understand the Problem:**  You will be designing an adder, starting with a single block today and progressing to a complete adder on Wednesday. The final adder will take two 4-bit numbers, A and B, as inputs and produce their sum, Out, as output. The symbol for an adder is depicted below:

    [Diagram of Adder Symbol]

    The notation indicates that "N" wires are used in parallel.  Therefore, "A" consists of 4 wires (bits), and "B" also consists of 4 wires (bits). We can represent this using array notation: A[3:0] (representing 4 wires: A[3], A[2], A[1], and A[0]). Similarly, B would be B[3:0], and Out would be Out[4:0]. We will assume that A[3] represents the Most Significant Bit (MSB) of "A".

    The same symbol can be used for other arithmetic operations, with the operation symbol changed from the plus sign to reflect the actual operation performed by the block.

    * Multiplication: [Symbol for Multiplication]
    * Subtraction: [Symbol for Subtraction]
    * Division: [Symbol for Division]

2. **Binary Addition:** Adding in base-2 (binary) is analogous to base-10 addition. However, in base-10, you carry over when the sum in a column is 10 or greater. In base-2, you carry when the sum in a column is 2 or greater.  Generally, if the sum in a column equals or exceeds the base, you carry.

    **Example from Lecture Slides:**

    [Example of Binary Addition]

    The adder we will build today will utilize a specific approach. Notice that each column in binary addition operates in the same way. Consider the circled column in the example. In this column, and in all other columns, to calculate the sum, you add the carry-in bit (0 or 1), a bit from "A", and a bit from "B". To determine if there's a carry-out to the next column to the left, you check if the sum is 2 or greater.

    In the circled column, the carry-in is '1', the bit from "A" is '1', and the bit from "B" is '1'. The sum is therefore 1+1+1=3. Since 3 is greater than 2, a carry is generated. Each carry effectively subtracts the base from the sum. So, with a sum of 3, carrying '1' subtracts the base '2' from '3', resulting in a sum of 3-2=1 and a carry of '1'.

    This pattern is consistent across all columns. You always add the carry-in bit from the column to your right, a bit from "A", and a bit from "B" to obtain a single sum bit and a single carry-out bit. Consequently, if you design a circuit that adds three bits and produces a sum bit and a carry-out bit, you can cascade or chain multiple copies of this circuit together to perform addition on larger binary numbers.

    [Diagram showing cascading adder blocks]

    (In the diagram, red wires represent carry-in signals from the preceding block, and Sum[4:0] represents the final sum. The carry-in for the very first block (LSB) is always zero, as indicated.)

    Today, we will focus on building the Least Significant Bit (LSB) block. Recall that the SUM bit is the result of adding the "A" bit, the "B" bit, and the carry-in bit: A[0]+B[0]+Cin=SUM[0]. However, for the LSB, the carry-in (Cin) is always zero. This simplification allows us to ignore the Cin input for the LSB block, resulting in the equation: A[0]+B[0]=SUM[0]. Similarly, when calculating the carry-out for the LSB, you can also disregard the carry-in. To determine if a carry occurs, you only need to check if the sum of the "A" bit and the "B" bit is greater than or equal to two.

    [Diagrams of Adder Blocks with Inputs and Outputs]

**Lab Activities for Today:**

If any of the preceding material is unclear, please ask for clarification from me or your classmates.

Here are the steps we will follow today (working through them together). Please document all your work for your lab report. This portion of the report will be combined with Wednesday's work to form a complete report due on Monday, February 3rd.

**Report Steps:**

i.  **Design the Block (LSB - Carry-in = 0):** The block we will build today is the simplified version described in the last paragraph of the previous page, where the carry-in is always zero.
    a.  **Understand the Problem:** Describe the function of this simplified block.
    b.  **Create Truth Tables:** Construct two truth tables: one for the SUM output and one for the CARRY-OUT output.
    c.  **Determine Logic (SOP):** Use the Sum of Products (SOP) method to derive the logic expressions for both SUM and CARRY-OUT.
ii. **Enter Circuits into LTSpice:** Implement your designed circuits in LTSpice.
iii. **Create a Symbol:** Generate a symbol for the block in LTSpice.
iv. **Make a Test Schematic:** Create a new schematic in LTSpice to test your block.
v.  **Test and Simulate:** Simulate the block for all possible input combinations. Include screenshots of your simulations in your report.
vi. **Submit Design Files:** You will be asked to submit your design files. Ensure you back up your *.asc and*.asy files.

**Additional Task:**

vii. **Design Simpler LSB Block:** Once your initial circuit is working, design an even simpler block specifically for the LSB.  Since the carry-in is always zero for the LSB, it doesn't need to be an input.
    a.  **Understand the Problem:** Describe the function of this further simplified LSB block.
    b.  **Create Truth Table:** Create a truth table for this simplified LSB block.
    c.  **Determine Logic:** Find the logic expressions for this simplified LSB block.
viii. **Enter Block into LTSpice:** Implement this simpler block in LTSpice.
ix. **Create a Symbol:** Make a symbol for this new block.
x.  **Make a Test Schematic:** Create a new schematic to test the simpler LSB block.
xi. **Test and Simulate:** Simulate the simpler block.
xii. **Replace LSB Block:** Substitute the original LSB block in your design with this new, simpler LSB block.
xiii. **Test and Verify:** Test the overall circuit to ensure it functions correctly with the new LSB block.

**Report Conclusion:**

In your report, follow these outlined steps and include all your work to demonstrate your design process.

## Conceptual Map

• Overview: This lab report details the design and analysis of the ALU, emphasizing key architectural components.
• Key Elements:

* ALU Functionality
* Controller Operations
* Memory Integration
* I/O Communication
