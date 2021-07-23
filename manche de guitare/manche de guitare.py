#Author-moiememe
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
import math
from tkinter import *

f1 = 0
ccc = 0
manche = 0
frette = 0
diapt = 0
alpha = 0


def run():
    global f1
    global ccc
    global manche
    global frette
    global diapt
    global alpha

    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        root = design.rootComponent

        sketches = root.sketches

        base = sketches.add(root.xYConstructionPlane)

        base.name = "manche avec frette"

        sketchLines = base.sketchCurves.sketchLines



        diap = float(diapason.get())/10
        frette = int(frettes.get())
        f1 = float(frette1.get())/10
        f12 = float(frette12.get())/10

        diapb = diap
        diapt = diap
        somme = 0
        for i in range (0,(frette+1), 1):
            ldiap = diap / 17.817
            somme += (ldiap)
            somme = round(somme, 4)

            diap = diap - ldiap


        manche = somme +1



        cc = (f12-f1)/2

        alpha = math.atan(cc/(diapb/2))

        ccc = math.tan(alpha)*manche

        d = 2*(ccc)+f1

        no = math.sqrt(manche*manche + ccc*ccc)

        beta = alpha*180/math.pi

        bases(sketchLines)
        extbase(base, root)

        esqfrette()

        cordeesq()
        sillet()

        diapasonesq()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


def bases(sketchLines):
    global f1
    global ccc
    global manche


    hg = adsk.core.Point3D.create(0,-0.8,0)
    hd = adsk.core.Point3D.create(f1,-0.8,0)
    bg = adsk.core.Point3D.create(-ccc,manche, 0)
    bd = adsk.core.Point3D.create(f1 + ccc, manche, 0)

    #lines = base.sketchCurves.sketchLines

    no = sketchLines.addByTwoPoints(hd, bd)
    op = sketchLines.addByTwoPoints(bd, bg)
    pm = sketchLines.addByTwoPoints(bg, hg)
    mn = sketchLines.addByTwoPoints(hg, hd)

def extbase(base, root):
    extrude = root.features.extrudeFeatures
    diapa = base.sketchCurves.sketchLines.count
        
    prof = base.profiles.item(0)

    dist = adsk.core.ValueInput.createByReal(0.7)

    newbody = extrude.addSimple(prof, dist, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)


def esqfrette():


    global frette
    global diapt
    

    diap = diapt
    somme = 0
    s = 0
    for i in range (frette+1):
            ldiap = diap / 17.817
            somme += (ldiap)
            sommes = round(somme, 4)

            diap = diap - ldiap   

            app = adsk.core.Application.get()
            ui  = app.userInterface
            product = app.activeProduct
            design = adsk.fusion.Design.cast(product)

            root = design.rootComponent

            sketches = root.sketches

            basess = sketches.add(root.xYConstructionPlane)

            s = str(i)

            k = "%s%s" % ("frette", s)


            basess.name = k

            sketchLines = basess.sketchCurves.sketchLines   

            a = adsk.core.Point3D.create(-ccc, (sommes-0.029), 0.7)
            b = adsk.core.Point3D.create((f1+ccc), (sommes-0.029), 0.7)
            c = adsk.core.Point3D.create((f1+ccc), (sommes+0.029), 0.7)
            d = adsk.core.Point3D.create(-ccc, (sommes+0.029), 0.7)

            ab = sketchLines.addByTwoPoints(a, b)
            bc = sketchLines.addByTwoPoints(b, c)
            cd = sketchLines.addByTwoPoints(c, d)
            da = sketchLines.addByTwoPoints(d, a)

            extrude = root.features.extrudeFeatures
            diapa = basess.sketchCurves.sketchLines.count

            
                
            prof = basess.profiles.item(0)

            dist = adsk.core.ValueInput.createByReal(-0.2)

            newbody = extrude.addSimple(prof, dist, adsk.fusion.FeatureOperations.CutFeatureOperation)

            

            


def diapasonesq():
    global f1
    global ccc
    global diapt


    app = adsk.core.Application.get()
    ui  = app.userInterface
    product = app.activeProduct
    design = adsk.fusion.Design.cast(product)

    root = design.rootComponent

    sketches = root.sketches

    base = sketches.add(root.xYConstructionPlane)

    base.name = "diapason"

    sketchLines = base.sketchCurves.sketchLines 

    a = adsk.core.Point3D.create(f1/2, 0, 0)
    b = adsk.core.Point3D.create(f1/2, diapt, 0)

    ab = sketchLines.addByTwoPoints(a, b)


