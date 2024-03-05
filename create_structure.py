import os

# Define the directory structure
dir_structure = {
    'app': {
        'static': {},
        'templates': {},
    },
    'data': {
        'raw': {},
        'processed': {},
        'external': {},
    },
    'models': {},
    'notebooks': {},
    'src': {
        'data': {},
        'features': {},
        'models': {},
        'visualization': {},
        'utils.py': None,
        'logger.py': None,  # logger.py added here
        'exception.py': None,  # exception.py added here
    },
    'tests': {
        'unit': {},
        'integration': {},
    },
}

# Function to create directories and files
def create_dir_structure(base_path, structure):
    for name, sub_structure in structure.items():
        if name.endswith('.py'):  # It's a file
            open(os.path.join(base_path, name), 'a').close()
        else:  # It's a directory
            dir_path = os.path.join(base_path, name)
            os.makedirs(dir_path, exist_ok=True)
            if isinstance(sub_structure, dict):
                create_dir_structure(dir_path, sub_structure)  # Recursively create subdirectories

# Create the project structure
create_dir_structure('.', dir_structure)

# Create additional files
additional_files = [
    'requirements.txt',
    'setup.py',
    'README.md',
]

for file_name in additional_files:
    open(file_name, 'a').close()

print("Project structure created successfully.")
