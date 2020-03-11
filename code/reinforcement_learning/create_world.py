import numpy as np
import matplotlib.pyplot as plt

world = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 1, 0, 1, 0, 0],
                  [0, 1, 1, 0, 0, 0, 1, 1, 0],
                  [0, 1, 1, 1, 0, 1, 1, 1, 0],
                  [0, 1, 1, 1, 1, 0, 1, 1, 0],
                  [0, 1, 1, 1, 1, 1, 1, 1, 0],
                  [0, 1, 0, 1, 1, 1, 1, 1, 0],
                  [0, 1, 0, 1, 1, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0]])

reward = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 2, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 2, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]])


# plot world
plt.imshow(world)
plt.title("1 : available position\n0 : not available position")
plt.colorbar()
plt.savefig("images/world.pdf")
plt.close()

# plot reward
plt.imshow(reward)
plt.title("reward")
plt.colorbar()
plt.savefig("images/reward.pdf")
plt.close()

np.save("world.npy", world)
np.save("reward.npy", reward)
