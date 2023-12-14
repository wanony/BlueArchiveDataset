import os
from collections import defaultdict

input_files = []
for root, dirs, files in os.walk("Formatted/"):
    for file in files:
        file_path = os.path.join(root, file)
        input_files.append(file_path)

characters = defaultdict(list)

for input_file in input_files:
    with open(input_file, 'r') as f:
        # loop through all the formatted files
        for line in f:
            line = str(line)
            parts = line.split(':', 1)
            character_name = parts[0].lower()
            line_text = "".join(parts[1:])

            # add character name to dict
            characters[character_name].append(line_text)


# Create a folder to store character files
character_folder = "Formatted/Characters"
os.makedirs(character_folder, exist_ok=True)

# Save each character's lines in a separate file
for character_name, lines in characters.items():
    character_file_path = os.path.join(character_folder, f"{character_name}.txt")
    with open(character_file_path, 'w') as character_file:
        character_file.writelines(lines)

print("Character files saved in 'Formatted/Characters/' folder.")
