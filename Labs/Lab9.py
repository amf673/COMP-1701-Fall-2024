
# Lab 9 
# 
# 

STUDENT_NAME = 0 
QUIZ_1 = 1
QUIZ_2 = 2
QUIZ_3 = 3
QUIZ_4 = 4

QUIZ_1_MAX = 10
QUIZ_2_MAX = 10
QUIZ_3_MAX = 20
QUIZ_4_MAX = 16

QUIZ_1_WEIGHT = 20
QUIZ_2_WEIGHT = 20
QUIZ_3_WEIGHT = 30
QUIZ_4_WEIGHT = 30


def grade_calculation(student:list)->float:
    """ Calculate the weighted average for a student. """

    total = int(student[QUIZ_1])/QUIZ_1_MAX * QUIZ_1_WEIGHT + \
            int(student[QUIZ_2])/QUIZ_2_MAX * QUIZ_2_WEIGHT + \
            int(student[QUIZ_3])/QUIZ_3_MAX * QUIZ_3_WEIGHT + \
            int(student[QUIZ_4])/QUIZ_4_MAX * QUIZ_4_WEIGHT 
    
    return total


def letter_grade(score:float)-> str:
    """ Return the letter grade for the score given."""

    letter = "A"
    if score < 50: 
        letter = "F"
    elif score <60:
        letter = "D"
    elif score < 70:
        letter = "C"
    elif score < 80:
        letter = "B"

    return letter  


def main() -> None: 

    input_file_name = input("Input File Name: ")
    input_file = open(input_file_name, "r")

    output_file_name = "L9_output.txt"
    output_file = open(output_file_name, "w")

    count = 0
    total = 0 
    header = input_file.readline()

    headings = "Name             Percentage Grade\n---------------------------------"
    print(headings)
    output_file.write(headings + "\n")

    line = input_file.readline()
    while line != "": 
        student_record = line.split("|")
        score = grade_calculation(student_record)
        total = total + score
        row_str = f"{student_record[STUDENT_NAME]:20} {score:6.1f} {letter_grade(score)}"
        print(row_str)
        output_file.write(row_str + "\n")

        count = count + 1
        line = input_file.readline()
    input_file.close()
    average = total/count
    footer = f"\n---------------------------------\nAverage {average:19.1f}\n{count} records processed"
    print(footer)
    output_file.write(footer+ "\n")

main()