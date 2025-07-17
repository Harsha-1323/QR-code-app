# RUN THIS COMMAND
docker build -t qr-code-app:latset .
docker run -d -p 5000:5000 --name qr-app qr-code-app

