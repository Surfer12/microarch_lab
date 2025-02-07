Lab Two Building with Gates
Monday Submission
To get started, just tap or click this placeholder text and begin typing. You can view and edit this document on your Mac, iPad, iPhone, or on iCloud.com.
It’s easy to edit text, change fonts, and add beautiful graphics. Use paragraph styles to get a consistent look throughout your document. For example, this paragraph uses Body style. You can change it in the Text tab of the Format controls.
To add photos, image galleries, audio clips, videos, charts, or any of more than 700 customizable shapes, tap or click one of the insert buttons in the toolbar or drag and drop the objects onto the page. You can layer objects, resize them, and place them anywhere on the page. To change how an object moves with text, select the object and then tap or click the Arrange tab in the Format controls.
Heading
You can use Pages for both word processing and page layout. This Simple Report template is set up for word processing, so your text flows from one page to the next as you type, with new pages created automatically when you reach the end of a page.
In page layout documents, you can manually rearrange pages and freely position text boxes, images, and other objects on the page. To create a page layout document, choose a page layout template in the template chooser. You can also change this document to page layout on your Mac, iPad, or iPhone by turning off Document Body in the Document controls.
“This is an example of a pull quote (a key phrase from your report). Tap or click this text to add your own.”
CIS+240+Lab2+Building+with+gates-notes-annotated.pdf
What to do for today’s lab: If the reading so far doesn’t make sense, please ask me or people around you to clarify. Here are the steps to go through today (we’ll work through this together). Please document all of what you do for your report. This part of the report will be combined with Wednesday’s part for a complete report due on Monday 2/3. Here are the steps I want you to include in your report: i. ii. iii. iv. v. Design the block: The block we’ll build today is the simpler one described in the last paragraph on the last page. The one with a carry-in equal to zero. a. Understand the problem – Describe what the block does. b. Create a truth table – Create two truth tables. One for SUM and one for CARRY-OUT. c. Find the logic for both the SUM and CARRY-OUT – Use SOP to find logic. Enter the circuits into LTSpice Make a symbol for the block Make a new schematic to test the block Test - Simulate the block for all possible inputs. Include screen captures of your simulation. vi. I’ll ask you to submit the design files. So make sure back up *.asc and *.asy files. Additionally: vii. Once you have the circuit working, you will design a simpler block to take the place of the LSB (least significant bit). Note that because the carry in is always zero, it doesn’t need to be an input. a. Understand the problem b. Create a truth table c. Find the logic viii. ix. x. xii. xiii. Enter the block into LTSpice Make a symbol for the block Make a new schematic to test the block xi. Test (simulate the block) Replace the LSB block with your new block Test and make sure it works In your report follow these steps and include all work to show
Today’s Lab Instructions
If the reading so far doesn’t make sense, please ask me or people around you to clarify.
Important: Document every step you take. This documentation will form part of your complete report due on Monday, 2/3 (combined with Wednesday’s work).

[DesignBlock] UnderstandProblem=Describe the function of the block. Explain that the block is a simpler one with a carry-in equal to zero. CreateTruthTable=Create a truth table for the SUM output. Create a truth table for the CARRY-OUT output. FindLogic=Use Sum of Products (SOP) to derive the logic expressions for SUM. Use SOP to derive the logic expressions for CARRY-OUT. [EnterCircuitsIntoLTSpice] InputLogicCircuits=Enter the derived logic circuits for SUM and CARRY-OUT into LTSpice. [MakeSymbolForBlock] CreateSymbol=Design a symbol for the block in LTSpice. [MakeNewSchematicToTestBlock] DesignTestSchematic=Create a new schematic in LTSpice to test the block. [TestBlock] SimulateBlock=Simulate the block for all possible input combinations. Include screen captures of your simulation results. [BackupDesignFiles] BackupFiles=Ensure you have backed up the *.asc and *.asy files. [DesignSimplerBlockForLSB] UnderstandProblem=Describe the function of the simpler block for the LSB, noting that carry-in is always zero. CreateTruthTable=Create a truth table for the simpler block. FindLogic=Use SOP to derive the logic expression for the simpler block. [EnterSimplerBlockIntoLTSpice] InputSimplerBlock=Enter the logic circuit for the simpler block into LTSpice. [MakeSymbolForSimplerBlock] CreateSymbol=Design a symbol for the simpler block in LTSpice. [MakeNewSchematicToTestSimplerBlock] DesignTestSchematic=Create a new schematic in LTSpice to test the simpler block. [TestSimplerBlock] SimulateSimplerBlock=Simulate the simpler block for all possible input combinations. Include screen captures of your simulation results. [ReplaceLSBBlockWithSimplerBlock] UpdateSchematic=Replace the original LSB block with the new simpler block in your schematic. [TestUpdatedBlock] SimulateUpdatedBlock=Simulate the updated block to ensure it works correctly. Include screen captures of your simulation results. [Documentation] IncludeAllWork=Include all work and steps followed in the report. Ensure clarity and completeness in documenting each step.

