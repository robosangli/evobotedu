# use pyrosim to generate a link (later, several links comprising the world),
# store it in a special file called world.sdf, and
# simulate.py will then read it in and simulate it.
import pyrosim.pyrosim as pyrosim       # Python Robot Simulator package communicates easily with Pybullet

pyrosim.Start_SDF("box.sdf")            # information of world being created will be stored in 'box.sdf'
# Note: SDF stands for Software Development Folder
length = 1
width = 2
height = 3
x = 0
y = 0
z = height/2.0                          # ensure that the bottom surface is right at ground level (& not embedded into the floor)
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])     # stores box's initial position and dimensions into 'box.sdf'
pyrosim.End()                           # closes the sdf file