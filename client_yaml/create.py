import yaml

client_ur = {"robot_name":"ur","height":1.0,"obj_namelists":['toothpaste'],"home":[0.3,0.0,0.1],"pick_height":-0.03,"place_height":-0.1,"calibration_start":[-0.3,0.3,0.],"calibration_speed":-0.5,"url":'rr+tcp://bbb2.local:58652?service=ur_robot'}
client_sawyer = {"robot_name":"sawyer","height":1.0,"obj_namelists":['bottle'],"home":[0.,0.3,0.3],"pick_height":-0.03,"place_height":-0.1,"calibration_start":[0.6,-0.2,0.15],"calibration_speed":0.05,"url":'rr+tcp://bbb1.local:58654?service=sawyer'}
client_abb = {"robot_name":"abb","height":1.0,"obj_namelists":['perfume'],"home":[0.3,0.0,0.3],"pick_height":-0.03,"place_height":-0.1,"url":'rr+tcp://bbb3.local:58655?service=staubli'}
client_staubli = {"robot_name":"staubli","height":1.0,"obj_namelists":['soap'],"home":[0.3,0.0,0.3],"pick_height":-0.03,"place_height":-0.1,"url":'rr+tcp://bbb4.local:58656?service=abb'}

with open(r'client_ur.yaml', 'w') as file:
    documents = yaml.dump(client_ur, file)
with open(r'client_sawyer.yaml', 'w') as file:
    documents = yaml.dump(client_sawyer, file)
with open(r'client_abb.yaml', 'w') as file:
    documents = yaml.dump(client_abb, file)
with open(r'client_staubli.yaml', 'w') as file:
    documents = yaml.dump(client_staubli, file)


with open(r'client_ur.yaml') as file:
    documents = yaml.load(file, Loader=yaml.FullLoader)
    print(documents)