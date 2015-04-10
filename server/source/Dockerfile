FROM python:2.7

ADD . /source
RUN pip install -r requirements.txt

EXPOSE 80
CMD ["python", "server.py"]
