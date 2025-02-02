# Week 2: Digital System Design Overview (1/27 & 1/29)

Previous Week: [Week 1: Course Introduction]

--------------------------------------------------

Section I: Monday 1/27 – Numbers, Binary, and Gates
--------------------------------------------------

● **Prep:**

- **Part 1:** Complete last week’s homework and review base-2 concepts. For extra practice, use this converter:
    <https://www.rapidtables.com/convert/number/base-converter.html>
- **Part 2:** Read about logic gates on GeeksforGeeks:
    <https://www.geeksforgeeks.org/logic-gates/>

● **Lecture Notes:**

- **Continued Slides:**
  - L1_CourseOverviewPart1.pptx _(Download)_
  - L1_CourseOverviewPart1 with scribbles from class _(Download)_
- **New Topics:**
  - Numbers Part 2 _(Download)_
  - Gates! _(Download)_

● **In-Class (Lecture):**

- **First Hour:** Introduction to 2’s complement numbers, exploring logic gates, and their role in circuit design.
- **Second Hour:** Hands-on circuit building using gates.

● **LTSpice Tutorials:**
  _(Ensure LTSpice is installed on lab/classroom computers.)_

- Video 1: Downloading and starting a drawing
    <https://cuesta-edu.zoom.us/rec/share/tDegJ9lfJXNo6X1aZT1ulEqf2Hm5Ump_aOH5Qa79oy5rRywk_rNOOVX-UPJccQn_.Lkyo4_lz9kJwBg17?startTime=1737667447000>
- Video 2: Setting up the files
    <https://cuesta-edu.zoom.us/rec/share/7ci0nb96LW30D2miOKJTILUSnJhMenuNJpKt1f5AVrgvh_mjBR3kd4KIOCL0ZWvv.ndQveofZSezi9iD-?startTime=1737668710000>
- Video 3: Drawing components and wiring
    <https://cuesta-edu.zoom.us/rec/share/7ci0nb96LW30D2miOKJTILUSnJhMenuNJpKt1f5AVrgvh_mjBR3kd4KIOCL0ZWvv.ndQveofZSezi9iD-?startTime=1737668942000>
- Video 4: Creating inputs, simulation, and graphing
    <https://cuesta-edu.zoom.us/rec/share/v0w_OUddE2c2x_amoTBKG-1tquXG8bosgyaBYZqQiwzayfbRsncIVzVCmqiuphMS.9C4M1PElh7ZyqVGD?startTime=1737675355000>
- Video 5: Creating custom symbols
    <https://cuesta-edu.zoom.us/rec/share/zjhkKPUo6XLhtZSxKa7Lly1Bh2Z6ouJJ3O-Q9nmYnI8hcIZzOwAlv9CLUTj9Otho.BCugj2cMbwfTnL79?startTime=1737670569000>
- Video 6: Start-to-finish demonstration
    <https://cuesta-edu.zoom.us/rec/share/pHuVq-A2WJt9Spns3yfuKlmyCrMcyVMsEpFtZ9F2GUWjSDJVxoixHk6xgHs2Nfvp.iT3uyILh33i-3WTP?startTime=1737678314000>

● **In-Class (Lab):**

- **Activity:** Using the simulator to build an adder with gates.
- **Resources:**
  - Lab Handout: _Lab 2: Introduction to LTSpice_ _(Download)_
  - Lab Files: [LogicLibrary.zip](Download)

● **What's Due:**

