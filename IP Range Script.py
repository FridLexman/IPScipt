import re

def ipRange(start_ip, end_ip):
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    ip_range = []

    ip_range.append(start_ip)
    while temp != end:
        start[3] += 1
        for i in (3,2):
            if temp[i] == 256:
                temp[i] = 0
                temp[i-1] += 1
            ip_range.append(".".join(map(str, temp)))
            
    return ip_range
with open(r'AU Sorted IPs') as f:
    fstring = f.readlines()
    
newFile = open("AU IP Block.txt", "w")    

start_ip = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1})')
end_ip = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{3})')
  

for line in fstring:
    ip_range = ipRange(start_ip.search(line).group(), end_ip.search(line).group())

    for ip in ip_range:
        newFile.write((ip)+"\n")
        print(ip)

newFile.close()