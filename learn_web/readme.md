This project is from Moscow Python learning lessons.

Use git checkout v1.x for switch between different stages of app.

For launch app use Docker.

docker build -t newsserver:latest .

don't forget DOT at the end of command

then 

docker run -d -p 5000:5000 newsserver

In browser perform request:
192.168.99.100:5000 (if use Docker Quickstart terminal)
or 
localhost:5000 
