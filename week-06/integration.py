import numpy as np

x = np.linspace(0,90,1000)
rad_x = np.deg2rad(x)
y = np.sin(rad_x)
np.savetxt("sine.dat", np.c_[x,y], fmt = "%8.5f")
final_sum=0
for i, val in enumerate(y):
    if i in [0, len(y)-1]:
        final_sum+=val
    else:
        final_sum+=(2*val)

final_int = (final_sum/2)*(rad_x[1]-rad_x[0])
print(final_int)

