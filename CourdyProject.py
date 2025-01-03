import csv

def read_csv_data(file_name):
    csv_data_list = []

    with open(file_name, 'r') as file:
        reader = csv.reader(file)

        for i in range(4):
            next(reader)

        heading = next(reader)

        for i in heading:
            csv_data_list.append([])

        for row in reader:
            for i, value in enumerate(row):
                clean_value = value.strip()
                if value != 'N/A':
                    clean_value = value.replace('%', '')
                    try:
                        clean_value = float(clean_value)
                    except ValueError:
                        pass
                    csv_data_list[i].append(clean_value)

    return csv_data_list
    

def get_lowest(file_data, states):
    values = []

    for value in file_data[1:]:
        if isinstance(value, str):
            clean_value = value.replace(".", "", 1).strip()
            if clean_value.isdigit():
                values.append(float(clean_value))
        elif isinstance(value, float) or isinstance(value, int):
            values.append(float(value))
    
    lowest_value = min(values)
    lowest_index = values.index(lowest_value)
    lowest_state = states[lowest_index + 1]
                
    return lowest_state, lowest_value
    

def get_highest(file_data, states):
    values = []

    for value in file_data[1:]:
        if isinstance(value, str):
            clean_value = value.replace(".", "", 1).strip()
            if clean_value.isdigit():
                values.append(float(clean_value))
        elif isinstance(value, float) or isinstance(value, int):
            values.append(float(value))

    highest_value = max(values)
    highest_index = values.index(highest_value)
    highest_state = states[highest_index + 1]
        
    return highest_state, highest_value
    

def extract_column_heading(file_data):
    
    return file_data[0]
    

def best_and_worst(find_column, highest_state, highest_value, lowest_state, lowest_value):
    with open("best_and_worst.txt", 'a') as output_file:

        heading = f"{extract_column_heading(find_column)}:".ljust(40)
        lowest_info = f": {lowest_state} : {lowest_value:.1f}".center(30)
        highest_info = f": {highest_state} : {highest_value:.1f}".rjust(35)

        output_file.write(f"{heading}{lowest_info}{highest_info}\n")
    

def main():
    while True:
        try:
            file_name = input("Enter the name of the file: ")
            csv_data_list = read_csv_data(file_name)
            break
        except FileNotFoundError:
            print("File not found, please try again.")

    states = csv_data_list[0]

    with open ("best_and_worst.txt", 'w') as output_file:
        output_file.write("Indicator".ljust(40) + ": Min ".center(30) + "Max".rjust(30) + "\n")
        output_file.write("-"*105 + "\n")

    analyze_columns = [1, 5, 7, 11, 13]

    for index in analyze_columns:
        find_column = csv_data_list[index]
            
        lowest_state, lowest_value = get_lowest(find_column, states)
        highest_state, highest_value = get_highest(find_column, states)

        best_and_worst(find_column, highest_state, highest_value, lowest_state, lowest_value)

main()