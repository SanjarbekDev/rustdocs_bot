RUN pip3 install -U pip

RUN pip3 install -U -r requirements.txt

CMD python3 app.py
