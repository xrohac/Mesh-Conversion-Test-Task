import trimesh


def convert_obj_to_stl(input_obj_path: str, output_stl_path: str) -> None:

    mesh = trimesh.load(input_obj_path)

    mesh.export(output_stl_path)
    print(f"Successfully converted {input_obj_path} to {output_stl_path}")
