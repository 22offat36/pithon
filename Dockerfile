# a simple for docker 
FROM python:2.7

ADD facts.py /

RUN pip install requests

CMD [ "python", "./facts.py" ]
