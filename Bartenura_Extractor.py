import os
import shutil

# Paths - 'os.path.expanduser' finds your Desktop automatically
desktop = os.path.expanduser("~/Desktop")
source_root = os.path.join(desktop, "Bartenura")
destination_folder = os.path.join(desktop, "Bartenura_Final")

# Create the final folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

print("Starting extraction...")

# Walk through all folders
for root, dirs, files in os.walk(source_root):
    for file in files:
        if file == "On Your Way.txt":
            # The 'root' looks like: .../Bartenura/Seder Zeriam/Bartenura on Mishnah Berakhot/Hebrew
            # We want to grab the "Bartenura on Mishnah Berakhot" part
            folder_parts = root.split(os.sep)
            
            # Find the part of the path that mentions the Masechet name
            masechet_folder = next((p for p in folder_parts if "Bartenura on Mishnah" in p), None)
            
            if masechet_folder:
                # Clean name: "Bartenura on Mishnah Berakhot" -> "Berakhot"
                masechet_name = masechet_folder.replace("Bartenura on Mishnah ", "").strip()
                
                # Construct new filename: Bartenura_Berakhot.txt
                new_filename = f"Bartenura_{masechet_name}.txt"
                source_path = os.path.join(root, file)
                dest_path = os.path.join(destination_folder, new_filename)
                
                # Copy and rename
                shutil.copy2(source_path, dest_path)
                print(f"✅ Extracted: {new_filename}")

print(f"\nDone! All files are now in the 'Bartenura_Final' folder on your desktop.")
