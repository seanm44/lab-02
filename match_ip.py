import re

pattern = r"\d+\.\d+\.\d+\.\d+"
text = "Failed login from 192.168.0.1 at 10:30 and 10.0.0.5 and 192.168.200.10"

print(re.findall(pattern, text))