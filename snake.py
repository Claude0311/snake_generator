from odio_urdf.odio_urdf import *

material = Material(Color(rgba="0.792156862745098 0.819607843137255 0.933333333333333 1"),name='')
geo0 = Geometry(Mesh(filename='package://final_v1/meshes/base_link.STL'))
geor = Geometry(Mesh(filename='package://final_v1/meshes/rod_one.STL'))
geol = Geometry(Mesh(filename='package://final_v1/meshes/link_one.STL'))
ori0 = Origin(xyz=(0,0,0),rpy=(0,0,0))
ori1 = Origin(xyz=(0.2159,0,0),rpy=(3.1416,0,0))
ori2 = Origin(xyz=(0.2159,0,0),rpy=(-3.1416,0,0))
vis1 = Visual(ori0)
lim = Limit(effort=1000, velocity=0.1, lower=-3.14, upper=3.14)


Links = []
for index in range(1,11):
    parity = (-1)**index
    if index==1:
        j1 = Joint("rod_%i_joint"%index,
                Parent("link_%i"%(index-1)), Child("rod_%i"%(index)),
                Origin(xyz=(0.2159,0,0),rpy=(0,0,0)),
                lim,
                type="revolute")
    else:
        j1 = Joint("rod_%i_joint"%index,
                Parent("link_%i"%(index-1)), Child("rod_%i"%(index)),
                Origin(xyz=(0.2159,0,0),rpy=(0,0,0)),
                lim,
                type="revolute")
    l1 = Link("rod_%i"%index,Visual(ori0,geor,material))
    j2 = Joint("link_%i_joint"%index,
            Origin(xyz=(0,0,0), rpy=(parity*1.5708,0,0)),
            Parent("rod_%i"%index), Child("link_%i"%(index)),
            Axis(xyz=(0,0,1)),type='fixed')
    l2 = Link("link_%i"%index,
            Visual(ori0, geol, material))
    Links.extend([j1,l1,j2,l2])

my_robot = Robot(
    Link("world"),
    Joint("world_joint",Parent("world"),Child("link_0"),ori0,type="fixed"),
    Link("link_0",Visual(ori0,geo0,material)),
    *Links
)

print(my_robot) #Dump urdf to stdout

text_file = open("sample.urdf", "w")
n = text_file.write(str(my_robot))
text_file.close()