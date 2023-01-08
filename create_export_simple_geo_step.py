from __future__ import print_function

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox

from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static_SetCVal
from OCC.Core.IFSelect import IFSelect_RetDone

from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax3

from OCC.Display.SimpleGui import init_display

def axis():
    p1 = gp_Pnt(2.0, 3.0, 4.0)
    d = gp_Dir(4.0, 5.0, 6.0)
    a = gp_Ax3(p1, d)
    a_IsDirect = a.Direct()
    print("a is direct:", a_IsDirect)
    # a_XDirection = a.XDirection()
    # a_YDirection = a.YDirection()
    p2 = gp_Pnt(5.0, 3.0, 4.0)
    a2 = gp_Ax3(p2, d)
    a2.YReverse()
    # axis3 is now left handed
    a2_IsDirect = a2.Direct()
    print("a2 is direct:", a2_IsDirect)
    # a2_XDirection = a2.XDirection()
    # a2_YDirection = a2.YDirection()
    
    #display.DisplayShape(p1, update=True)
    #display.DisplayShape(p2, update=True)
    #display.DisplayMessage(p1, "P1")
    #display.DisplayMessage(p2, "P2")
    return a

# creates a basic shape
box_s = BRepPrimAPI_MakeBox(10, 20, 30).Shape()
b = axis()

# initialize the STEP exporter
step_writer = STEPControl_Writer()
dd = step_writer.WS().TransferWriter().FinderProcess()
print(dd)

Interface_Static_SetCVal("write.step.schema", "AP203")

# transfer shapes and write file
step_writer.Transfer(box_s, STEPControl_AsIs)
# step_writer.Transfer(b, STEPControl_AsIs)
status = step_writer.Write("box2.stp")

if status != IFSelect_RetDone:
    raise AssertionError("load failed")