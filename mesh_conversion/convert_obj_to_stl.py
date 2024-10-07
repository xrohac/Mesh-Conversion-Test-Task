import trimesh


def convert_obj_to_stl(input_obj_path: str, output_stl_path: str) -> None:
    # Load the .obj file using trimesh
    mesh = trimesh.load(input_obj_path)

    # Export the mesh to .stl format
    mesh.export(output_stl_path)
    print(f"Successfully converted {input_obj_path} to {output_stl_path}")
