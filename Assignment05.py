# -------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   Gentsch, 2/11/2019, Added code to complete assignment 5
# https://www.tutorialspoint.com/python/python_dictionary.htm
# -------------------------------------------------#

# -- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

# -- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

# -- Processing --#
# Step 1
# When the program starts, load the any data you have

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
# -------------------------------


# Step 1 - Load data from a file
# When the program starts, load each "row" of data
# in "ToDo.txt" into a python Dictionary.
# Add the each dictionary "row" to a python list "table"
# in a text file called ToDo.txt into a python Dictionary.

from ast import literal_eval
objFile = open("Todo.txt", "r")
lstTable = []
for row in objFile: #Loop through the Todo.txt file for each row
    #print(row)
    strData = row.split(",") # splits data into
    #print(strData)
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip("\n")}
    #print(dicRow, "\n")
    lstTable.append(dicRow)
objFile.close()
#print(dicRow)
print(lstTable)

# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"])
        print("*******************************************")
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        dicRow2 = {"Task": input("Enter additional Task: "), "Priority": input("Enter Priority (high or low): ")}
        lstTable.append(dicRow2)
        for row in lstTable:
            print(row["Task"])
        # Step 5 - Remove a new item to the list/Table
    elif (strChoice == '3'):
        while True:
            print("*******************Items*******************")
            for row in lstTable:
                print(row["Task"])
            print("*******************************************")

            strRemove = input("Which would you like to remove? ")
            strPriority = input("An what is the priority of that item? ")
            dicRow = {"Task": strRemove.strip(), "Priority": strPriority.strip()}
            if dicRow not in lstTable:
                    print("That wasn't an option. Try Again \n")
                    continue
            elif dicRow in lstTable:
                lstTable.remove(dicRow)
                print("\nSuccessfully removed item")
                break
            #for row in lstTable:
                #if str(row["Task"]) == strRemove:
                # Tried this as well and it didnt work if row["Task"] == {"Task": strRemove, "Priority": strRemove}:
                    #dicRow = literal_eval("{'Task': \'" + row["Task"] + "\', 'Priority': '" + row["Priority"] + "'}")
                    #lstTable.remove(dicRow)
                    #print("removed item")
                #break
        continue

    # Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("Todo.txt", "a")
        for row in lstTable:
            objFile.write(row["Task"] + ", " + row["Priority"] + "\n")
        print("The data has been saved to the file!")
        objFile.close()

    elif (strChoice == '5'):
        break  # and Exit the program

