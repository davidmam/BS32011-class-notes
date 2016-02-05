#To-Do List

###General
- [x] Organise GitHub repositoryby adding new subdirectories and rearranging files (sequences, biographies, tutorials)
- [x] Create list of meetings and a to-do list
- [x] Update README.md file

===

###Weekly Goals
#### General
- [ ] Python tutorials!
- [ ] Git

####Simon and Alan
- [ ] script to read EMBOSS output and present the restriction maps
  - [ ] correct gaps so that each restriction enzyme site refers to a column in the aligned sequence
  - [ ] write a general script

####Maxim and Imogen
- [x] realign .fasta output in Jalview, upload the file

- [ ] script to find restriction enzymes sites to distinguish two species

===

###Planning Ahead

- [ ] think about Primer3 input and output

===

#Meetings

===

###Meeting 4 - Thursday 04/Feb
####Overview

1. Current State of the Project
Both codes are partially completed. Guidance given with regards to creation of headers, dictionaries and the loop for adding in gaps for Simon and Alan; altering the loop and aligning two lists correctly for Maxim and Imogen.

2. Actions
 -Both groups should complete their code by Monday, with everyone agreeing on the name for _gapstart_. 
 -Look at the Primer3 manual.
 -Look at mitochondrial sequences to recognise which regions of the DNA are conserved and which are hypervariable.
 -Identifying restriction sites which are a suitable length that a primer will have a certain level of specificity for.

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
