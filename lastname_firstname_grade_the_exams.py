import numpy as np
import pandas as pd

NUM_OF_DATA = 26
ANSWER_KEYS = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"

def validate_student_response(response):
    data = response.strip().split(",")
    response_length = len(data)
    status = False

    if response_length != NUM_OF_DATA:
        print(f"Invalid line of data: does not contain exactly 26 values:\n{response}")
    else:
        student_id = data[0]

        if not student_id or student_id[0] != "N" or len(student_id[1:]) != 8 or not student_id[1:].isdigit():
            print(f"Invalid line of data: N# is invalid\n{response}")
        else:
            status = True

    return status, data


def main():
    try:
        file_name = input("Enter a class file to grade (i.e. class1 for class1.txt): ").strip()
        file_path = "./Data Files/" + file_name + ".txt"

        total_lines = 0
        valid_lines = 0
        list_of_correct_responses = []

        with open(file_path, "r") as file:
            print(f"Successfully opened {file_name}.txt")
            print("**** ANALYZING ****")
            for line in file.readlines():
                # Skip blank row
                if not line.strip():
                    continue

                total_lines += 1
                is_valid, obj_data = validate_student_response(line)
                student_marks = [0] * 25

                # Continue processing when the data in line is in valid format.
                if is_valid:
                    valid_lines += 1
                    student_id = obj_data[0]
                    student_response = obj_data[1:]
                    correct_answers = ANSWER_KEYS.split(",")
                    student_dict = {"StudentID": student_id}
                    for idx in range(1, 26):
                        student_selection = student_response[idx-1].strip()
                        correct_answer = correct_answers[idx-1].strip()
                        
                        if not student_selection: # No point for skipped answer
                            point = 0
                        elif student_selection == correct_answer: # 4 points for correct answer
                            point = 4
                        else: # -1 point for wrong answer
                            point = -1
                            
                        student_dict["SUBJECT" + str(idx)] = point
                        
                    list_of_correct_responses.append(student_dict)
                    
            if total_lines == valid_lines:
                print("No errors found!")

        print("**** REPORT ****")
        print("Total valid lines of data: ", valid_lines)
        print("Total invalid lines of data:", total_lines - valid_lines)
        
        df = pd.DataFrame(list_of_correct_responses)
        df.set_index("StudentID", inplace=True)
        df["Total"] = df.sum(axis=1)

        # Pandas
        new_df = df[["Total"]]
        new_df.describe()

        # Numpy
        marks = new_df["Total"].tolist() # Convert pandas Series to Python list
        marks_np = np.array(marks) # Convert Python list to numpy array

        print("Mean (average) score: ", marks_np.mean())
        print("Highest score: ", marks_np.max())
        print("Lowest score: ", marks_np.min())
        print("Range of scores: ", marks_np.max() - marks_np.min())
        print("Median score: ", np.median(marks_np))

        new_df.reset_index(inplace=True)
        grades = new_df.values.tolist()

        # Write data to file
        with open(f"./processed/{file_name}_grades.txt", "w") as w_file:
            for student, mark in grades:
                w_file.write(f"{student},{mark}\n")

            print("Finish writting processed file!")

    except FileNotFoundError as ex:
        print(f"Cannot find the file named {file_name} in 'Data Files' folder, please check and run the program again.")
        print(f"Exception : {ex}")

    except BaseException as ex1: # Catch on the unhandled exception
        print("There was unhandled exception. Please check the log file.")
        print(f"Exception : {ex1}")


while True:
    main()
    answer = input("\n\nDo you want to continue processing another file? (Y/N): ").strip()
    if answer.upper() != "Y":
        print("Exitting!")
        break
