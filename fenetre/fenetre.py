#Author-
#Description-faire des fenetre\n

import adsk.core, adsk.fusion, adsk.cam, traceback
from tkinter import *

def run():
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        

        cadre()
        encardement()

        trou()




    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def trou():
    long = float(longueur.get())/10
    lar = float(largeur.get())/10
    


    app = adsk.core.Application.get()
    ui  = app.userInterface
    product = app.activeProduct
    design = adsk.fusion.Design.cast(product)

    root = design.rootComponent

    sketches = root.sketches

    base = sketches.add(root.xYConstructionPlane)

    base.name = "trou"

    sketchLines = base.sketchCurves.sketchLines 

    a = adsk.core.Point3D.create(long/2-.15, lar/2-0.15, 3)
    b = adsk.core.Point3D.create(0, 0, 3)

    ab = sketchLines.addCenterPointRectangle(b, a)

    extrude = root.features.extrudeFeatures
    diapa = base.sketchCurves.sketchLines.count

    
        
    prof = base.profiles.item(0)

    dist = adsk.core.ValueInput.createByReal(-10)

    newbody = extrude.addSimple(prof, dist, adsk.fusion.FeatureOperations.CutFeatureOperation)
    



def encardement():


    long = float(longueur.get())/10
    lar = float(largeur.get())/10
    bo = float(bord.get())/10


    app = adsk.core.Application.get()
    ui  = app.userInterface
    product = app.activeProduct
    design = adsk.fusion.Design.cast(product)

    root = design.rootComponent

    sketches = root.sketches

    base = sketches.add(root.xYConstructionPlane)

    base.name = "encadrement"

    sketchLines = base.sketchCurves.sketchLines 

    a = adsk.core.Point3D.create(long/2, lar/2, 1)
    b = adsk.core.Point3D.create(0, 0, 1)

    ab = sketchLines.addCenterPointRectangle(b, a)

    extrude = root.features.extrudeFeatures
    diapa = base.sketchCurves.sketchLines.count

    
        
    prof = base.profiles.item(0)

    dist = adsk.core.ValueInput.createByReal(bo)

    newbody = extrude.addSimple(prof, dist, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)


def cadre():
    long = float(longueur.get())/10
    lar = float(largeur.get())/10


    app = adsk.core.Application.get()
    ui  = app.userInterface
    product = app.activeProduct
    design = adsk.fusion.Design.cast(product)

    root = design.rootComponent

    sketches = root.sketches

    base = sketches.add(root.xYConstructionPlane)

    base.name = "cadre"

    sketchLines = base.sketchCurves.sketchLines 

    a = adsk.core.Point3D.create(long/2+0.15, lar/2+0.15, 0)
    b = adsk.core.Point3D.create(0, 0, 0)

    ab = sketchLines.addCenterPointRectangle(b, a)

    extrude = root.features.extrudeFeatures
    diapa = base.sketchCurves.sketchLines.count

    
        
    prof = base.profiles.item(0)

    dist = adsk.core.ValueInput.createByReal(0.05)

    newbody = extrude.addSimple(prof, dist, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)


win = Tk()

win.title("La tirelire magique ")
win.geometry("660x550")
win.config(background='#00ffe0')


label1 = Label(win, text='epaisseur du rebord(le gros)', font=('Courrier', 27), bg='#00ffe0')
label1.pack(side=TOP)

bord = Entry(win, width=45)
bord.pack(expand=YES)




label3 = Label(win, text='longueur', font=('Courrier', 27), bg='#00ffe0')
label3.pack(side=TOP)

largeur = Entry(win, width=45)
largeur.pack(expand=YES)

label4 = Label(win, text='largeur', font=('Courrier', 27), bg='#00ffe0')
label4.pack(side=TOP)

longueur = Entry(win, width=45)
longueur.pack(expand=YES)

but = Button(win, text='créer mon manche',
  font=('Courrier', 20), bg='#00ffe0', command=run)
but.pack(expand=YES)

win.mainloop()