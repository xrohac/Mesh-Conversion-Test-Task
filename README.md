"# Mesh-Conversion-Test-Task" 

# Clone the Repository
git clone https://github.com/xrohac/Mesh-Conversion-Test-Task.git

# Install dependencies
pip install -r requirements.txt

# Convert the .obj file to .stl format using cli
python cli.py convert <path_to_input_obj> <path_to_output_stl>

# Visualization of the .stl file with or without a specific color (RGB values)
python cli.py visualize <path_to_stl_file> --color <r> <g> <b> 
