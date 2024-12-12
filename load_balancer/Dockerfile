FROM python:3.11-alpine

WORKDIR load_balancer

COPY load_balancer/requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY load_balancer .

EXPOSE 3000

CMD ["python3", "main.py"]
