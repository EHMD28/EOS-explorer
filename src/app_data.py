import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0, 2 * np.pi, 100)
sin_y_values = np.sin(x_values)
cos_y_values = np.cos(x_values)
fig, ax = plt.subplots()

ax.plot(x_values, sin_y_values, color="red", label="sin x")
ax.plot(x_values, cos_y_values, color="blue", label="cos x")
ax.axhline(y=0, linestyle="--", color="green")
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.legend()
fig.tight_layout()
