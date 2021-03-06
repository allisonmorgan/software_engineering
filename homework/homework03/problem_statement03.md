# Homework 3

### Overview

This homework assignment asks you to demonstrate your asynchronous programming skills, your node programming skills, AND your Javascript programming skills all at once!

In the slides for Lecture 12 on slide 36, a program was presented that could determine the total file size for all files in a given directory using asynchronous programming techniques (in this case, Javascript's event loop, node's file system API, and callback functions). The program defaulted to reading the contents of the current directory and it did not traverse into sub-directories.

Your assignment is to write a similar program that will report the total file size for all files in a given directory along with all files contained in all sub-directories (no matter how deep the sub-directories go).

Your program will take one command-line argument, `<directory>`, where `<directory>` can be an absolute or relative path to an input directory. Your program will start its traversal within the given directory.

Your program can generate any output that you desire but the last line of output must be in this form if no errors occur:

`Total size: <total_number_of_bytes>`

where `<total_number_of_bytes>` is replaced with the number that your program calculates.

If an error does occur, then the last line of output generated by your program must start with the prefix `Error: `. Any additional information can appear after that prefix but the last line must start with that prefix. (This means that your program should NOT generate a stack trace when an error occurs.)

Be sure to test your program on multiple directories that between them meet the following three conditions

* the input directory contains files but does not have sub-directories
* the input directory does not contain files but has multiple sub-directories (which also do not contain files)
* the input directory contains multiple files and one or more sub-directories (which, in turn, have files and zero or more sub-directories).

I have a test program that will invoke your submitted program on multiple test directories; for each test directory, the program will compare the final line of output of your program with an expected output value.

### Format

Upload your code as part of a repo on GitHub and send me an e-mail message telling me where it is located. Make sure `kenbod` is a collaborator on that repo. You can, for instance, add this code to the repo you used to turn in Homework 1.

### Collaboration

I **strongly encourage** students work in teams on this assignment. Indeed, you can use this assignment to form the team of 2-5 students you'll use to work on the semester project. The semester project will start in week 9 and will span weeks 9 to 15 of the semester.

### Assignment Header

The source code should be contained in a single file called `total_size.js` and an assignment header should appear at the top of the file that:

* A line that identifies the class and current semester (i.e. CSCI 5828 – Spring 2018)
* A line that identifies the homework assignment (i.e. Homework 3)
* A line that identifies the people who worked on the assignment (list all team members)
* Other embellishments (such as the due date) are fine too

### Javascript Concerns

Your solution can be similar to the original program and make use of node's filesystem API and callbacks to solve this new problem. You are also free to make use of a combination of promises and callbacks (like the `file_total.js` file did in Lecture 13, slide 32; see the sample code for lecture 13). **Under no circumstances are you allowed to use the synchronous functions of Node's file system API.** If you need help with Javascript data types, take a look at <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures> to get started.

### Due Date

This assignment is due by 11:59 PM MST on Friday, March 16, 2018. That means that I must have received an e-mail message from you or your team pointing me at the location of your source code on GitHub by that time.

### Questions?

Send me e-mail and I'll get back to you. Feel free to ask questions in class as well!
