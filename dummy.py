#!/usr/bin/env python

import os, sys, json, re

def searchHosts():
  inventory = {}

  for root, dirs, files in os.walk('.'):
    for filename in files:
      fullpath = os.path.join(root, filename)

      if fullpath.endswith(".yml"):
        with open(fullpath, 'r') as f:
          results = re.findall(r"(?<=hosts:\s).*", f.read())

          for item in results:
            if "{" in item:
              continue

            list = [ i.strip() for i in item.split(":&") ]

            for i in list:
              inventory[i] = ["localhost"]

  print(json.dumps(inventory, indent=4))

if __name__ == "__main__":
  searchHosts()
