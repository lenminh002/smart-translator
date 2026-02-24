## HOW TO RUN LOCALLY
1. upload extension to chrome://extensions/ and enable developer mode.
2. run **python3 extension/app/app.py** while open extension to let it works.

## HOW TO DEPLOY WITH DOCKER LOCALLY
1. run **docker build -t translator-backend .**
2. run **docker run -p 8080:8080 --env-file .env translator-backend**
3. upload extension to chrome://extensions/ and enable developer mode.
4. change the host in **extension/index.js** to **http://localhost:8080**

## HOW TO DEPLOY WITH DOCKER USING DOKPLOY
- I've already deployed the backend so you can just try out the extension yourself by simply upload extension to chrome://extensions/ and enable developer mode, or:
1. Create a new project on [Dokploy].
2. Import this project to Dokploy.
3. Change the host in **extension/index.js** to your Dokploy domain.
4. Upload extension to chrome://extensions/ and enable developer mode.


