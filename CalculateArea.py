# Import necessary modules
import os
import time

# Folder Path
path = 'C:/Users/Evans/Desktop/Pixel Academy/Python Practice Projects/Coordinates/Coordinates'

# Change directory
os.chdir(path)

# Since we don't know the smallest area, we give a temporary value of ten.
smallest_area = 10
file_names = 0

def read_text_file(file_path):
    global smallest_area
    global file_names
    with open(file_path, 'r') as f:
        inputString = f.read()
        itemsInString = inputString.split("\n") # splitting the text by new line delimiter
        itemsInString.pop(-1) # let's remove the last item since it is just a new line with empty data
    
        total_area = 0
        # iterate through the list to calculate area of each rectangle
        for each in itemsInString:
            #a = itemsInString[m]
            #print(each)
            each_to_list = each.split(" ")
            # we use pop() method to remove items at specified index
            each_to_list.pop(0) # index values
            each_to_list.pop(-1) # empty string
            #print(each_to_list)
            
            # Let's now assign values to x and y
            x1 = float(each_to_list[0])
            y1 = float(each_to_list[1])
            x2 = float(each_to_list[2])
            y2 = float(each_to_list[3])
            
            # let's now perform computation to get area of each rectangle
            length = x1 - x2 # get length of each rectangle
            height = y1 - y2 # get width of each rectangle
            
            # Formula to obtain area
            area = length * height
            #print(area)
            
            # Validating results. (-) values should be changes to positive
            if area < 0: # Applies to all negative values
                area = area*-1
                #print(area)
                total_area += area
            else:
                total_area += area
        
        total_area = round(total_area, 5)
        print("Text File", file_name, "has an area of", total_area)
        #print(file_name)
        # Find the smallest area
        if total_area < smallest_area:
            smallest_area = total_area
            if total_area == smallest_area:
                file_names = file_name
        



# Iterating through all the files in our folder
for file in os.listdir():
    # Check whether the file is in .txt format
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
        file_name = file_path.split("_") # split the file names with underscore(_) as the delimiter
        file_name = file_name[1].split(".") # split the text_file number with (.) as the delimiter
        file_name = file_name[0] # save the value in the first index
        read_text_file(file_path) # call read text file function
        time.sleep(0.25)


time.sleep(2)
print("The smallest area is", smallest_area,", which is from the text file", file_names)
