Checkpoint Information:

- backend API and frontend do not communicate yet
- backend has database plus dockerfiles setup
- some simple endpoints have been setup in the backend but no proper authentication has
  been implemented
- frontend has several pages with static data modelled after a wireframe design using adobe xd:
  https://xd.adobe.com/view/4a70b26b-246b-402a-67de-33fb60d54932-3c41/

Setup:

backend
- docker-compose build && docker-compose up
- browsable django-rest-framework api viewable at: http://localhost:8080/
- example endpoint where you can create users: http://localhost:8080/users/
- we also have custom login and logout endpoints but they are currently broken
 - http://localhost:8080/users/login
 - http://localhost:8080/users/logout

frontend
- npm i && npm run start
- website viewable at: http://localhost:3000/
- little to no interactivity besides switching pages
