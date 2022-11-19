from odio_urdf.odio_urdf import *

material = Material(Color(rgba="0.792156862745098 0.819607843137255 0.933333333333333 1"),name='')
mb =Material(Color(rgba="0.2 0.1 0.8 1.0"),name='') 
mg = Material(Color(rgba="0.1 0.8 0.1 1.0"),name='') 
mr = Material(Color(rgba="0.8 0.1 0.1 1.0"),name='') 
geo1 = Geometry(Mesh(filename='package://final_v1/meshes/servo.stl',scale = (0.002,0.002,0.002)))
geo0 = Geometry(Mesh(filename='package://final_v1/meshes/base_link.STL'))
geor = Geometry(Mesh(filename='package://final_v1/meshes/rod_one.STL'))
geol = Geometry(Mesh(filename='package://final_v1/meshes/link_one.STL'))
ori0 = Origin(xyz=(0,0,0),rpy=(0,0,0))
ori0_0 = Origin(xyz=(0,0,0.072),rpy=(1.57079632679,0,0))
ori1 = Origin(xyz=(0.2159,0,0),rpy=(3.1416,0,0))
ori2 = Origin(xyz=(0.2159,0,0),rpy=(-3.1416,0,0))
vis1 = Visual(ori0)
lim = Limit(effort=1000, velocity=0.1, lower=-3.14, upper=3.14)
pi2 = 1.57079632679

Links = []
for index in range(1,40):
    parity = (-1)**index
    if parity==1:
        m = mg
    else:
        m=mr
    j1 = Joint("joint%i"%index,
            Origin(xyz=(0,0,0.072),rpy=(0,0,parity*1.57079632679)),
            lim,
            Parent("link_%i"%(index-1)),Child("link_%i"%index),type="continuous")
    l1 = Link("link_%i"%index,
            Origin(xyz=(0,0,0.036),rpy=(0,0,0)),
            Visual(Origin(xyz=(0,0,0.072),rpy=(1.57079632679,0,0)),geo1,m))
    Links.extend([j1,l1])

my_robot = Robot(
    Link("world"),
    Joint("world_joint",Parent("world"),Child("link_0"),ori0,type="fixed"),
    Link("link_0",Visual(ori0_0,geo1,mb),Origin(xyz=(0,0,0),rpy=(pi2,0,pi2))),
    *Links
)

print(my_robot) #Dump urdf to stdout

text_file = open("sample.urdf", "w")
n = text_file.write(str(my_robot))
text_file.close()