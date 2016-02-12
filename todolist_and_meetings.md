#To-Do List

###General
- [x] Create list of meetings and a to-do list
- [x] Update README.md file

===

###Weekly Goals
#### General
- [ ] Use completed scripts to produce 'filtered' restrict files containing unique restriction sites for pair of species
- [ ] Open fasta files in Jalview and import 'features.txt' to highlight the restriction sites for pair of species
- [ ] View the restriction sites highlighted and perhaps consider selecting regions recognised in one species, but not so much in the other
- [ ] Consider the approach as to whether selecting restriction sites 'by eye' or perhaps writing out a script, for example to filter out similar sites in both sequences
- [x] Download and familiarise with SnapGene and Primer3
- [ ] Look at mitochondrial sequences to recognise which regions of the DNA are conserved and which are hypervariable
- [ ] Import the 'filtered' restrict files into Primer3
- [ ] Map restriction sites onto the mitochondrial genome in SnapGene
- [ ] Write script together for Primer3 output

===

###Planning Ahead

- [ ] Decide yourselves the approach you will take to select the primer pairs that distinguish the two species from each other when writing a personal script

===

#Meetings

===

###Meeting 6 - Thursday 11/Feb
###Overview

1. Python overview: emboss_Read 
		     - Added list to prevent matching break
		     - Printed at various points to check data is correct at each point (then removed once confirmed)
		            align_emboss
		     - Added lists for unique restriction sites for species a and b
			 - added try/except to give count and unique cuts

2. Actions:

 - Add in 'species_b_unique' list 
 - Decide which cuts are suitable and colour these in a different colour to rest
 - Decide suitable parameters for primer3
 
3. No further issues so far

####Roles and Attendance
| Group Member   | Roles         | Attendance  |
| -------------  |:-------------:| -----------:|
| Imogen Stafford| Presenter     | Present     |
| Simon Bajew    | Chair         | Present     |
| Alan Keith     | Minute Taker  | Present     |
| Maxim Tsenkov  |       -       | Present     |

==

###Meeting 5 - Monday 08/Feb
####Overview

1. Current State of the Project: Script is complete and gives the correct output we need in the right format. Went over what Primer3 is, how it works and the manual online, as well as the different filters and conditions to consider for finding the best primers.

2. Actions: 

 - Download and familiarise with SnapGene and Primer3.
 - Look at mitochondrial sequences to recognise which regions of the DNA are conserved and which are hypervariable.
 - Identifying restriction sites with specific filters and conditions, either choosing them 'by eye' or writing out a personal script to automate the process.
 - Write a script together for Primer3 output by Thursday. 


3. No further issues: everyone felt comfortable to continue with their tasks after discussions.

 ___N.B. - Remember to only email Dr. David Martin the commit number and the script name of your latest copy pushed, instead of sending a block of code___

####Roles and Attendance
| Group Member   | Roles         | Attendance  |
| -------------  |:-------------:| -----------:|
| Simon Bajew    | Presenter     | Present     |
| Imogen Stafford| Chair         | Present     |
| Maxim Tsenkov  | Minute Taker  | Present     |
| Alan Keith     |       -       | Present     |

===

###Meeting 4 - Thursday 04/Feb
####Overview

1. Current State of the Project:

Both codes are partially completed. Guidance given with regards to creation of headers, dictionaries and the loop for adding in gaps for Simon and Alan; altering the loop and aligning two lists correctly for Maxim and Imogen.

2. Actions: 

 - Both groups should complete their code by Monday, with everyone agreeing on the name for _gapstart_. 
 - Look at the Primer3 manual.
 - Look at mitochondrial sequences to recognise which regions of the DNA are conserved and which are hypervariable.
 - Identifying restriction sites which are a suitable length that a primer will have a certain level of specificity for.

3. No further issues: everyone felt comfortable to continue with their tasks after discussions.

####Roles and Attendance
| Group Member   | Roles         | Attendance  |
| -------------  |:-------------:| -----------:|
| Maxim Tsenkov  | Presenter     | Present     |
| Alan Keith     | Chair         | Present     |
| Imogen Stafford| Minute Taker  | Present     |
| Simon Bajew    |       -       | Present     |

===

###Meeting 3 - Monday 01/Feb
###Overview

1. Project Overview
So far, raw alignment has been curated according to curated_alignment.py script. 
The alignment was loaded to EMBOSS to get the idea of how data output looks like. 
Meanwhile, everyone’s working on Python tutorials.

2. Next Steps
  - process curated alignment in EMBOSS (names edited by Dr Martin)
  - data saved in .restrict table format as individual files in a new folder
  - think about reading and sorting data
  - establish strategy for sequence comparison by unique restriction enzyme sites (algorithm provided by Dr Martin)

3. EMBOSS
  - strips alignment out of the gaps -> first challenge is to reassign the restriction sites so that they align to the sequences
  - may create different type of output files -> it was chosen to use .restrict file that presents the output in a table

4. Actions
  - Alan and Simon will write a script to read the data
  - Imogen and Maxim will write a script to process the data
  - ideal scenario: data processed by Thursday, maximum by next Monday
  - Dr Martin was asked to provide more information on:
  
      •	  how to edit files in EMBOSS

      •	  how to process the data using simple loops
      
      •	  useful list of commands
      
      •	  report writing criteria
      
  - Dr Martin will provide more flip chart paper for forthcoming sessions

5. Issues
  - No issues.

===

###Meeting 2 - Thursday 28/Jan
####Overview
1. What has been achieved
  - ___Folders___ created and used to sort the directory
  - Continual progress through various ___Python tutorials___
  - Python code created to ___Loop___ the desired ___List of dictionaries___
  - ___FASTA___ file created from _output_ of python code
2. Current state of the project
  - Table of contents for species completed and displayed on ___README.md___
  - NCBI sequences aligned and processed
  - FASTA file created for realigned sequences
3. Plans and discussion
  - Have a brief look over _EMBOSS_ and work with it in any free time
  - Realign the new _FASTA_ file in jalview  

===

####Roles and Attendance
| Group Member   | Roles         | Attendance  |
| -------------  |:-------------:| -----------:|
| Imogen Stafford| Presenter     | Present     |
| Simon Bajew    | Chair         | Present     |
| Alan Keith     | Minute Taker  | Present     |
| Maxim Tsenkov  |       -       | Present     |

===

#Meetings
###Meeting 1 - Monday 25/Jan
####Overview
1. What has been achieved
  - ___GiHub account___ set up and ___Git tutorial___ completed
  - Progress through ___Python tutorials___, but _not completed_
  - Ability to ___orientate in NCBI___, and fetch the correct and complete nucleotide sequences
  - Capable of ___working on Jalview___, and aligning and editing sequences on display
2. Current state of the project
  - Table of contents for species completed and displayed on ___README.md___
  - NCBI sequences aligned and processed
3. Plans and discussion
The next step is to shift from Jalview to Python, by processing the raw data from Jalview into Python;
Sort the following by ___strings and loops____ on Python
  - Sort sequences and gaps
  - Realign circular mitochondrial sequences

===

####Roles and Attendance
| Group Member   | Roles         | Attendance  |
| -------------  |:-------------:| -----------:|
| Simon Bajew    | Presenter     | Present     |
| Imogen Stafford| Chair         | Present     |
| Maxim Tsenkov  | Minute Taker  | Present     |
| Alan Keith     |       -       | Absent      |
