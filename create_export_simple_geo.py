from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.StlAPI import StlAPI_Writer

 
# Create a simple box using the primitives API
box_shape = BRepPrimAPI_MakeBox(50,50,50).Shape()
 
# Export to STL
stl_writer = StlAPI_Writer()
stl_writer.SetASCIIMode(True)
stl_writer.Write(box_shape,'C:\test\box2.stl')

