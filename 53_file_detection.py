# PYTHON FILE DETECTION:

# import os


# file_path = "C:/Users/aarav/OneDrive/Desktop"

# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exists")

# else:
#     print("That location doesn't exist")




# WRITING FILES:

# txt_data = "I love you dear zindagi"

# file_path = "C:/Users/aarav/OneDrive/Desktop/text.txt"

# try:
#     with open(file_path, "a") as file:
#         file.write("\n" + txt_data)
#         print(f"txt file {file_path} was created")
# except FileExistsError:
#     print("That file already exists!")




# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]


# file_path = "C:/Users/aarav/OneDrive/Desktop/text.txt"

# try:
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         print(f"txt file {file_path} was created")
# except FileExistsError:
#     print("That file already exists!")



# import json

# employees = {

#     "name" : "SAARAV",
#     "age": "22",
#     "Job": "Engineer"

# }


# file_path = "C:/Users/aarav/OneDrive/Desktop/text.json"

# try:
#     with open(file_path, "w") as file:
#         json.dump(employees, file, indent=4)
#         print(f"json file {file_path} was created")
# except FileExistsError:
#     print("That file already exists!")




# import csv

# employees = [["Name", "Age", 'Job'],
#              [" SAARAV", "22", "Engineering"],
#              ["AARSHI", "19","Doctor"]]


# file_path = "C:/Users/aarav/OneDrive/Desktop/text.csv"

# try:
#     with open(file_path, "w") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"json file {file_path} was created")
# except FileExistsError:
#     print("That file already exists!")
