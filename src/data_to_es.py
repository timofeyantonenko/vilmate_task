import os

import json

from os import listdir
from os.path import isfile, join

from elasticsearch import Elasticsearch

from src.text_processing import ImportantWordsExtractor
from src.transcription import OUTPUT_FOLDER


class ProcessingResult:
    def __init__(self, total_text, timestamps):
        self.total_text = total_text
        self.timestamps = timestamps


class WatsonResultProcessor:
    def __init__(self, result_json):
        self.initial_json = result_json

    def process(self):
        all_results = self.initial_json["results"]
        total_text = ""
        timestamps = []
        for fraze_analysis in all_results:
            alternatives = fraze_analysis["alternatives"][0]
            total_text += alternatives["transcript"]
            for timestamp in alternatives["timestamps"]:
                timestamps.append(timestamp)

        return ProcessingResult(total_text, timestamps)


class ESProcessor:
    def __init__(self):
        self.es = Elasticsearch([{'host': os.getenv("ES_HOST", 'localhost'),
                                  'port': int(os.getenv("ES_PORT", 9200))}])

    def insert(self, data, doc_type, index):
        self.es.index(index=index, doc_type=doc_type, body=data)


class TextEngine:

    def get_top_and_move_to_es(self):
        # 1. Get all text
        onlyfiles = [f for f in listdir(OUTPUT_FOLDER) if isfile(join(OUTPUT_FOLDER, f))]
        total_text = ""
        all_timestamps = []
        for file in onlyfiles:
            with open(os.path.join(OUTPUT_FOLDER, file)) as json_data:
                d = json.load(json_data)
                wrp = WatsonResultProcessor(d)
                processing_result = wrp.process()
                total_text += processing_result.total_text
                all_timestamps.extend(processing_result.timestamps)

        top_20 = ImportantWordsExtractor(total_text).get_top(20)
        data_for_es = []
        for words in all_timestamps:
            if words[0] in top_20:
                data_for_es.append({"start": words[1], "end": words[2], "word": words[0]})
        es = ESProcessor()
        for data in data_for_es:
            es.insert(data, doc_type="words", index="elon_and_joe")


def main():
    # esp = ESProcessor()
    TextEngine().get_top_and_move_to_es()

    # with open('output/part_1.txt') as json_data:
    #     d = json.load(json_data)
    #     wrp = WatsonResultProcessor(d)
    #     wrp.process()



if __name__ == '__main__':
    main()
