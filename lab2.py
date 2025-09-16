with open("auth.log" , "r") as f:
    pattern = r"\d+\.\d+\.\d+\.\d+"
    for line in f:
       print(f:.findall(pattern, line))