- **Lab Assignments:** Monday's and Wednesday's lab work are due next Monday (2/3).
- **Homework:** “CIS 240 HW2 2z comp and building with gatesUPDATED.pdf” is due 2/3.
    _(Includes HEX, 2's complement, and logic from truth tables.)_
- **Note:** "Don't cares" will be covered in class on Monday to allow time for the final problem.

--------------------------------------------------

Section II: Comprehensive Breakdown, Conceptual Map & Glossary
--------------------------------------------------

### Detailed List of Key Concepts

1. **Numbers & Data Representations**
   - **Positive Binary Numbers:** Understanding binary representation for positive integers.
   - **2’s Complement Numbers:** Techniques for representing negative numbers.
   - **Base-2 Conversions:** Converting between decimal and binary (using online tools).

2. **Digital Logic & Circuit Design**
   - **Logic Gates:**
     • _Basic Gates:_ AND, OR, NOT, NAND, NOR, XOR, XNOR.
     • _Application:_ Forming the building blocks for complex circuits.
   - **Truth Tables:**
     • _Construction:_ Listing all inputs and outputs.
     • _Analysis:_ Utilizing “don’t care” conditions for simplification.
   - **Circuit Construction:**
     • Building circuits like adders and ALUs using gates.

3. **Simplification Techniques**
   - **Karnaugh Maps (KMaps):**
     • _Usage:_ Visual tool to minimize Boolean expressions.
     • _Application:_ Simplifying logic derived from truth tables.

4. **LTSpice Simulation Tool**
   - **Installation & Setup:** Making sure LTSpice is ready for use.
   - **Drawing & Wiring:** Crafting circuit schematics and connecting components.
   - **Simulation & Analysis:** Running simulations, setting up inputs, and analyzing outputs.
   - **Advanced Features:** Creating custom symbols and following comprehensive video tutorials.

5. **Assignments, Labs, and Resources**
   - **Lab Work:** Introduction to LTSpice and hands-on circuit building.
   - **Homework:** Covering 2's complement and logic design principles.
   - **Supplementary Materials:** Includes lecture slides, lab handouts, external readings, and video tutorials.

### Conceptual Map

Digital System Design (Week 2)

```
   ├── Numbers & Data
   │      ├── Positive Binary Numbers
   │      ├── 2's Complement Numbers
   │      └── Base-2 Conversions
   ├── Digital Logic & Circuit Design
   │      ├── Logic Gates (AND, OR, NOT, etc.)
   │      ├── Truth Tables (with “don’t care” conditions)
   │      └── Circuit Construction (Adder, ALU)
   ├── Simplification Techniques
   │      └── Karnaugh Maps (KMaps)
   ├── Simulation with LTSpice
   │      ├── Setup & Installation
   │      ├── Drawing & Wiring Components
   │      └── Simulation & Analysis
   └── Assignments & Resources
          ├── Homework: 2's complement & logic design
          ├── Lab Work: LTSpice exercises and circuit building
          └── Supplementary Materials: Lecture notes, handouts, external resources
```

### Glossary

- **Binary & 2’s Complement:**
  Methods for representing numerical data in digital systems.

- **Logic Gates:**
  Fundamental circuits (e.g., AND, OR, NOT) used to perform logic operations.

- **Truth Tables:**
  Diagrams that map out outputs for every possible combination of inputs.

- **Circuit Construction:**
  Assembling basic components to design functional digital circuits.

- **Karnaugh Maps (KMaps):**
  Tools for visual Boolean expression simplification.

- **LTSpice:**
  A simulation environment for designing and analyzing electronic circuits.

- **Assignments & Deadlines:**
  Scheduled tasks including lab work and homework submissions.

--------------------------------------------------

Section III: Wednesday 1/29 – Extended Data, KMaps & ALU Lab
--------------------------------------------------

● **Prep:**

- **Part 1:** Read about logic gates:
    <https://www.geeksforgeeks.org/logic-gates/Links>
- **Part 2:** Review gate operations and logic creation from truth tables.
- **Part 3:** Optional: Preview a KMap video (note that many omit key details).

● **Lecture Notes:**

- Refer to Monday's "Numbers Part 2" slides. _(Download)_

● **In-Class (Lecture):**

- **First Hour:** Discussion on alternative data types beyond numbers and an introduction to Karnaugh Maps (KMaps).

● **In-Class (Lab):**

- **Activity:** Continued exploration of logic gate simulation; building an ALU.
- **Resources:**
  - Lab Handout (Updated 1/29): _CIS 240 Lab2 Building with gatesUPDATED.pdf_ _(Download)_
  - Lab Files: Use the same [LogicLibrary.zip](Download) as Monday.

● **What's Due:**

- **Lab Work:** All lab assignments specified in the handout are due by 2/3 midnight (include Monday’s lab products).
- **Homework:** As outlined on Monday, due 2/3.

● **Next Week Preview:**

- Topics for Week 3 include Registers, Memory, and Computer Block Diagrams.
