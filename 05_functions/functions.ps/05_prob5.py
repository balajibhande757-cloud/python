import math
import requests
print(math.sin(math.radians(90)))
print(math.sqrt(144))

a=requests.get("https://api.github.com")

print(a.json())