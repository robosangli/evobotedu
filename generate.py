# use pyrosim to generate a link (later, several links comprising the world),
# store it in a special file called world.sdf, and
# simulate.py will then read it in and simulate it.
import pyrosim.pyrosim as pyrosim       # Python Robot Simulator package communicates easily with Pybullet

pyrosim.Start_SDF("box.sdf")            # information of world being created will be stored in 'box.sdf'
# Note: SDF stands for Software Development Folder
length = 1
width = 2
height = 3
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[length,width,height])     # stores box's initial position and dimensions into 'box.sdf'
pyrosim.End()                           # closes the sdf file