[[Lab Two Start]]


Steps
Design the Block (Carry-In = 0)
• Overview:
Build the simpler block described in the last paragraph on the final page—the version with a carry-in fixed at zero.
• Tasks:
• Understand the Problem:
Describe what the block does.
• Create Truth Tables:
Prepare two truth tables—one for SUM and one for CARRY-OUT.
• Derive the Logic:
Use the Sum of Products (SOP) method to determine the logic for both SUM and CARRY-OUT.
Implementation in LTSpice
• Enter the circuits into LTSpice.
• Create a symbol for the block.
• Develop a new schematic to test the block.
Simulation
• Simulate the block for all possible inputs.
• Include screen captures of your simulation results.
File Backup
• Ensure that all design files (*.asc and *.asy) are backed up and ready for submission.
LSB Block Design (Simplified)
• Overview:
Once the main circuit is working, design a simplified block to replace the LSB (least significant bit). Note that since the carry-in is always zero, it will not be an input.
• Tasks:
• Understand the Problem:
Describe what the new LSB block should do.
• Create a Truth Table:
Develop a truth table for the new block.
• Derive the Logic:
Use the SOP method (or an appropriate logic derivation method) to define the block’s behavior.
LSB Block Implementation in LTSpice
• Enter the new block into LTSpice.
• Create a symbol for the new block.
• Build a new schematic to test this block.
LSB Block Simulation and Integration
• Simulate the new LSB block to confirm its operation.
• Replace the original LSB block with your new design.
• Test the integrated circuit to ensure everything works as intended.
Lab 2 Requirements
Part 1: Main Block Design
• Design the Block (Carry-In = 0):
• Understand and describe the block function.
• Create truth tables for SUM and CARRY-OUT.
• Derive the logic using the SOP method.
• Implementation:
• Enter the circuits in LTSpice.
• Create a block symbol.
• Develop a test schematic.
• Simulate all input conditions (include screenshots of your simulation).
• File Backup:
• Backup all design files (*.asc and *.asy).
Part 2: LSB Block Optimization
• Design the Simplified LSB Block:
• Analyze the requirements.
• Create a truth table.
• Derive the logic.
• Implementation:
• Enter the new block into LTSpice.
• Create a block symbol.
• Develop a test schematic.
• Simulate the block.
• Integration:
• Replace the original LSB block with the new design.
• Verify that the circuit functions correctly.
Note: Ensure that you document every step thoroughly. This documentation will be combined with Wednesday’s work for the final report due on Monday, 2/3.
Use this structured guide to work through today’s lab and to compile a complete, organized report.
Lab 2 Requirements
Part 1: Main Block Design
Design the block (carry-in = 0)
Understand and describe block function
Create truth tables for SUM and CARRY-OUT
Derive logic using SOP method
Implementation
Enter circuits in LTSpice
Create block symbol
Create test schematic
Simulate all inputs (include screenshots)
Backup *.asc and *.asy files
Part 2: LSB Block Optimization
Design simplified LSB block
Analyze requirements
Create truth table
Derive logic
Implementation
Enter block in LTSpice
Create block symbol
Create test schematic
Simulate block
Integration
Replace original LSB with new block
Verify functionality
Note: Document all steps thoroughly for your report. This part will be combined with Wednesday's work for the final report due Monday 2/3.
Below is a suggested structured format for your Lab Two write-up. You can adapt the headers, numbering, and details as needed. The important part is to clearly present each required step (from understanding the problem, to creating truth tables, to simulation and integration) and provide all relevant screenshots, schematics, and files.

Lab Two: Building with Gates

Submission Date: Monday, 2/3

1. Introduction
	•	Objective
Briefly state the purpose of this lab. For example:
	“The objective of this lab is to design, simulate, and test a simple block with carry-in = 0 (using logical gates in LTSpice) and then optimize the design for a Least Significant Bit (LSB) block without a carry-in input.”
	•	Overview
Give a high-level overview of what will be done in Parts 1 and 2.
	“Part 1 focuses on designing and verifying a single-bit adder block with carry-in set to zero. Part 2 extends the design by creating a simplified LSB block that eliminates the carry-in entirely.”

