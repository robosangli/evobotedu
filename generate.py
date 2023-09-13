# use pyrosim to generate a link (later, several links comprising the world),
# store it in a special file called world.sdf, and
# simulate.py will then read it in and simulate it.
import pyrosim.pyrosim as pyrosim       # Python Robot Simulator package communicates easily with Pybullet

pyrosim.Start_SDF("boxes.sdf")          # information of world being created will be stored in 'boxes.sdf'
# Note: SDF stands for Software Development Folder
length = 1                              # in units of m
width = 1
height = 1
x = 0
y = 0
z = height/2.0                          # ensure that the bottom surface is right at ground level (& not embedded into the floor)
# pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])     # stores box's initial position and dimensions into 'boxes.sdf'
# pyrosim.Send_Cube(name="Box2", pos=[x + length,y,z + height] , size=[length,width,height])     # stores box2's initial position and dimensions
for i in range(0, 10):                  # using a for loop to procedurally generate each block in the tower
    pyrosim.Send_Cube(name=("Box"+str(i)), pos=[x,y,z + (i*height)] , size=[length*(0.9**i),width*(0.9**i),height*(0.9**i)])
pyrosim.End()                           # closes the sdf file