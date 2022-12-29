import streamlit as st
import math
from math import acos, degrees

st.set_page_config (layout="centered")
st.title ("Welcome to Shapes, Squares, Square roots, Cubes, Cube roots calculator",)
st.header ("Calculate every singe value on just one click")

typecal = st.radio ("Select the type you want to calculate", ("Shapes", "Squares, Square roots, Cubes, Cube roots"))
if typecal == ("Squares, Square roots, Cubes, Cube roots"):
    typesq = st.radio ("Select what you want to calculate", ("Squares", "Square roots", "Cubes", "Cube roots"))
    
    if typesq == ("Squares"):
        squarenuber = st.number_input ("Please enter the number whose square you want to find: ")
        square = squarenuber ** 2
    elif typesq == ("Square roots"):
        squarerootnumber = st.number_input ("Please enter the number whose square root you want to find: ")
        squareroot = squarerootnumber ** 0.5
    elif typesq == ("Cubes"):
        cubenumber = st.number_input ("Please enter the number whose cube you want to find: ")
        cube = cubenumber ** 3
    elif typesq == ("Cube roots"):
        cuberootnumber = st.number_input ("Please enter the number whose cube root you wnat to find: ")
        cuberoot = cuberootnumber ** (1/3)
        
    if (st.button("Calculate values")):
        if typesq == ("Squares"):
            st.write ("Square of", squarenuber, "=", square)
        elif typesq == ("Square roots"):
            st.write ("Square root of", squarerootnumber, "=", squareroot)
        elif typesq == ("Cubes"):
            st.write ("Cube of", cubenumber, "=", cube)
        elif typesq == ("Cube roots"):
            st.write ("Cube root of", cuberootnumber, "=", cuberoot)






