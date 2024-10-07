import argparse
from mesh_conversion import convert_obj_to_stl, visualize_stl


def main():
    parser = argparse.ArgumentParser(description="Mesh Conversion and Visualization Tool")

    # commands for conversion and visualization
    subparsers = parser.add_subparsers(dest="command")

    # command: convert
    convert_parser = subparsers.add_parser("convert", help="Convert .obj to .stl")
    convert_parser.add_argument("input_obj", help="Path to the input .obj file")
    convert_parser.add_argument("output_stl", help="Path to the output .stl file")

    # command: visualize
    visualize_parser = subparsers.add_parser("visualize", help="Visualize an .stl file")
    visualize_parser.add_argument("input_stl", help="Path to the input .stl file")
    visualize_parser.add_argument("--color", nargs=3, type=float, default=(0.9, 0.6, 0.4),
                                  help="RGB color values for the mesh")

    args = parser.parse_args()

    if args.command == "convert":
        convert_obj_to_stl(args.input_obj, args.output_stl)
    elif args.command == "visualize":
        visualize_stl(args.input_stl, tuple(args.color))


if __name__ == "__main__":
    main()
