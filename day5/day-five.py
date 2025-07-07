import os

# Writing on file using pythong
with open("day5/output.txt",'a') as text_file:
  text_file.writelines(input("What to add in file? : ")+"\n")

with open("day5/output.txt", "r") as textss:
  print(textss.read())
    # for line in textss:
    #    print(f"{line.strip()} okay")



if not os.path.exists("day5/testfolder"):
    os.mkdir("day5/testfolder")
    print("Folder created")
else:
    print("Folder already exists")



# # Get the current working directory (where the script runs)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define path to notes folder inside day5/
notes_folder = os.path.join(current_dir, "notes")



# Step 2: Create topic folder inside notes (e.g., notes/python)
topic_folder_path = os.path.join(notes_folder)

# Step 3: Create folders if they don't exist
if not os.path.exists(topic_folder_path):
    os.makedirs(topic_folder_path)

# Step 4: Ask for note title and content
note_title = input("Enter note title: ")
note_content = input("Enter your note:\n")

# Step 5: Build full file path (e.g., notes/python/list-functions.txt)
file_path = os.path.join(topic_folder_path, note_title + ".txt")

# Step 6: Save the note content
with open(file_path, "w") as file:
    file.write(note_content)

# Step 7: Confirm to user
print(f"\n✅ Note saved to {file_path}")
