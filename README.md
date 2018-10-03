# TEST TASK VILMATE

####0. Total Spent time ~ 6hr

___
####1. Create ELK docker
Based on the official Docker images from Elastic:

* [elasticsearch](https://github.com/elastic/elasticsearch-docker)
* [logstash](https://github.com/elastic/logstash-docker)
* [kibana](https://github.com/elastic/kibana-docker)

##### Usage

Start the stack using `docker-compose`:

```console
$ docker-compose up
```

By default, the stack exposes the following ports:
* 5000: Logstash TCP input.
* 9200: Elasticsearch HTTP
* 9300: Elasticsearch TCP transport
* 5601: Kibana
___

####2. Get audio podcast of youtube video

My example: 
```buildoutcfg
Joe Rogan Experience #1169 - Elon Musk
https://www.youtube.com/watch?v=ycPr5-27vSI
```

Check `download_video_and_get_audio_from_it.py`
___

####3. Convert it to mp3 and split for Watson API

Check 
 - `mp4tomp3.py`
 - `mp3_splitting.py`
 - `transcription.py`
___

####4. Get most relevant words

Check `text_processing.py`

####5. Load it to ES

Check `data_to_es.py`

___

####Author: 

*Timofey Antonenko*


