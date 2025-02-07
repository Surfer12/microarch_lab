# Week 3 (2/3, 2/5): Week 3: Finish ALU, registers, memory and computer block diagram.

​

 Summarize

​

>> Previous week's link: [Week 2 (1/27, 1/29): Numbers, data, gates, truth tables, and other digital system design stuff. LTSpice videos](https://cuesta.instructure.com/courses/42443/pages/week-2-1-slash-27-1-slash-29-numbers-data-gates-truth-tables-and-other-digital-system-design-stuff-ltspice-videos "Week 2 (1/27, 1/29): Numbers, data, gates, truth tables, and other digital system design stuff. LTSpice videos.").

>>>>>>>>>>>>> ======================== <<<<<<<<<<<<<<<<

**Monday 2/3:  KMaps (Karnaugh maps),** finish ALU, registers, and memory.

**Prep:**

Part 1: Make sure to do the homework for last week. We will be building on deriving logic from truth tables so please be comfortable with it when you come to class.

Part 2: Reading (optional but one of the better pages I found) on KMaps (chapter 2): [https://rhlab.ece.uw.edu/wp-content/uploads/sites/26/2022/03/Lab-3_-Boolean-Algebra-and-K-Maps.pdf](https://rhlab.ece.uw.edu/wp-content/uploads/sites/26/2022/03/Lab-3_-Boolean-Algebra-and-K-Maps.pdf)  .

**Lecture notes:** 

KMap slides (continuation of last week's slides): [L2_GatesAndSimulatorPart1.pptx](https://cuesta.instructure.com/courses/42443/files/8983337?wrap=1 "L2_GatesAndSimulatorPart1.pptx")[](https://cuesta.instructure.com/courses/42443/files/8983337/download?download_frd=1)[](https://cuesta.instructure.com/courses/42443/files/8961280/download)[](https://cuesta.instructure.com/courses/42443/files/8985881/download)[](https://cuesta.instructure.com/courses/42443/files/8983337/download)

**In Class (Lecture):**

First hour: Lecture will be on KMaps (Karnough maps). Karnough maps are used to simplify logic equations. The fewer gates you use, the faster your circuit will be and the more power efficient it will be.  

**In class (Lab):**

Lab hour: You'll:

1. Designing the more complicated block on the adder lab handout.
    1. You'll make the truth table,
    2. then reduce using KMaps,
    3. and then enter it into LTSpice,
    4. then make a symbol for it
    5. Test it
    6. Then cascade it with your block from last week to make a 4-bit adder. 
    7. Then make a symbol for the adder
    8. Test it

Lab handout: [Lab for week 3 (Monday)](https://cuesta.instructure.com/courses/42443/files/8991996?wrap=1 "CIS 240 Lab2 Building with gatesUPDATED.pdf")[](https://cuesta.instructure.com/courses/42443/files/8991996/download?download_frd=1)[](https://cuesta.instructure.com/courses/42443/files/8978582/download)

Files for lab (same ones from last week): [LogicLibrary.zip](https://cuesta.instructure.com/courses/42443/files/8921084?wrap=1 "LogicLibrary.zip")[](https://cuesta.instructure.com/courses/42443/files/8921084/download)

**Here's a file that includes 8 sources for you to use. It takes the place of voltage sources:**

**[EightInputsForAdderTest.txt](https://cuesta.instructure.com/courses/42443/files/9000342?wrap=1 "EightInputsForAdderTest.txt")[](https://cuesta.instructure.com/courses/42443/files/9000342/download?download_frd=1)**

**To use it, use .inc through the .t button:**

**![image.png](https://cuesta.instructure.com/courses/42443/files/9000344/preview)**

**icon. In your schematic it should look like this:**

**![image.png](https://cuesta.instructure.com/courses/42443/files/9000353/preview)**

**The inputs it supplies are called A1, A2, A3, A4, B1, B2, B3, and B4. You should simulate for 128m to cycle through all possible values.**

**What's due:**

Lab stuff: Add this to your report. We'll add some more to your design/report on Wednesday 2/5 and next week.

Homework: **To be posted soon**.[](https://cuesta.instructure.com/courses/42443/files/8989497/download)

>>>>>>>>>>>>> ======================== <<<<<<<<<<<<<<<<

**Wednesday 2/5:  Registers and memory.** PLEASE TRY TO ATTEND CLASS 2/5!!!! BIG DEAL DAY!!!!

**Prep:**

We will be looking at registers and memory today. A register is a group of flip-flops. One flip-flop stores 1-bit of data. If a computer uses 8-bit words (the basic data chunks are 8-bits long), then the computer's registers are most likely 8-bits long and each register is just 8-flip-flops grouped together. The ALU uses a small group of registers (32 in the assembly language we'll be working with after break but 4 registers for the hardware we're building in class) that store values that the ALU is using at that moment. Values that the ALU isn't using in its present or recent calculations will be moved back to or be stored in RAM memory. Registers are pretty large circuits so you wouldn't want to use them for large amounts of data but they are fast so they can give the ALU the data it needs immediately when the ALU needs it. RAM is made of smaller circuits (so is good at storing a lot of data) but is slower to provide those values when asked. This is a little misleading because you can actually get a piece of data from RAM in around the same amount of time as from the register file (the group of 32- or 4-registers is called the "register file") but the register file is made so you can get two values at the same time - If you are adding two numbers, A+B, you can get both numbers immediately. To add the circuitry to get two numbers at the same time from RAM, it would add quit a bit of area and power costs as well as make the RAM access slower. So registers (the register file) is used for values the ALU has just used, is using, or will use soon and (RAM) memory is for data that needs to be stored but isn't being used right now. Also, registers only store 32 (or 4) pieces of data whereas RAM can store mega- or, recently, giga-bytes of data. 

Part 1: Reading on D flip-flops (circuits that store one bit): [https://www.youtube.com/watch?v=-TFNGklWZCc](https://www.youtube.com/watch?v=-TFNGklWZCc)[![](https://cuesta.instructure.com/images/play_overlay.png)](https://www.youtube.com/watch?v=-TFNGklWZCc) . 

Part 2: Memory video: [https://www.youtube.com/watch?v=F0Ri2TpRBBg](https://www.youtube.com/watch?v=F0Ri2TpRBBg)[![](https://cuesta.instructure.com/images/play_overlay.png)](https://www.youtube.com/watch?v=F0Ri2TpRBBg) [](https://www.youtube.com/watch?v=l6rO5IjyrcQ)

**Lecture notes:** .

**In Class (Lecture): [L3_RegistersAndMemory.pptx](https://cuesta.instructure.com/courses/42443/files/9005884?wrap=1 "L3_RegistersAndMemory.pptx")[](https://cuesta.instructure.com/courses/42443/files/9005884/download?download_frd=1)**

First hour: Registers and register files. 

**In class (Lab): We will work through the rest of the computer together in class and create a block diagram. This will be a big deal on the midterm.**

Adding register file to ALU. 

Lab handout**: We will work through the rest of the computer together in class and create a block diagram. This will be a big deal on the midterm.**[](https://cuesta.instructure.com/courses/42443/files/8991996/download)

Files for lab: [ClassFeb5.zip](https://cuesta.instructure.com/courses/42443/files/9005948?wrap=1 "ClassFeb5.zip") [](https://cuesta.instructure.com/courses/42443/files/9005948/download?download_frd=1) .[](https://cuesta.instructure.com/courses/42443/files/8921084/download)

**What's due:**

Lab stuff: Add this week's lab stuff to your report. Nothing due. 

Homework: See Monday above. Due 2/10.

>>>>>>>>>>>>> ======================== <<<<<<<<<<<<<<<<

Next week's link: [Week 4 (2/10, 2/12): Finishing hardware and how it relates to assembly/machine language.](https://cuesta.instructure.com/courses/42443/pages/week-4-2-slash-10-2-slash-12-finishing-hardware-and-how-it-relates-to-assembly-slash-machine-language "Week 4 (2/10, 2/12): Finishing hardware and how it relates to assembly/machine language")