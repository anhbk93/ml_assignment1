
# Project name: Test Grade Calculator

Project Requirement

Complete the following tasks in the project:

# Task 1:

Create a new Python program called “lastname_firstname_grade_the_exams.py.” (Make sure your source code file is inside of the same folder as the data files you just downloaded.)

Next, write a program that lets the user type in the name of a file. Attempt to open the supplied file for reading access. If the file exists you can print out a confirmation message. If the file doesn’t exist you should tell the user that the file cannot be found and prompt them again.

Use a try/except block to do this (don’t just use a series of “if” statements—we want this program to be as “generic” as possible). You will not get credit for this part of the program if you write something like the following to identify valid data files:

```python
filename = input("Enter a filename: ")
if filename == "class1":
        # open class1.txt
elif filename == "class2":
        # open class2.txt
else:
        print ("Sorry, I can't find this filename")
```

Here’s a sample running of the program:

Enter a class file to grade (i.e. class1 for class1.txt): foobar
File cannot be found.
Enter a class file to grade (i.e. class1 for class1.txt): class1
Successfully opened class1.txt

# Task 2:

Next, you will need to analyze the data contained within the file you just opened to ensure that it is in the correct format. Each data file contains a series of student responses in the following format:

N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D

or

N12345678,B,,D,,C,B,,A,C,C,,B,A,B,A,,,,A,C,A,A,B,D,

The first value is the student’s ID number. The following 25 letters are the student responses to the exam. All values are separated by commas. If there is no letter following a comma, this means the student skipped answering the question.

Note that some lines of data may be corrupted! For example, this line of data does not have enough answers:

N12345678,B,A,D,D,C,B

And this line of data has too many answers:

N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D,A,B,C,D,E

Your tasks for this part of the program is to do the following:

Report the total # of lines of data stored in the file.

Analyze each line and make sure that it is “valid.”

A valid line contains a comma-separated list of 26 values

The N# for a student is the first item on the line. It should contain the character “N” followed by 8 numeric characters.

If a line of data is not valid you should report it to the user by printing out an error message. You should also count the total # of valid lines of data in the file.

Hints: Use the split method to split apart the data from the file. You may need to use this method a few times along with a loop or two. Think about the order in which you need to split your items. For example, your file is organized so that one student’s record occupies an entire line in the file. Splitting first on the line break will isolate each student’s data. Then you will need to further split each item based on the separator character to pull out the responses for each student.

Here is a sample running of your program for the first two data files. A complete listing of the expected output for all data files can be found in the downloadable package for this assignment.

```
Enter a class to grade (i.e. class1 for class1.txt): class1
Successfully opened class1.txt
**** ANALYZING ****
No errors found!
**** REPORT ****
Total valid lines of data: 20
Total invalid lines of data: 0
Enter a class to grade (i.e. class1 for class1.txt): class2
Successfully opened class2.txt
**** ANALYZING ****
Invalid line of data: does not contain exactly 26 values:
N00000023,,A,D,D,C,B,D,A,C,C,,C,,B,A,C,B,D,A,C,A,A
Invalid line of data: N# is invalid
N0000002,B,A,D,D,C,B,D,A,C,D,D,D,A,,A,C,D,,A,C,A,A,B,D,D
Invalid line of data: N# is invalid
NA0000027,B,A,D,D,,B,,A,C,B,D,B,A,,A,C,B,D,A,,A,A,B,D,D
Invalid line of data: does not contain exactly 26 values:
N00000035,B,A,D,D,B,B,,A,C,,D,B,A,B,A,A,B,D,A,C,A,C,B,D,D,A,A
**** REPORT ****
Total valid lines of data: 21
Total invalid lines of data: 4
```

# Task 3:

Next, you are going to write a program to grade the exams for a given section. The exam was a 25-question, multiple-choice exam. Here is a string that represents the answer key:

answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"

Your program should use this key to compute a score for each valid line of data. Scores can be computed as follows:

+4 points for every right answer
0 points for every skipped answer
-1 point for every incorrect answer
You will also want to compute the following statistics for the entire class:

The average score
The highest score
The lowest score
The range of scores (the highest minus the lowest)
The median value (Sort the grades in ascending order. If the # of students is odd you can take the middle of all the grades (i.e. [0, 50, 100]—the median is 50). If the # of students is even you can compute the mean by averaging the middle two values (i.e. [0, 50, 60, 100]—the median is 55).
Hint: Once you’ve scored the students you should use a list to store individual student scores; you can then compute statistics after you’ve examined every student in the file.

Here is a sample running of your program for the first two data files. A complete listing of the expected output for all data files can be found in the downloadable package for this assignment.

```
Enter a class to grade (i.e. class1 for class1.txt): class1
Successfully opened class1.txt
**** ANALYZING ****
No errors found!
**** REPORT ****
Total valid lines of data: 20
Total invalid lines of data: 0 
Mean (average) score: 75.60
Highest score: 91
Lowest score: 59
Range of scores: 32
Median score: 79.5
Enter a class to grade (i.e. class1 for class1.txt): class2
Successfully opened class2.txt 
**** ANALYZING **** 
Invalid line of data: does not contain exactly 26 values:
N00000023,,A,D,D,C,B,D,A,C,C,,C,,B,A,C,B,D,A,C,A,A 
Invalid line of data: N# is invalid
N0000002,B,A,D,D,C,B,D,A,C,D,D,D,A,,A,C,D,,A,C,A,A,B,D,D 
Invalid line of data: N# is invalid
NA0000027,B,A,D,D,,B,,A,C,B,D,B,A,,A,C,B,D,A,,A,A,B,D,D 
Invalid line of data: does not contain exactly 26 values:
N00000035,B,A,D,D,B,B,,A,C,,D,B,A,B,A,A,B,D,A,C,A,C,B,D,D,A,A 
**** REPORT **** 
Total valid lines of data: 21
Total invalid lines of data: 4 
Mean (average) score: 78.00
Highest score: 100
Lowest score: 66
Range of scores: 34
Median score: 76
```

# Task 4:

Finally, have your program generate a “results” file that contains the detailed results for each student in your class. Each line of this file should contain the student’s ID number, a comma, and then their grade. You should name this file based on the original filename supplied—for example, if the user wants to analyze “class1.txt” you should store the results in a file named “class1_grades.txt”.

Here is a sample running of your program for the first two data files. A complete listing of the expected output for all data files can be found in the downloadable package for this assignment.

### this is what class1_grades.txt should look like                               
N00000001,59
N00000002,70
N00000003,84
N00000004,73
N00000005,83
N00000006,66
N00000007,88
N00000008,67
N00000009,86
N00000010,73
N00000011,86
N00000012,73
N00000013,73
N00000014,78
N00000015,72
N00000016,91
N00000017,66
N00000018,78
N00000019,78
N00000020,68
### this is what class2_grades.txt should look like
N00000021,68
N00000022,76
N00000024,73
N00000026,72
N00000028,73
N00000029,87
N00000030,82
N00000031,76
N00000032,87
N00000033,77
N00000034,69
N00000036,77
N00000037,75
N00000038,73
N00000039,66
N00000040,73
N00000041,91
N00000042,100
N00000043,86
N00000044,90
N00000045,67

# Task 5:
Use only pandas and numpy when you implement task 1 to task 4.