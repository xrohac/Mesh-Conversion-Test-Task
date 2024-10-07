import vtk


def visualize_stl(stl_file_path: str, color: tuple = (0.6, 0.4, 1)) -> None:
    # Create a reader for the STL file
    reader = vtk.vtkSTLReader()
    reader.SetFileName(stl_file_path)

    # Create a mapper for the data
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    # Create an actor for the object
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(list(color))  # Set object color

    # Create a renderer and add the actor to it
    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(1, 1, 1)  # Set background color

    # Create a render window
    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)
    render_window.SetWindowName("STL Visualization with VTK")

    # Create an interactor
    render_window_interactor = vtk.vtkRenderWindowInteractor()
    render_window_interactor.SetRenderWindow(render_window)

    # Initialize the interactor and start the visualization
    render_window.Render()
    render_window_interactor.Start()
