"""
===================
Visualize SDF Actor
===================
Here is a simple tutorial that shows how to visualize SDF primtives using FURY.
"""

import numpy as np
from fury import window, actor

###############################################################################
# Lets define varibles for the SDF Actor

dirs = np.random.rand(3, 3)
colors = np.random.rand(3, 3) * 255
centers = np.array([[1, 0, 0], [0, 0, 0], [-1, 0, 0]])
scale = np.random.rand(3, 1)


###############################################################################
# Create SDF Actor

sdfactor = actor.sdf(centers=centers, directions=dirs, colors=colors,
                     primitives=['sphere', 'torus', 'ellipsoid'],
                     scale=scale)

##############################################################################
# Create a scene

scene = window.Scene()
scene.background((1.0, 0.8, 0.8))
scene.add(sdfactor)


###############################################################################
# Show Manager
#
# Since all the elements have been initialised,we add them to the show manager.

current_size = (1024, 720)
showm = window.ShowManager(scene, size=current_size,
                           title="Visualize SDF Actor")

interactive = True

if interactive:
    showm.start()

window.record(scene, out_path='viz_sdfactor.png', size=current_size)
