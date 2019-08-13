import argparse
import pyattck_tool

parser = argparse.ArgumentParser(
  prog="Pyattck Scraping",
  description="Tool for scraping the pyattack file",
  prefix_chars="-"
)

group = parser.add_mutually_exclusive_group()
group.add_argument("-actor")
group.add_argument("-tool")

args = parser.parse_args()

if args.tool:
  pyattck_tool.find_tool()
else:
  pyattck_tool.find_actor()





