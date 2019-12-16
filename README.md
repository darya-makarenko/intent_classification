# Intent Classification Service

*The service uses SpaCy and nltk to preprocess text and get it to normalised form without punctuation and then convert it to vector representation.*

## Docker usage:
1) To build docker container type `docker build -t intent_classify .` in intent_classify folder.
2) To run Docker container type `docker run -p 5000:5000 intent_classify`.

## Service API:
1) To start Swagger and get all available methods visit `<base_url>:5000`. Example: `127.0.0.1:5000`.
2) If you want to get information about the intent classification service, make GET request to the endpoint `<base_url>:5000/classify_intent`.
  NB: You can perform all requests with the help of Swagger (see par. 1), or you can choose Postman, curl or your custom web-client.
3) In order to classify one or more texts send POST request to the endpoint `<base_url>:5000/classify_intent` with JSON object in the request body:
  <pre>
  {
  "texts": [
      {
        "text": "нет, не правильно",
        "lang": "ru"
      }
  ]}
  </pre>
  
## Project details:

1) main.py - start point of the project.
2) view.py - specifies service endpoints.
3) intent_classify.py - implements intent classification functionality.
4) positive.csv - dataset of positive (yes) phrases.
5) negative.csv - dataset of negative (no) phrases.

**methods of "intent_classify.py"**

- def cleanup_text(text, logging=False):
      deletes punctuation from texts and normalises them
- def classify_intent(texts):
      expects an array of texts and produces the array of following structure:
<pre>
      [
          {
            'text': text['text'], 
            'lang': text['lang'],
            'intents': [
              { 'label': 'pos',
                'conf': preds[0][0]
              },
              {'label': 'neg', 
               'conf': preds[0][1]
              }]
          }
      ]
</pre>


## Docker problems:
1) If you get problem with already used ports when starting docker image type:
`docker ps` to show list of running containers and kill (see par. 4) container that uses this port.
2) If first advice didn't work, try typing `docker container prune`.
3) You can then try typing `docker system prune`.
4) To kill running docker container type `docker ps` to show list of running containers, then use command `kill <deleted_container_id>`. You can either use id of running container or it's name. 
5) To see list of all built docker images type `docker images`.

  
  
  
  
  
