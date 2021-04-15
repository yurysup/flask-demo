FROM python:3.6-slim
WORKDIR /flask-code
COPY . /flask-code
RUN pip3 install flask gunicorn
#ENV FLASK_APP hello.py
#ENV PYTHONUNBUFFERED True
#CMD flask run --host=0.0.0.0
CMD gunicorn -w 4 -b 0.0.0.0:5000 hello:app