# Import matplotlib and numpy to get the value of Pi
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# # Add a bar in the polar coordinates
# plt.subplot(111, polar=True);
# plt.bar(x=0, height=10, width=np.pi/2, bottom=5);
# Build a dataset
df = pd.DataFrame(
        {
            'Name': ['Treatment ' + str(i) for i in list(range(1, 81)) ],
            'Value': np.random.randint(low=10, high=100, size=80)
        })
# # Show 3 first rows
# df.head(3)
print (df)
# set figure size
plt.figure(figsize=(20,10))
# plot polar axis
ax = plt.subplot(111, polar=True)
# remove grid
plt.axis('off')
# Set the coordinates limits
upperLimit = 100
lowerLimit = 30
# Compute max and min in the dataset
max = df['Value'].max()
# Let's compute heights: they are a conversion of each item value in those new coordinates
# In our example, 0 in the dataset will be converted to the lowerLimit (10)
# The maximum will be converted to the upperLimit (100)
slope = (max - lowerLimit) / max
heights = slope * df.Value + lowerLimit
# Compute the width of each bar. In total we have 2*Pi = 360°
width = 2*np.pi / len(df.index)
# Compute the angle each bar is centered on:
indexes = list(range(1, len(df.index)+1))
angles = [element * width for element in indexes]
angles
# Draw bars
bars = ax.bar(
    x=angles,
    height=heights,
    width=width,
    bottom=lowerLimit,
    linewidth=2,
    edgecolor="white")
# Draw bars
bars = ax.bar(
    x=angles,
    height=heights,
    width=width,
    bottom=lowerLimit,
    linewidth=2,
    edgecolor="red",
    color="pink",
)
# little space between the bar and the label
labelPadding = 4
# Add labels
for bar, angle, height, label in zip(bars,angles, heights, df["Name"]):
    # Labels are rotated. Rotation must be specified in degrees :(
    rotation = np.rad2deg(angle)
    # Flip some labels upside down
    alignment = ""
    if angle >= np.pi/2 and angle < 3*np.pi/2:
        alignment = "right"
        rotation = rotation + 180
    else:
        alignment = "left"
    # Finally add the labels
    ax.text(
        x=angle,
        y=lowerLimit + bar.get_height() + labelPadding,
        s=label,
        ha=alignment,
        va='center',
        rotation=rotation,
        rotation_mode="anchor")
plt.show()
