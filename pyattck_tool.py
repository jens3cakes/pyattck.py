from pyattck import Attck 
import argparse

attack = Attck()

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-actor')
group.add_argument('-tool')
args = parser.parse_args()
 
def find_actor():
  attack_info = open("attack_file3.txt", "a")
  for actor in attack.actors:
    if args.actor in actor.name:
      attack_info.write("Actor's name: " + actor.name)
      for tech in actor.techniques:
        attack_info.write("\n" + "Technique or techniques used: " + tech.name)
      for mal in actor.malware:
        attack_info.write("\n" + "Malware used: " + mal.name)
      for tools in actor.tools:
        attack_info.write("\n" + "Tool or tools used: " + tools.name)
  attack_info.close()
    
    
def find_tool():
  for tool in attack.tools:
    if tool.name == args.tool:
      print("this it is the " + args.tool)
      for actor in tool.actors:
        print(actor.name)

find_actor() 
find_tool()