2. Part 1: Main Block Design (Carry-In = 0)

2.1 Understand the Problem
	•	Provide a brief description of the role of the block and why setting the carry-in to 0 simplifies the logic.

2.2 Create Truth Tables
	•	SUM Table: Include the input variables (e.g., A, B, Cin=0) and the resulting SUM.
	•	CARRY-OUT Table: Same inputs, now focusing on the CARRY-OUT bit.

	Example Layout

(Fill in the question marks with the correct outputs.)

2.3 Derive the Logic (SOP)
	•	Show each Sum of Products step for the SUM output and for the CARRY-OUT output.
	•	Write down the final Boolean expressions for both outputs.

2.4 Enter the Circuits into LTSpice
	•	Explain how you translated the Boolean expressions into LTSpice schematic form.
	•	Mention any specific gates (e.g., AND, OR, NOT, XOR) used.

2.5 Create a Symbol for the Block
	•	Show or describe how you created the symbol (.asy file) in LTSpice.
	•	Optionally include a screenshot of the symbol.

2.6 Develop a New Schematic to Test the Block
	•	Show the top-level schematic you used to test all possible input combinations.
	•	Briefly describe how the inputs are driven (e.g., using voltage sources, pulse sources, etc.).

2.7 Simulation and Results
	•	Simulation Method: Indicate the type of simulation (transient, DC sweep, etc.).
	•	Screenshots: Include relevant waveforms or simulation results that show SUM and CARRY-OUT for the different input combinations.
	•	Comment on the results: Confirm that they match your truth table.

2.8 Backup and Submission of Design Files
	•	List the files you backed up:
	•	*.asc (schematic)
	•	*.asy (symbol)
	•	Mention that you will submit these along with your report.

3. Part 2: LSB Block Optimization (No Carry-In Input)

3.1 Understand the Problem
	•	Briefly restate why the LSB block doesn’t need a carry-in input.
	•	Clarify the difference between this simpler block and the previous one.

3.2 Create a Truth Table for the Simpler Block
	•	Only inputs here are likely A and B (since Cin is removed).
	•	Show the outputs for SUM and CARRY-OUT (if applicable).

	Example Layout

3.3 Derive the Logic
	•	Show the SOP derivation or any simplifications used.
	•	Present the final Boolean expression.

3.4 Implementation in LTSpice
	•	Translate your simplified logic into an LTSpice schematic.
	•	Screenshots or a brief description of how it’s wired.

3.5 Create Symbol and Test Schematic
	•	Create a block symbol for the simpler LSB.
	•	Build a test schematic just like in Part 1 and run a simulation for all possible inputs.

3.6 Simulation Results
	•	Provide screenshots of the simulation waveforms or final table.
	•	Verify that the results match the truth table.

3.7 Integration: Replace Original LSB
	•	Show or describe how you replaced the old LSB block with the new simpler block in the main circuit.
	•	Re-simulate (briefly show results to confirm correct operation).

4. Discussion
	•	Summarize the key findings and observations (e.g., does the logic behave as predicted, any pitfalls discovered, etc.).
	•	If you encountered any design challenges or interesting insights about carry propagation or gate-level implementation, mention them here.

5. Conclusion
	•	Restate the overall success of the lab:
	“Both the main block (with carry-in = 0) and the simplified LSB block performed as expected, verifying the correctness of the SOP-derived logic and LTSpice implementation.”
	•	Highlight any next steps or additional notes.

6. Appendix (Optional)
	•	Include any extra screenshots, code snippets, or additional tables that don’t fit neatly in the main body.
	•	List references or resources (if any were used), such as textbooks, lecture notes, or websites about Boolean logic or LTSpice.

Final Checklist
	1.	Truth Tables for both the main block and the simpler LSB block.
	2.	SOP Derivations for SUM and CARRY-OUT (both blocks).
	3.	LTSpice Schematic screenshots (main circuit and test bench for each block).
	4.	Simulation Waveforms or tabular results.
	5.	Symbol (.asy) files creation details.
	6.	Discussion/Analysis of the results.
	7.	All files (*.asc and *.asy) ready to submit.

Submission Notes
	•	Combine this part of the lab (Part 1 & Part 2) with Wednesday’s work in a single coherent report.
	•	Ensure you adhere to any additional formatting requirements from your instructor (e.g., margins, font size, cover page, etc.).

By following this structure, you’ll have a clear, well-organized report that demonstrates every stage of the project—from concept and design to simulation and backup. Good luck!
