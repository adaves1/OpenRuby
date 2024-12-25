def version():
    print("OpenRuby v1.02.0 GitHub Port HTTPS by adaves1")

class ActionFlow:

    actionflowa = 0

    def RubyActionflow():
        cone = input("Welcome to RubyChatter. Please give the required details to create an actionflow.")
        print("1. Provide the name of the actionflow. ")
        afname = input(" ")
        print("2. Provide the ID of the actionflow. ")
        afid = input(" ")
        print("3. Provide the UIC of the actionflow. ")
        afuic = input(" ")
        print("All details provided. Creating an actionflow...")
        global actionflowa
        actionflowa = "openruby.af." +  afname + "." + afid + "." + afuic
        print(f"Actionflow '{afname}' created with ID '{afid}' and UIC '{afuic}' ")
        print("OpenRuby")

    def RubyActionflow_pre(name, id, uic):
        global actionflowa
        actionflowa = "openruby.af." +  name + "." + id + "." + uic
        print(f"Actionflow '{name}' created with ID '{id}' and UIC '{uic}' ")
        print("Actionflows 1 of 1 left. OpenRuby")

    def RubyActionflow_delete(name, id, uic):
        global actionflowa
        actionflowa = 0
