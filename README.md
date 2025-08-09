CSV Data Analyzer – Best and Worst States

Overview:
This Python program reads a CSV file, analyzes specific columns of numerical data, and determines which states have the highest and lowest values for each selected column.
The results are saved into a file called best_and_worst.txt.

It is designed to work with CSV files that:
Contain some header lines before the actual column names.
Contain percentage values, "N/A" entries, or other text that needs cleaning before processing.

Features
Reads and cleans CSV data (removes "%" symbols and ignores "N/A" values).
Skips the first 4 lines of the CSV file before reading the column headers.
Analyzes specific columns (currently columns 1, 5, 7, 11, 13).
Finds the minimum and maximum values for each analyzed column.
Saves results into a neatly formatted best_and_worst.txt file.

How It Works:
1.) Prompt for file name:
The program will ask you to enter the name of your CSV file (e.g., data.csv).
2.) Read CSV data:
Skips the first 4 lines.
Reads the column headings.
Cleans and stores the data in a list of lists.
3.) Analyze columns:
For each selected column:
  Finds the lowest and highest state and value.
  Writes them to best_and_worst.txt.
