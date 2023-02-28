FROM python:3.8

LABEL maintainer="hj146@duke.edu"

COPY . /src

WORKDIR /src

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]