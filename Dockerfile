FROM python:latest
WORKDIR  /Blog_Flask
ADD . /Blog_Flask
RUN pip install -r requirements.txt
CMD ["python","run.py"]