def cordeesq():
    global f1
    global diapt
    global alpha

    hauteur= float(haut.get())/10 +0.7

    diap = float(diapason.get())/10
    frette = int(frettes.get())
    f1 = float(frette1.get())/10
    f12 = float(frette12.get())/10

    cor = int(corde.get()) 

    cn = math.tan(alpha)*diap

    lt = cn*2+f1

    esph = (f1 / (cor) ) / 2

    espb = (lt / (cor) ) / 2

    for i in range (0, cor , 1):
        app = adsk.core.Application.get()
        ui  = app.userInterface
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        root = design.rootComponent

        sketches = root.sketches

        base = sketches.add(root.xYConstructionPlane)

        s = str(i)

        k = "%s%s" % ("corde", s)


        base.name = k

        sketchLines = base.sketchCurves.sketchLines 



        a = adsk.core.Point3D.create((i*2+1)*esph, 0, hauteur)
        b = adsk.core.Point3D.create((i*2+1)*espb-cn, diap, hauteur)

        ab = sketchLines.addByTwoPoints(a, b)

def sillet():
    profo = float(psillet.get())/10
    larg = float(lsillet.get())/10


    app = adsk.core.Application.get()
    ui  = app.userInterface
    product = app.activeProduct
    design = adsk.fusion.Design.cast(product)

    root = design.rootComponent

    sketches = root.sketches

    base = sketches.add(root.xYConstructionPlane)

    base.name = "sillet"

    sketchLines = base.sketchCurves.sketchLines 

    a = adsk.core.Point3D.create(-1, -larg, 0.7)
    b = adsk.core.Point3D.create(-1, 0, 0.7)
    c = adsk.core.Point3D.create(10, 0, 0.7)
    d = adsk.core.Point3D.create(10, -larg, 0.7)

    ab = sketchLines.addByTwoPoints(a, b)
    bc = sketchLines.addByTwoPoints(b, c)
    cd = sketchLines.addByTwoPoints(c, d)
    da = sketchLines.addByTwoPoints(d, a)


    extrude = root.features.extrudeFeatures
    diapa = base.sketchCurves.sketchLines.count

    
        
    prof = base.profiles.item(0)

    dist = adsk.core.ValueInput.createByReal(-profo)

    newbody = extrude.addSimple(prof, dist, adsk.fusion.FeatureOperations.CutFeatureOperation)






win = Tk()

win.title("La tirelire magique ")
win.geometry("360x750")
win.config(background='#00ffe0')

label = Label(win, text='taille du diapason', font=('Courrier', 27), bg='#00ffe0')
label.pack(side=TOP)

diapason = Entry(win, width=45)
diapason.pack(expand=YES)

label1 = Label(win, text='nombre de frette', font=('Courrier', 27), bg='#00ffe0')
label1.pack(side=TOP)

frettes = Entry(win, width=45)
frettes.pack(expand=YES)

label2 = Label(win, text='taille de la frette 1', font=('Courrier', 27), bg='#00ffe0')
label2.pack(side=TOP)

frette1 = Entry(win, width=45)
frette1.pack(expand=YES)

label3 = Label(win, text='taille de la frette 12', font=('Courrier', 27), bg='#00ffe0')
label3.pack(side=TOP)

frette12 = Entry(win, width=45)
frette12.pack(expand=YES)

label4 = Label(win, text='nombre de cordes', font=('Courrier', 27), bg='#00ffe0')
label4.pack(side=TOP)

corde = Entry(win, width=45)
corde.pack(expand=YES)

label5 = Label(win, text='hauteur des cordes ', font=('Courrier', 27), bg='#00ffe0')
label5.pack(side=TOP)

haut = Entry(win, width=45)
haut.pack(expand=YES)

label6 = Label(win, text='profondeur sillet ', font=('Courrier', 27), bg='#00ffe0')
label6.pack(side=TOP)

psillet = Entry(win, width=45)
psillet.pack(expand=YES)

label7 = Label(win, text='largeur sillet ', font=('Courrier', 27), bg='#00ffe0')
label7.pack(side=TOP)

lsillet = Entry(win, width=45)
lsillet.pack(expand=YES)



but = Button(win, text='créer mon manche',
  font=('Courrier', 20), bg='#00ffe0', command=run)
but.pack(expand=YES)

win.mainloop()