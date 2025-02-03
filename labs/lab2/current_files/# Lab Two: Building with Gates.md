# Lab Two: Building with Gates
## Monday Submission

**Today's Lab Instructions**

If the reading so far doesn’t make sense, please ask for clarification.  This lab will guide you through building digital logic circuits using gates in LTSpice.  Remember to **document every step** as this documentation will be part of your lab report, due on Monday, 2/3, combined with Wednesday's work.

**Lab Objectives:**

This lab has two main parts:

**Part 1: Main Block Design (Carry-In = 0)**

**Objective:** Design and implement a digital logic block with a carry-in fixed at zero.

**Steps:**

1.  **Design the Block (Carry-In = 0)**
    *   **Understand the Problem:** Describe the function of the block. Explain that this block is a simplified version with the carry-in input always being zero.
    *   **Create Truth Tables:** Construct two truth tables: one for the SUM output and one for the CARRY-OUT output.
    *   **Derive the Logic:** Use the Sum of Products (SOP) method to derive the logic expressions for both the SUM and CARRY-OUT outputs.

2.  **Implementation in LTSpice**
    *   **Enter Circuits:**  Enter the derived logic circuits for SUM and CARRY-OUT into LTSpice.
    *   **Create Symbol:** Design a symbol for this block in LTSpice for easier reuse.
    *   **Test Schematic:** Create a new schematic in LTSpice to specifically test the functionality of your newly designed block.

3.  **Simulation and Testing**
    *   **Simulate Block:** Simulate the block for all possible input combinations to verify its correctness.
    *   **Capture Results:** Include screen captures of your simulation results in your lab report.

4.  **File Backup**
    *   **Backup Files:** Ensure you have backed up all your design files (`*.asc` and `*.asy` files) for submission.

**Part 2: LSB Block Optimization (Simplified Block)**

**Objective:** Design and implement a simplified logic block to replace the Least Significant Bit (LSB) block, taking advantage of the fixed zero carry-in.

**Steps:**

1.  **Design the Simplified LSB Block**
    *   **Understand the Problem:** Describe the function of this simplified block, specifically for the LSB position where carry-in is always zero.
    *   **Create Truth Table:** Develop a truth table for this simplified LSB block.
    *   **Derive the Logic:** Use the SOP method (or any appropriate logic simplification method) to derive the logic expression for this simplified block.

2.  **LSB Block Implementation in LTSpice**
    *   **Enter Block:** Enter the logic circuit for the simplified LSB block into LTSpice.
    *   **Create Symbol:** Design a symbol for this simplified LSB block in LTSpice.
    *   **Test Schematic:** Create a new schematic in LTSpice to test the simplified LSB block.

3.  **LSB Block Simulation and Integration**
    *   **Simulate Block:** Simulate the simplified LSB block to confirm it operates correctly.
    *   **Replace Original Block:** Replace the original LSB block in your main circuit schematic with this new simplified block.
    *   **Verify Functionality:** Test the complete integrated circuit to ensure everything works as intended after replacing the LSB block.

**Lab Report Requirements:**

Your lab report should comprehensively document all steps taken in both Part 1 and Part 2.  Ensure clarity and completeness in documenting each step, including:

*   **For each block design:**
    *   Problem description and function explanation.
    *   Truth tables for all outputs.
    *   Derived logic expressions (using SOP).
    *   LTSpice schematics for the circuits and test benches.
    *   Symbols created for the blocks.
    *   Simulation results (with screenshots) for all input combinations.

*   **File Backup Confirmation:**  Confirmation that `*.asc` and `*.asy` files are backed up.

**Note:** This report, combined with your work from Wednesday's lab, will constitute the complete Lab Two report due on Monday, 2/3.

Use this guide to structure your work and ensure all requirements are met for today's lab and your final report.
