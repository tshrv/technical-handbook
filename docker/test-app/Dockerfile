FROM python:slim-buster

WORKDIR /usr/src/app/

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py app.py

EXPOSE 80

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]