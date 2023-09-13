import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)    # creates object 'physicsClient', handles physics, and draws results to GUI
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)      # disable pybullet sidebars resulting in speed-up of GUI simulation
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)              # adds the force of gravity to exist in the world
planeId = p.loadURDF("plane.urdf")  # adds a floor to the simulation from preexisting Pybullet data
p.loadSDF("boxes.sdf")                # pybullet reads in the world described in 'box.sdf' (from generate.py)
for i in range(0, 500):
    p.stepSimulation()              # stepping the world: slowing things down to see the simulated world
    print("for: ", i)               # to get a real-time sense of how long each loop iteration takes
    time.sleep(1/60)                # sleeping by 1/60th of a second during each pass through the loop
p.disconnect()
# pass        # simulate.py file for now does nothing