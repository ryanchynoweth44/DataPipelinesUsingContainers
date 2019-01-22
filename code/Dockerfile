FROM python:3.6

RUN mkdir /src
COPY . /src/
WORKDIR /src
RUN pip install -r requirements.txt
RUN pip install .
CMD [ "python", "./application/extract_data.py" ]