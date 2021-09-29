#built in form node image
FROM node

#tell about what should be working directory
WORKDIR /app
#which files should go to image from local system
#THIS WILL TELL ABOUT LOCATION INSIDE OF CONTAINER FILE SYSTEM
COPY . /app


#tell docker how to install dependencies

RUN npm install 


#expose a port to container 

EXPOSE 80
#remember you run a container based on an image 

CMD ["node", "server.js"]


