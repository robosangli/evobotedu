# use pyrosim to generate a link (later, several links comprising the world),
# store it in a special file called world.sdf, and
# simulate.py will then read it in and simulate it.
import pyrosim.pyrosim as pyrosim       # Python Robot Simulator package communicates easily with Pybullet

pyrosim.Start_SDF("world.sdf")          # information of world being created will be stored in 'world.sdf'
# Note: SDF stands for Software Development Folder
length = 1                              # in units of m
width = 1
height = 1
x = 0
y = 0
z = height/2.0                          # ensure that the bottom surface is right at ground level (& not embedded into the floor)
pyrosim.Send_Cube(name="Block", pos=[x,y,z], size=[length,width,height])        # creates a simple block
pyrosim.End()                           # closes the sdf file