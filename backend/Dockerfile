FROM python:3.11-alpine

WORKDIR backend

COPY backend/requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENV FLASK_APP=backend/app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=0
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

COPY backend .

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]
