# . json Module
# 👇 Why?
# Used in APIs to send & receive data


# 💼 Used in:
# Backend APIs (Flask, FastAPI)

# Storing app settings/config

# Client-server communication

import json

data = {
  "name": "Hariom Shah",
  "phone": 9811243552
}

print(data)

json_string = json.dumps(data)
print(json_string)

# without converting into json
print(json_string[0])

# converting back
convert_json = json.loads(json_string)
print(convert_json["name"])