from __future__ import print_function

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox

from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static_SetCVal
from OCC.Core.IFSelect import IFSelect_RetDone

# creates a basic shape
box_s = BRepPrimAPI_MakeBox(10, 20, 30).Shape()

# initialize the STEP exporter
step_writer = STEPControl_Writer()
dd = step_writer.WS().TransferWriter().FinderProcess()
print(dd)

Interface_Static_SetCVal("write.step.schema", "AP203")

# transfer shapes and write file
step_writer.Transfer(box_s, STEPControl_AsIs)
status = step_writer.Write("box2.stp")

if status != IFSelect_RetDone:
    raise AssertionError("load failed")