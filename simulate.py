import pybullet as p

physicsClient = p.connect(p.GUI)    # creates object 'physicsClient', handles physics, and draws results to GUI
p.disconnect()
# pass        # simulate.py file for now does nothing