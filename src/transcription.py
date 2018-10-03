from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

OUTPUT_FOLDER = "output"


def main():
    service = SpeechToTextV1(
        username='17ebf791-4d02-4e4e-9e2d-df6ce4e52913',
        password='UYJwTPmPWDNr',
        url='https://stream.watsonplatform.net/speech-to-text/api')

    model = service.get_model('en-US_BroadbandModel').get_result()
    print(json.dumps(model, indent=2))

    for i in range(1):
        with open(join(dirname(__file__), 'splitted/{}_part.mp3'.format(i + 1)),
                  'rb') as audio_file:
            with open('output/part_{}.txt'.format(i + 1), 'w') as f:
                json.dump(service.recognize(
                    audio=audio_file,
                    content_type='audio/mp3',
                    timestamps=True,
                    word_confidence=True).get_result(), f)


if __name__ == '__main__':
    main()
