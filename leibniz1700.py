import numpy as np
from config import box_width,box_height

# Meeus p. 222
def equation_of_center(e, m):
    return ((2*e-e**3/4+5*e**5/96)*np.sin(m)+(5*e*e/4-11*e**4/24)*np.sin(2*m)+
            (13*e**3/12 - 43*e**5/64)*np.sin(3*m) + 103*e**4*np.sin(4*m)/96+
            1097*e**5*np.sin(5*m)/960)

# creates a circle with Euler angle delta and eps
# this ia an ellipse if view along the y-axis
def make_ellipse(delta,eps):
    
    ex=np.array([np.cos(delta),-np.sin(delta),0])
    ey=np.array([np.sin(delta)*np.cos(eps),np.cos(delta)*np.cos(eps),np.sin(eps)])

    x=np.zeros(100)
    y=np.zeros(100)
    z=np.zeros(100)
    phi=np.linspace(0,2*np.pi,100)

    for i in range(len(phi)):
        el=phi[i]
        x[i]=ex[0]*np.cos(el)+ey[0]*np.sin(el)
        y[i]=ex[1]*np.cos(el)+ey[1]*np.sin(el)
        z[i]=ey[2]*np.sin(el)
    return x,y,z

# kepler equation for the radius vector
def radius(phi,a=1,epsilon=0.3):
    return a*(1-epsilon**2)/(1-epsilon*np.cos(phi))

# reads a file with the dates (not months) of luna 14 
# between March 21 and April 18 in the Gregorian calendar
#
def read_moons(file, delta=0):
    res=[]
    f=open(file,'r')
    # file contains one column with the date of the easter moon
    for line in f:
        col=line.strip()
        moon=int(col)
        # 1st April and so on -> 32nd March
        if moon<=19:
            moon=moon+31
        
        # start with 1 for March 21
        moon=moon-20
        
        # delta is the Gregorian shift (0 between 1900 and 2199)
        res.append((moon-1+delta)%30+1)
    f.close()
    
    return res


# luna 14 markers are plotted according to the dates in 'luna14'
def plot_boxes(ax,luna14,hatch='///'):
    # plot luna 14
    for gn in range(1,20):
   
        xp=((31-luna14[gn-1])-1)*box_width
        yp=(gn-1+0.1)*box_height

        # fill boxes
        ax.fill_between(np.linspace(xp,xp+box_width,10),np.repeat(yp,10),
            np.repeat(yp+box_height,10), facecolor="none", edgecolor='k',
                        hatch=hatch)

