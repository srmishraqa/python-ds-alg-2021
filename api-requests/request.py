import requests

response = requests.get("https://gitlab.com/api/v4/users/navan_k/projects")
print(type(response))

# print(response.text)
# print(type(response.text))

# reads response in JSON format and return it as a list data type
print(response.json())
print(type(response.json()))
my_projects = response.json()
print('------------------------')

for project in my_projects:
    print(f"Project Name is : {project['name']}")
    print(f"project URL is : {project['web_url']}")
    print("-------------------------------------->")
