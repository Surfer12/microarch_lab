# Lab Two: Building with Gates

**Submission Date:** Monday, 2/3

────────────────────────────
## 1. Introduction
────────────────────────────
- **Purpose & Objectives**
  – Briefly state what the lab is about (e.g., designing and testing a logic block that uses gates with a fixed carry-in of 0).
  – Explain why this exercise is important (e.g., understanding gate-level design and simulation in LTSpice).

- **Overview of the Project**
  – Outline the steps: design the block, derive truth tables, implement in LTSpice, create a symbol, test the schematic, and simulate.

────────────────────────────
## 2. Part 1 – Main Block Design (Carry-In = 0)
────────────────────────────
### 2.1. Problem Understanding
- Describe the function of the block.
- Explain that the block is the "simpler" version with a carry-in fixed to zero.

### 2.2. Truth Table Creation
- Create a truth table for the SUM output.
- Create a truth table for the CARRY-OUT output.
  – Make sure to list all input combinations and expected outputs.

### 2.3. Logic Expression Derivation (SOP Method)
- Derive the Sum of Products (SOP) for the SUM signal.
- Derive the SOP for the CARRY-OUT signal.
  – Include your working so that the derivation is clear.

### 2.4. Implementation in LTSpice
- Enter the derived logic circuits (for SUM and CARRY-OUT) in LTSpice.
- Create a block symbol (.asy file) for your design.
  – (Include screenshots or file names if needed.)

### 2.5. Test Schematic Development & Simulation
- Develop a new schematic to test the block.
- Describe how you drive the inputs (e.g., using voltage or pulse sources).
- **Simulation Details:**
  – Specify the type of simulation (transient, DC sweep, etc.).
  – Include screenshots of key waveforms that show the correct behavior matched to your truth tables.

### 2.6. Backup and Submission of Design Files
- List and backup all files (e.g., *.asc and *.asy).
- Confirm that every design file is ready for submission.

────────────────────────────
## 3. Part 2 – LSB Block Optimization (Simplified LSB Block)
────────────────────────────
### 3.1. Requirements and Analysis
- Explain any modifications that simplify the LSB block.
- Create a corresponding truth table and derive its logic.

### 3.2. Implementation & Symbol Creation
- Implement the optimized design in LTSpice.
- Show or describe the creation of the new symbol (.asy file).

### 3.3. Testing and Simulation
- Create a top-level schematic to replace and test the original LSB block with this new version.
- Re-simulate the block in the integrated circuit.
- Include simulation results or screenshots that verify its proper operation.

────────────────────────────
## 4. Integration and Overall Testing
────────────────────────────
- Describe how you replaced the original LSB block with your new design in the main circuit.
- Explain the integration process and show simulation results that confirm correct overall operation.

────────────────────────────
## 5. Discussion and Analysis
────────────────────────────
- Summarize the project's key findings, including:
  – Whether the logic behaved as predicted.
  – Any challenges encountered (e.g., issues with carry propagation or simulation anomalies).
  – Lessons learned or insights about gate-level design and circuit integration.

────────────────────────────
## 6. Conclusion
────────────────────────────
- Recap the steps performed during the lab.
- Reflect on the success of your design and any potential improvements for future projects.

────────────────────────────
## 7. Appendices
────────────────────────────
- Include any additional information such as:
  – Extra simulation screenshots
  – Detailed derivations or circuit diagrams that were referenced in the main body
  – A complete list of the backed-up files (*.asc and *.asy)

────────────────────────────
**Submission Notes**
────────────────────────────
- Combine this report (both Part 1 & Part 2) with Wednesday's lab work into one coherent document.
- Make sure to adhere to any additional formatting or cover page requirements as prescribed by your instructor.

────────────────────────────

Good luck with your lab!