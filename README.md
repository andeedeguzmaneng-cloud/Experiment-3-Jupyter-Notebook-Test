# Experiment-3-Jupyter-Notebook-Test

This repository contains a Jupyter Notebook with two solved Python problems using the Pandas library. The goal is to apply and utilize Pandas functions for various data analysis tasks, such as loading datasets, subsetting, slicing, and indexing data.

Problems Included:

      PROBLEM 1: Loading and Displaying Data
      PROBLEM 2: Subsetting and Slicing Data

_____________________________________

Getting Started with Jupyter Noteboook

        To begin creating your Python code using Jupyter Notebook:
        
                1. Open Anaconda Navigator on your computer.
                2. Look for Jupyter Notebook and open it.
                3. Once Jupyter Notebook launches in your browser, you can create a folder to keep all your Jupyter files organized.
                4. Open the folder where you want to save your work.
                5. Click the New button (on the top-right side).
                6. From the dropdown, select Python 3 (ipykernel).
                
        A new Jupyter Notebook will open — and now you can start writing and running your Python code!

_____________________________________

IMPORTING LIBRARY

Before starting with the problems, you'll need to import the pandas library, as both problems make use of it.

--- CODE ---

	[]: import pandas as pd    # Import pandas library

_____________________________________

Problem # 1. 

Loading and Displaying Data

In this problem, you will load a provided CSV file into a Pandas DataFrame and display both the first and last five rows using head() and tail() functions.

--- CODE ---

	[]: url = "http://bit.ly/Cars_file"            # Load the CSV file from the URL              
	[]: cars = pd.read_csv(url)

	[]: print("First five rows:")                  # Display the first five rows
	[]: print(cars.head())

	[]: print("\nLast five rows:")                 # Display the last five rows          
	[]: print(cars.tail())

--- EXECUTION / RUNNING THE CODE ---

To execute the code cell:

	1. Click inside the cell
	2. Then click the Run botton
	3. The output will appear dirctly below the cell

Note this are the outputs it may give:

         1. No Output: Nothing is displayed because the code only defines something it can be a function or variable but does not print it yet.
         2. Normal Output: This is when the program successfully prints a result. 
         3. Input Prompt: The program asks the user to type something before continuing.
         4. Error Message: A red message shown when the code has a mistake or when an undefined variable or function is used.
 
--- OUTPUT ---

    The program prints the first five and last five rows of the dataset.

--- DEFINITON OF SYNTAX USED ---

    1. import pandas as pd → loads the pandas library.
    2. pd.read_csv(url) → loads the dataset from the URL into a DataFrame.
    3. .head() → displays the first five rows of the DataFrame.
    4. .tail() → displays the last five rows of the DataFrame.
    5. print() → displays the output to the console.

_____________________________________

Problem # 2

Subsetting and Slicing Data

This problem demonstrates how to use subsetting, slicing, and indexing techniques in Pandas to filter and extract specific data from the loaded DataFrame.

--- CODE ---

	[]: url = "http://bit.ly/Cars_file"                                        # Load the dataset
	[]: cars = pd.read_csv(url)

	[]: odd_columns = cars.iloc[:, ::2]                                        # a. First five rows with odd-numbered columns (0-indexed: 0, 2, 4,...)
	[]: print("a. First five rows with odd-numbered columns:")
	[]: print(odd_columns.head())

	[]: print("\nb. Row for 'Mazda RX4':")                                     # b. Row where Model == 'Mazda RX4'
	[]: print(cars[cars['Model'] == 'Mazda RX4'])

	[]: camaro_cyl = cars[cars['Model'] == 'Camaro Z28']['cyl'].values[0]      # c. Cylinders of 'Camaro Z28'
	[]: print(f"\nc. 'Camaro Z28' has {camaro_cyl} cylinders.")

	[]: models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']            # d. Cylinders and gear of specific models
	[]: selected = cars[cars['Model'].isin(models)][['Model', 'cyl', 'gear']]
	[]: print("\nd. Cylinders and gear types for selected models:")
	[]: print(selected)

--- EXECUTION / RUNNING THE CODE ---

To execute the code cell:

	1. Click inside the cell
	2. Then click the Run botton
	3. The output will appear dirctly below the cell

Note this are the outputs it may give:

         1. No Output: Nothing is displayed because the code only defines something it can be a function or variable but does not print it yet.
         2. Normal Output: This is when the program successfully prints a result. 
         3. Input Prompt: The program asks the user to type something before continuing.
         4. Error Message: A red message shown when the code has a mistake or when an undefined variable or function is used.
 
--- OUTPUT ---

    1. The program prints:
    2. The first five rows with odd-numbered columns.
    3. The row for Mazda RX4.
    4. The number of cylinders in Camaro Z28.
    5. Cylinders and gear types for the selected models.

--- DEFINITON OF SYNTAX USED ---

    1. .iloc[:, ::2] → selects columns with odd indices (0, 2, 4...).
    2. cars[cars['Model'] == 'Mazda RX4'] → filters rows where the Model is Mazda RX4.
    3. .values[0] → retrieves the first value from a filtered series.
    4. .isin(models) → filters rows where the Model is one of the specified models.
    5. [['Model', 'cyl', 'gear']] → selects only the specified columns (Model, cyl, and gear).
    6. print() → displays the output to the console.

_____________________________________

Now that you’re done with all the problems, the next step is to download your file as .py and upload your file to GitHub so it can be saved, shared, and accessed easily.

--- DOWNLOADING AS PY FILE ---

Steps to Save as Executable Python Script:

    1. Open Jupyter Notebook with your code.
    2. Click File > Save and Export Notebook As > Executable Script.
    3. The Python file (.py) will be downloaded to your default folder.

--- PROCEDURE FOR UPLOADING TO GITHUB ---

        1. Open your web browser and go to GitHub.
        2. Sign in to your GitHub account.
        3. On the top-right, click the + (plus) button and choose New repository.
        4. Enter a Repository Name (for example: Experiment-3-Jupyter-Notebook-Test).
        5. Turn on "Add a README file" so the repository starts with a description.
        6. Click Create repository.
        7. Once inside the repository, click Add file → Upload files.
        8. Click Choose your files and select the .py files
        9. Scroll down and click Commit changes to upload it.

Now your files is saved and viewable in your GitHub repository. 


 
