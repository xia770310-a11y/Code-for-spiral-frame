"""This file acts as the main module for this script."""

import traceback
import adsk.core,  adsk.core, adsk.fusion, adsk.cam, traceback, math
import adsk.fusion
# import adsk.cam

# Initialize the global variables for the Application and UserInterface objects.
app = adsk.core.Application.get()
ui  = app.userInterface


def run(_context: str):
    """This function is called by Fusion when the script is run."""
    try:
        # Your code goes here.
        ui.messageBox(f'"{app.activeDocument.name}" is the active Document.')

        def archimedeanSpiral():
            ui = None
            try:
                app = adsk.core.Application.get()
                ui  = app.userInterface
        
                des = adsk.fusion.Design.cast(app.activeProduct)
                root = des.rootComponent
        
            # Create a new sketch.
                sk = root.sketches.add(root.xYConstructionPlane)

        # Create a series of points along the spiral using the spiral equation.
        # r = a + (beta * theta)
                pnts = adsk.core.ObjectCollection.create()
                numTurns =13
                pointsPerTurn = 30
                distanceBetweenTurns = 0.145  # beta
                theta = 0
                offset = 0                # a
                for i in range(pointsPerTurn * numTurns + 1):
                    r = offset + (distanceBetweenTurns * theta) 
                    x = r * math.cos(theta)
                    y = r * math.sin(theta)
                    pnts.add(adsk.core.Point3D.create(x,y,0))
            
                    theta += (math.pi*2) / pointsPerTurn

                sk.sketchCurves.sketchFittedSplines.add(pnts)        
            except:
                if ui:
                    ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
    except:  #pylint:disable=bare-except
        # Write the error message to the TEXT COMMANDS window.
        app.log(f'Failed:\n{traceback.format_exc()}')
    archimedeanSpiral()
