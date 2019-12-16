FROM python:3.6
COPY . /intent_classify
WORKDIR /intent_classify
RUN pip install -r requirements.txt
RUN pip install -U spacy
#RUN pip install -U spacy-lookups-data
RUN python -m spacy download xx_ent_wiki_sm
#EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["/usr/local/bin/gunicorn"  , "-c", "gunicorn.conf", "main:app"]
#CMD ["main.py"]