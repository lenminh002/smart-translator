run python3 extension/app/app.py while open extension to let it works.



docker build -t translator-backend .
docker run -p 8080:8080 --env-file .env translator-backend