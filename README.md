# evobotedu
This code repository was created by Ananda Sangli on September 4 2023 while following Josh Bongard's Education in Evolutionary Robotics Course. This online course is based on CS206 which Josh teaches at The University of Vermont.
# Simulation
An object was created to handle the physics (pybullet) and draw the results to a GUI simulation. The time library is used to step into the simulated world while slowing things down on the GUI.
# One Link
The Python Robot Simulator (Pyrosim) package was used to generate a link in the form of a Software Development Folder (SDF). The position and dimension of the link were specified and Pyrosim shields most details of Pybullet into the SDF, 'box.sdf'. This SDF is also loaded into the simulation.
# Many Links
Pybullet is a physics engine that simulates physics by
    1. Applying forces to each link in the world
    2. Updating its acceleration based on the forces that are acting on it using F = ma
    3. Updating the new position and orientation of each link using its new acceleration
