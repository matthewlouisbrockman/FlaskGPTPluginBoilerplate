import requests
r = requests.post('http://localhost:5000/pictures/generate_picture', json={'pictureDescription':'hi'})

print(r.text)

r = requests.get('http://localhost:5000/pictures/generate_picture')

print(r.text)

r = requests.post('https://turtlesandpipe1.herokuapp.com/pictures/generate_picture', json={'pictureDescription':'hi'})

print(r.text)

r = requests.get('https://turtlesandpipe1.herokuapp.com/pictures/generate_picture')

print(r.text)