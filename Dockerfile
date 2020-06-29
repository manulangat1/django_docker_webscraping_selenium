FROM python:3.6

RUN mkdir -p /code 
WORKDIR /code 

RUN pip install -r requirements.txt

COPY . /code 

EXPOSE 8000 

CMD ["gunicorn" ,"--chdir","webs",":8000","webs.wsgi:application"]