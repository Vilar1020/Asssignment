import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

#for drawing a crescent moon with some craters and stars in the background
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.set_facecolor('navy')  # Dark blue night sky

# Draw the main moon circle (will be partially covered)
moon = patches.Circle((0, 0), 30, color='lightgray', ec='white', linewidth=2)
ax.add_patch(moon)

# Draw a slightly smaller circle to create the crescent shape
# Positioned to the right to create the crescent effect
crescent = patches.Circle((8, 0), 28, color='navy')  # Same color as background
ax.add_patch(crescent)

# Add some craters to make it more realistic
crater1 = patches.Circle((-15, 10), 5, color='darkgray', ec='white', linewidth=1)
crater2 = patches.Circle((5, 15), 3, color='darkgray', ec='white', linewidth=1)
crater3 = patches.Circle((-10, -15), 4, color='darkgray', ec='white', linewidth=1)
ax.add_patch(crater1)
ax.add_patch(crater2)
ax.add_patch(crater3)

# Add some stars in the background
for i in range(50):
    x = np.random.uniform(-60, 60)
    y = np.random.uniform(-60, 60)
    size = np.random.uniform(0.5, 2)
    star = patches.Circle((x, y), size, color='white')
    ax.add_patch(star)

# Set limits and remove axes
ax.set_xlim(-60, 60)
ax.set_ylim(-60, 60)
ax.axis('off')

# Save as PNG
plt.savefig('moon_drawing.png', bbox_inches='tight', pad_inches=0.1, dpi=100)
plt.close()

# drawing a sun with rays extending outward
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.set_facecolor('lightblue')

# Draw the sun (center circle)
sun_center = patches.Circle((0, 0), 30, color='yellow', ec='orange', linewidth=2)
ax.add_patch(sun_center)

# Draw sun rays (triangles around the circle)
num_rays = 12
ray_length = 20
for i in range(num_rays):
    angle = 2 * np.pi * i / num_rays
    x = 30 * np.cos(angle)
    y = 30 * np.sin(angle)
    
    # Create a triangle for the ray
    ray = patches.RegularPolygon(
        (x * 1.5, y * 1.5),  # Position the ray further out
        numVertices=3,        # Triangle
        radius=ray_length,
        orientation=angle,
        color='orange'
    )
    ax.add_patch(ray)

# Set limits and remove axes
ax.set_xlim(-80, 80)
ax.set_ylim(-80, 80)
ax.axis('off')

# Save as PNG
plt.savefig('sun_drawing.png', bbox_inches='tight', pad_inches=0.1, dpi=100)
plt.close()