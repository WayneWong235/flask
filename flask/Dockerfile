FROM python:2.7-stretch

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install pymysql
EXPOSE 5000

COPY . /app

ENTRYPOINT [ "python" ] 
CMD [ "runserver.py","&" ]