elif typecal == ("Shapes"):
    shape = st.radio ("Select Your Shape:", ("Square", "Rectangle", "Cube", "Cuboid", "Circle", "Sphere", "Cylinder", "Trapezium", "General Quadrilateral", "Triangle"))
    value = st.radio ("Choose the unit", ("Millimeters", "Centimeters", "Inch" ,"Meters" ,"Kilometers"))


    if shape == ("Square"):
        lengthofsquare = st.number_input ("Please enter the length of your Square: ")
        try:
            areaofsquare = lengthofsquare ** 2
            perimeterofsquare = lengthofsquare * 4

        except:
            st.text ("Enter a value")
            
    
    elif shape == ("Rectangle"):
        lengthofrectangle = st.number_input("Please enter the length of your Rectangle: ")
        breadthofrectangle = st.number_input("Please enter the breadth of your Rectangle: ")
        try:
            areaofrectangle = lengthofrectangle * breadthofrectangle
            perimeterofrectangle = 2 * (lengthofrectangle + breadthofrectangle)
        
        except:
            st.text ("Enter a value")
            
    
    elif shape ==("Cube"):
        lengthofcube = st.number_input("Please enter the length of your Cube: ")
        try:
            volumeofcube = lengthofcube ** 3
            surfaceareaofcube = 6 * lengthofcube ** 2
            lateralsurfaceareaofcube = 4 * (lengthofcube * lengthofcube)
            surfaceareaofonesideofcube = lengthofcube ** 2
            perimeterofonesideofcube = 4 * lengthofcube
            if value == ("Inch"):
                valueofcubeinliters = volumeofcube * 0.016387064
            elif value == ("Centimeters"):
                valueofcubeinliters = volumeofcube * 0.001
            elif value == ("Millimeters"):
                valueofcubeinliters = volumeofcube * 0.000001
            elif value == ("Meters"):
                valueofcubeinliters = volumeofcube * 1000
            elif value == ("Kilometers"):
                valueofcubeinliters = volumeofcube * 1000000000000
        
        except:
            st.text ("Enter a value")
            
    
    elif shape ==("Cuboid"):
        lengthofcuboid = st.number_input("Please enter the length of your Cuboid: ")
        breadthofcuboid = st.number_input("Please enter the breadth of your Cuboid: ")
        heightofcuboid = st.number_input("Please enter the height of your cuboid: ")
        try:
            volumeofcuboid = lengthofcuboid * breadthofcuboid * heightofcuboid
            surfaceareaofcuboid = 2 * ((lengthofcuboid * breadthofcuboid) + (breadthofcuboid * heightofcuboid) + (heightofcuboid * lengthofcuboid))
            lateralsurfaceareaofcuboid = (2 * heightofcuboid) * (lengthofcuboid + breadthofcuboid)
            surfaceareaofonesideofcuboid = lengthofcuboid * breadthofcuboid
            perimeterofonesideofcuboid = 2 * (lengthofcuboid + breadthofcuboid)
            if value == ("Inch"):
                valueofcuboidinliters = volumeofcuboid * 0.016387064
            elif value == ("Centimeters"):
                valueofcuboidinliters = volumeofcuboid * 0.001
            elif value == ("Millimeters"):
                valueofcuboidinliters = volumeofcuboid * 0.000001
            elif value == ("Meters"):
                valueofcuboidinliters = volumeofcuboid * 1000
            elif value == ("Kilometers"):
                valueofcuboidinliters = volumeofcuboid * 1000000000000

        
        except:
            st.text ("Enter a value")
            
        
    elif shape ==("Circle"):
        radiusofcircle = st.number_input("Please enter the radius of your circle: ")
        try:
            areaofcircle = 22/7 * radiusofcircle ** 2
            circumferenceofcircle = 2 * 22/7 * radiusofcircle
        
        except:
            st.text ("Enter a value")
            
    
    elif shape ==("Sphere"):
        radiusofsphere = st.number_input("Please enter the radius of shpere: ")
        try:
            surfaceareaofsphere = 4 * 22/7 * radiusofsphere ** 2
            volumeofsphere = (4 % 3) * 22/7 * radiusofsphere ** 3
            if value == ("Inch"):
                valueofsphereinliters = volumeofsphere * 0.016387064
            elif value == ("Centimeters"):
                valueofsphereinliters = volumeofsphere * 0.001
            elif value == ("Millimeters"):
                valueofsphereinliters = volumeofsphere * 0.000001
            elif value == ("Meters"):
                valueofsphereinliters = volumeofsphere * 1000
            elif value == ("Kilometers"):
                valueofsphereinliters = volumeofsphere * 1000000000000
        
        except:
            st.text ("Enter a value")
            
    
    elif shape ==("Cylinder"):
        radiusofcylinder = st.number_input("Please enter the radius of cylinder: ")
        heightofcylinder = st.number_input("Please enter the height of cylinder: ")
        try:
            surfaceareaofcylinder = 2 * 22/7 * radiusofcylinder * (radiusofcylinder + heightofcylinder)
            curvedsurfaceareaofcylinder = 2 * 22/7 * radiusofcylinder * heightofcylinder
            volumeofcylinder = 22/7 * radiusofcylinder ** 2 * heightofcylinder
            if value == ("Inch"):
                valueofcylinderinliters = volumeofcylinder * 0.016387064
            elif value == ("Centimeters"):
                valueofcylinderinliters = volumeofcylinder * 0.001
            elif value == ("Millimeters"):
                valueofcylinderinliters = volumeofcylinder * 0.000001
            elif value == ("Meters"):
                valueofcylinderinliters = volumeofcylinder * 1000
            elif value == ("Kilometers"):
                valueofcylinderinliters = volumeofcylinder * 1000000000000
        
        except:
            st.text ("Enter a value")
            
            
    elif shape ==("Trapezium"):
        lengthofsideaoftrapezium = st.number_input("Please enter the length of first side of your trapezium: ")
        lengthofsidebofreapezium = st.number_input("Please enter the length of second side of your trapezium: ")
        heightoftrapezium = st.number_input("Please enter the height of your trapezium")
        try:
            areaoftrapezium = heightoftrapezium * (lengthofsideaoftrapezium + lengthofsidebofreapezium) * 1/2
        
        except:
            st.text ("Enter a value")
            
    elif shape ==("General Quadrilateral"):
        height1ofgeneralquadrilateral = st.number_input("Please enter the length of first height: ")
        height2ofgeneralquadrilateral = st.number_input("Please enter the length of second height: ")
        diagonalofgeneralquadrilateral = st.number_input("Please enter the length of diagonal: ")
        try:
            areaofgeneralquadrilateral = 1/2 * diagonalofgeneralquadrilateral * (height1ofgeneralquadrilateral + height2ofgeneralquadrilateral)
        
        except:
            st.text ("Enter a value")
    
    elif shape == ("Triangles"):
        typetriangle = st.radio ("Select the type of triangle", ("Right angled Triangle", "Equilateral Triangle (every side equal)", "Isosceles Triangle (2 sides equal)", "Scalene Tringle (no equal sides)"))
        
        if typetriangle == ("Right angled Triangle"):
            try:
                heightofrightangletriangle = st.number_input ("Please enter the height of Right Angle Triange")
                baseofrightangletriangle = st.number_input ("Please enter the base of Right Angle Triangle")
                areaofrightangletriangle = 1/2 * baseofrightangletriangle * heightofrightangletriangle
                hypotenuseofrightangletriangle = (heightofrightangletriangle ** 2 + baseofrightangletriangle ** 2) ** 0.5 
                perimeterofrightangleoftriangle = heightofrightangletriangle + baseofrightangletriangle + hypotenuseofrightangletriangle
                angle1rightangledtriangle = degrees(acos((heightofrightangletriangle * heightofrightangletriangle + baseofrightangletriangle * baseofrightangletriangle - hypotenuseofrightangletriangle * hypotenuseofrightangletriangle) / (2 * heightofrightangletriangle * baseofrightangletriangle)))
                angle2rightangledtriangle = degrees(acos((baseofrightangletriangle * baseofrightangletriangle + hypotenuseofrightangletriangle * hypotenuseofrightangletriangle - heightofrightangletriangle * heightofrightangletriangle) / (2 * baseofrightangletriangle * hypotenuseofrightangletriangle)))
                angle3rightangletriangle = 180 - (angle1rightangledtriangle + angle2rightangledtriangle)
                
            except:
                print ("Enter a value")
                
        
        elif typetriangle == ("Equilateral Triangle (every side equal)"):
            
            try:
                asideofequilateraltriangle = st.number_input ("Please enter the length of your triangle")
                perimeterofequilateraltriangle = asideofequilateraltriangle * 3
                equi = 1/2 * (asideofequilateraltriangle + asideofequilateraltriangle + asideofequilateraltriangle)
                areaofequilateraltriangle = (equi*(equi - asideofequilateraltriangle)*(equi - asideofequilateraltriangle)*(equi - asideofequilateraltriangle)) ** 0.5 
                angle1ofequilateraltriangle = 180 / 3
                angle2ofequilateraltriangle = 180 / 3
                angle3ofequilateraltriangle = 180 / 3
                heightofequilateraltriangle = (areaofequilateraltriangle * 2) / asideofequilateraltriangle
                
            except:
                print ("Enter a value")
                
        
        elif typetriangle == ("Isosceles Triangle (2 sides equal)"):

            try:
                asideofisocelesestriangle = st.number_input ("Please enter length a of your triangle")
                bsideofisocelesestriangle = st.number_input ("Please enter length b of your triangle")
                csideofisocelesestriangle = st.number_input ("Please enter the length c of your triangle")
                perimeterofisocelesestriangle = asideofisocelesestriangle + bsideofisocelesestriangle + csideofisocelesestriangle
                isoc = 1/2 * (asideofisocelesestriangle + bsideofisocelesestriangle + csideofisocelesestriangle)
                areaofisocelesestriangle = (isoc*(isoc - asideofisocelesestriangle)*(isoc - bsideofisocelesestriangle)*(isoc - csideofisocelesestriangle)) ** 0.5
                angle1ofisocelesestriangle = degrees(acos((bsideofisocelesestriangle * bsideofisocelesestriangle + csideofisocelesestriangle * csideofisocelesestriangle - asideofisocelesestriangle * asideofisocelesestriangle) / (2 * bsideofisocelesestriangle * csideofisocelesestriangle)))
                angle2ofisocelesestriangle = degrees(acos((csideofisocelesestriangle * csideofisocelesestriangle + asideofisocelesestriangle * asideofisocelesestriangle - bsideofisocelesestriangle * bsideofisocelesestriangle) / (2 * csideofisocelesestriangle * asideofisocelesestriangle)))
                angle3ofisocelesestriangle = 180 - (angle1ofisocelesestriangle + angle2ofisocelesestriangle)
                heightofisocelesestriangle = (areaofisocelesestriangle * 2) / csideofisocelesestriangle
                
            except:
                print ("Enter a value")
        
        
        elif typetriangle == ("Scalene Tringle (no equal sides)"):
            try:
                asideofscalenetriangle = st.number_input ("Please enter length a of your triangle")
                bsideofscalenetriangle = st.number_input ("Please enter length b of your triangle")
                csideofscalenetriangle = st.number_input ("Please enter the length c of your triangle")
                perimeterofscalenetriangle = asideofscalenetriangle + bsideofscalenetriangle + csideofscalenetriangle
                scal = 1/2 * (asideofscalenetriangle + bsideofscalenetriangle + csideofscalenetriangle)
                areaofscalenetriangle = (scal*(scal - asideofscalenetriangle)*(scal - bsideofscalenetriangle)*(scal - csideofscalenetriangle)) ** 0.5
                angle1ofscalenetriangle = degrees(acos((bsideofscalenetriangle * bsideofscalenetriangle + csideofscalenetriangle * csideofscalenetriangle - asideofscalenetriangle * asideofscalenetriangle) / (2 * bsideofscalenetriangle * csideofscalenetriangle)))
                angle2ofscalenetriangle = degrees(acos((csideofscalenetriangle * csideofscalenetriangle + asideofscalenetriangle * asideofscalenetriangle - bsideofscalenetriangle * bsideofscalenetriangle) / (2 * csideofscalenetriangle * csideofscalenetriangle)))
                angle3ofscalenetriangle = 180 - (angle1ofscalenetriangle + angle2ofscalenetriangle)
                heightofscalenetriangle = (areaofscalenetriangle * 2) / csideofscalenetriangle
                
            except:
                print ("Enter a value")
    
    
    if (st.button("Calculate values")):
        if shape == ("Square"):
            st.write ("Area =", areaofsquare,value, "sq")
            st.write ("Perimeter =", perimeterofsquare, value) 
        
        elif shape == ("Rectangle"):
            st.write ("Area =", areaofrectangle, value, "sq")
            st.write ("Perimeter=", perimeterofrectangle, value)
        
        elif shape == ("Cube"):
            st.write ("Volume =", volumeofcube, value, "cube")
            st.write ("Volume in Liters =", valueofcubeinliters, "Liter/s")
            st.write ("Surface Area =", surfaceareaofcube, value, "sq")
            st.write ("Lateral Surface Area =", lateralsurfaceareaofcube, value, "sq")
            st.write ("Area of one side =", surfaceareaofonesideofcube, value, "sq")
            st.write ("Perimeter of one side =", perimeterofonesideofcube, value)
            
        elif shape == ("Cuboid"):
            st.write ("Volume =", volumeofcuboid, value, "cube")
            st.write ("Volume in Liters =",valueofcuboidinliters, "Liter/s")
            st.write ("Surface area =", surfaceareaofcuboid, value, "sq")
            st.write ("Lateral surface area =", lateralsurfaceareaofcuboid, value, "sq")
            st.write ("Area of one side =", surfaceareaofonesideofcuboid, value, "sq")
            st.write ("Perimeter of one side =", perimeterofonesideofcuboid, value)
        
        elif shape == ("Circle"):
            st.write ("Perimeter =", circumferenceofcircle, value)
            st.write ("Area =", areaofcircle, value, "sq")
        
        elif shape == ("Sphere"):
            st.write ("Volume =", volumeofsphere, value, "cube")
            st.write ("Volume in Liters =", valueofsphereinliters, "Liter/s")
            st.write ("Surface area =", surfaceareaofsphere, value, "sq")
            
        elif shape == ("Cylinder"):
            st.write ("Volume =", volumeofcylinder, value, "cube")
            st.write ("Volume in Liters =", valueofcylinderinliters, "Liter/s" )
            st.write ("Surface area =", surfaceareaofcylinder, value, "sq")
            st.write ("Lateral surface area =", curvedsurfaceareaofcylinder, value, "sq")
            
        elif shape == ("Trapezium"):
            st.write ("Area =", areaoftrapezium, value, "sq")
        
        elif shape == ("General Quadrilateral"):
            st.write ("Area =", areaofgeneralquadrilateral, value, "sq")
        
        elif shape == ("Triangle"):
            if typetriangle == ("Right angled Triangle"):
                st.write ("Area =", areaofrightangletriangle, value, "sq")
                st.write ("Perimeter =", perimeterofrightangleoftriangle, value)
                st.write ("Hypotenuse =", hypotenuseofrightangletriangle, value)
                st.write ("Angle 1 =", angle1rightangledtriangle,"°" )
                st.write ("Angle 2 =", angle2rightangledtriangle, "°")
                st.write ("Angle 3 =", angle3rightangletriangle, "°")
                
            elif typetriangle == ("Equilateral Triangle (every side equal)"):
                st.write ("Area =", areaofequilateraltriangle, value, "sq")
                st.write ("Perimeter =", perimeterofequilateraltriangle, value)
                st.write ("Angle 1 =", angle1ofequilateraltriangle, "°")
                st.write ("Angle 2 =", angle2ofequilateraltriangle, "°")
                st.write ("Angle 3 =", angle3ofequilateraltriangle, "°")
                st.write ("Height =", heightofequilateraltriangle, value)
                
            elif typetriangle == ("Isosceles Triangle (2 sides equal)"):
                st.write ("Area =", areaofisocelesestriangle, value, "sq")
                st.write ("Perimeter =", perimeterofisocelesestriangle, value)
                st.write ("Angle 1 =", angle1ofisocelesestriangle, "°")
                st.write ("Angle 2 =", angle2ofisocelesestriangle, "°")
                st.write ("Angle 3 =", angle3ofisocelesestriangle, "°")
                st.write ("Height =", heightofisocelesestriangle, value)
                
            elif typetriangle == ("Scalene Tringle (no equal sides)"):
                st.write ("Area =", areaofscalenetriangle, value, "sq")
                st.write ("Perimeter =", perimeterofscalenetriangle, value)
                st.write ("Angle 1 =", angle1ofscalenetriangle, "°")
                st.write ("Angle 2 =", angle2ofscalenetriangle, "°")
                st.write ("Angle 3 =", angle3ofscalenetriangle, "°")
                st.write ("Height =", heightofscalenetriangle, value)

            
        
        




            



    
    
    
    
    
    
        
