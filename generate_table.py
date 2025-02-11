import os
import subprocess

def get_submodules(directory):
    """Retrieve submodule names and their latest commit dates in the given directory."""
    subdirectories = []

    # Iterate over all items in the directory
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)

        # Check if it is a directory and a Git repository
        if os.path.isdir(full_path) and os.path.exists(os.path.join(full_path, ".git")):
            try:
                # Get the latest commit date of the repository
                commit_date = subprocess.run(
                    ["git", "-C", full_path, "log", "-1", "--format=%cd", "--date=format:%Y-%m-%d"],
                    capture_output=True, text=True
                ).stdout.strip()

                subdirectories.append((item, commit_date if commit_date else "N/A"))
            
            except subprocess.CalledProcessError as e:
                print(f"Error retrieving latest commit for {full_path}: {e}")
                subdirectories.append((item, "Error"))

    return subdirectories

def generate_markdown(submodule_data):
    """Generate a Markdown table from collected submodule data."""
    md_table = "| Type | Bootlaoder | Latest Commit Date |\n"
    md_table += "|------|-----------|---------------------|\n"

    for directory, submodules in submodule_data.items():
        if submodules:
            for submodule, date in submodules:
                md_table += f"| {directory} | {submodule} | {date} |\n"
            md_table += "| | | |\n"
    return md_table

if __name__ == "__main__":
    directories = ["type1", "type2", "type3"]  # Change these to the actual directory names
    submodule_data = {dir_name: get_submodules(dir_name) for dir_name in directories}

    markdown_output = generate_markdown(submodule_data)
    
    with open("table.md", "w") as f:
        f.write(markdown_output)