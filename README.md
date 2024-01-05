Short description:

  This is a project I am working on for university. I am exporting the faces of different mechanical components developed in SolidWorks and with Python I am generating the contours of the objects and get the positions in space for the CNC to move to.
  The software will give as output the positions, speeds and accelerations for a four axis CNC machine (two horizontal axis and two vertical axis) that cuts using hot wire.
  The goal of the project is to be able to replace the usual method of controling a CNC (generating or writting G CODE based on the object we have to create) with a more mathematical aproach of using polynomial equations for obtaining 
the necessary trajectories and speeds.

--------------------------------------

Getting the points:
  - The points will be added trough a GUI using a button, and they will be moved on the required position by mouse.
  - To be able to cut into more different shapes we will have the points generated on both the front and the back of the image at the same time, and we can modify the points on the images independently.

---------------------------------------

Connection of the points:
  - For connecting points we will use a polynomial equation with of the fifth degree which has the general form:  f(x) = a⋅x^5 + b⋅x^4 + c⋅x^3 + d⋅x^2 + e⋅x + g
  - From this equation we can determine the speed by which we want to move to the midle of the cutting position by applying the first derivative.
  - By deriving the speed we can obtain the acceleration needed.
  - These will be plotted based on time, which is the third parameter for each individual point. Having the plots for speed, position and acceleration we can addept the coefficients of the polinom for better results.  

---------------------------------------


 
