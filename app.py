import streamlit as st

st.set_page_config (layout="wide")
st.title ("Welcome to Shape calculator")
st.header ("Calculate every singe value on just one click")

typecal = st.radio ("Select the type you want to calculate", ("Square, Square roots, Cubes, Cube roots", "Shapes"))
if typecal == ("Square, Square roots, Cubes, Cube roots"):
    typesq = st.radio ("Select what you want to calculate", ("Squares", "Square roots", "Cubes", "Cube roots"))
    
    if typesq == ("Squares"):
        squarenuber = st.number_input ("Please enter the number whose square you want to find: ")
        square = squarenuber * squarenuber
    elif typesq == ("Square roots"):
        squarerootnumber = st.number_input ("Please enter the number whose square root you want to find: ")
        squareroot = squarerootnumber ** 0.5
    elif typesq == ("Cubes"):
        cubenumber = st.number_input ("Please enter the number whose cube you want to find: ")
        cube = cubenumber * cubenumber * cubenumber
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
    shape = st.radio ("Select Your Shape:", ("Square", "Rectangle", "Cube", "Cuboid", "Circle", "Sphere", "Cylinder", "Trapezium", "General Quadrilateral"))
    value = st.radio ("Choose the unit", ("Millimeters", "Centimeters", "Inch" ,"Meters" ,"Kilometers"))

    if shape == ("Square"):
        lengthofsquare = st.number_input ("Please enter the length of your Square: ")
        try:
            areaofsquare = lengthofsquare * lengthofsquare
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
            volumeofcube = lengthofcube * lengthofcube * lengthofcube
            surfaceareaofcube = 6 * (lengthofcube * lengthofcube)
            lateralsurfaceareaofcube = 4 * (lengthofcube * lengthofcube)
            surfaceareaofonesideofcube = lengthofcube * lengthofcube
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
            areaofcircle = 22/7 * radiusofcircle * radiusofcircle 
            circumferenceofcircle = 2 * 22/7 * radiusofcircle
        
        except:
            st.text ("Enter a value")
            
    
    elif shape ==("Sphere"):
        radiusofsphere = st.number_input("Please enter the radius of shpere: ")
        try:
            surfaceareaofsphere = 4 * 22/7 * radiusofsphere * radiusofsphere
            volumeofsphere = (4 % 3) * 22/7 * radiusofsphere * radiusofsphere * radiusofsphere
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
            volumeofcylinder = 22/7 * radiusofcylinder * radiusofcylinder * heightofcylinder
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
            st.write ("Area =", areaoftrapezium, value, "sq")