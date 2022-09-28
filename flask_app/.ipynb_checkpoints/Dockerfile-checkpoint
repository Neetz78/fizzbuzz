FROM python:3.6.7

WORKDIR /Users/neethug/Desktop/Neethu/flask_gunicorn_nginx_docker/flask_app  
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .


EXPOSE 5000
CMD [ "python", "app.py"]