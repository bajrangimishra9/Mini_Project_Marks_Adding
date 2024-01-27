import csv     

def calculate_total_marks(csv_file):     #function defn and working
    total_marks = {}

    with open(csv_file, 'r') as file:     #file oprning in reading mode
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for roll_number, marks in reader:

            #compute the total marks for given marks
            total_marks[roll_number] = total_marks.get(roll_number, 0) + int(marks) 
    return total_marks

csv_file = '/content/Mini Project - Marks Adding.csv'     #file path coping in a variable
result = calculate_total_marks(csv_file)    #function call and storing the total marks in result variable 

for roll_number, total_marks in result.items():
    print(f'Roll Number: {roll_number}, Total Marks: {total_marks}')   #takes the input of roll no. and marks
