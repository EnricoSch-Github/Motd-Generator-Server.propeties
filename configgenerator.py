import re
import os


Serversettings = []

#  Read the file where the server.properties is.

File = open(r"C:\Users\Enrico\OneDrive\Documents\MinecraftPlugins\server.properties","r").read().split("\n")

# Search for the motd line and deleted it

with open(r"C:\Users\Enrico\OneDrive\Documents\MinecraftPlugins\server.properties","r") as input:
    with open(r"C:\Users\Enrico\OneDrive\Documents\MinecraftPlugins\server.propertiesnew", "w") as output:
        # iterate all lines from file
        for line in input:
            # if line starts with substring 'motd' then don't write it in temp file
            if not line.strip("\n").startswith('motd'):
                output.write(line)

os.replace("server.propertiesnew","server.properties")


File = open(r"C:\Users\Enrico\OneDrive\Documents\MinecraftPlugins\server.properties","a+")
File.write('\nmotd=' + "\\" + 'u00A77' + "\\" + 'u00A7lhttps\://dc.valhallamc.io')