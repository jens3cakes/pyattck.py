from pyattck import Attck 
import argparse

attack = Attck()

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-actor')
group.add_argument('-tool')
args = parser.parse_args()


def report_maker():
  file = open('attack_file.txt',"w")
  file.write()
  file.close()
  #tool_list = attack.too
 
def find_actor():
  attack_info = open("attack_file3.txt", "a")
  for actor in attack.actors:
    if args.actor in actor.name:
      attack_info.write(actor.name)
      print(actor.name)
      for tech in actor.techniques:
        attack_info.write("\n" + tech.name)
        print("this is " + tech.name)
      for mal in actor.malware:
        attack_info.write("\n" + mal.name)
        print("this " + mal.name)
      for tools in actor.tool:
        attack_info.write("\n" + tools.name)
        print("This is the tool used: " + tools.name)
  attack_info.close()
    
    
def find_tool():
  for tool in attack.tools:
    if tool.name == args.tool:
      print("this it is the " + args.tool)
      for actor in tool.actors:
        print(actor.name)

    
      print(actor.name)
      # if args.name in actor:
      #   print(args.name)
         
    

#find_actor() 
find_tool()

  
# if __name__ == "__main__":
#   find_actor()