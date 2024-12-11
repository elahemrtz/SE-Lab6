FROM python:3.11-alpine

WORKDIR backend

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV FLASK_APP "backend/app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG 0

COPY . .

EXPOSE 8080

CMD [ "python3", "-m" , "flask", "run"]
