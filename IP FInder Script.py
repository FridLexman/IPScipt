import re

with open(r'C:\Users\jacdo\Downloads\au.csv') as fh:
   fstring = fh.readlines()
  
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\,\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')


newFile = open("AU Sorted IPs", "w")
for line in fstring:
   newFile.write(pattern.search(line).group()+"\n")
   
newFile.close()