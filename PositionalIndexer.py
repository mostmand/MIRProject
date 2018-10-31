from os import listdir
from typing import Dict
from Index import Index
from PreProcess import PreProcessor
from Serialization import Serialization


def get_word_by_word(file_path: str) -> (str, str, int):
    files = listdir(file_path)

    for file in files:
        opened_file = open(file_path + '/' + file)

        position = 0

        for line in opened_file:
            words = line.split(' ')

            for word in words:
                yield (word, file, position)
                position += len(word) + 1


def combine_path(parent_directory: str, file_name: str) -> str:
    return parent_directory + '/' + file_name


class IdManager:
    ids_dic: Dict[str, int]
    first_available_id: int

    def __init__(self):
        self.ids_dic = {}
        self.first_available_id = 1

    def get_available_id(self) -> int:
        self.first_available_id += 1
        return self.first_available_id - 1

    def get_document_id(self, path: str) -> int:
        if path not in self.ids_dic:
            self.ids_dic[path] = self.get_available_id()
        return self.ids_dic[path]


class PositionalIndexer:
    def __init__(self):
        self.index_db = Index()
        self.preprocessor = PreProcessor()
        self.id_manager = IdManager()

    def index(self, files_parent_directory):
        for (word, file, position) in get_word_by_word(files_parent_directory):
            tokens = self.preprocessor.pre_process(word)
            path = combine_path(files_parent_directory, file)
            doc_id = self.id_manager.get_document_id(path)
            for token in tokens:
                self.index_db.index(token, doc_id, position)

    def save(self, compress: bool):
        ids_filename = 'Index/ids.mir'
        Serialization.write_ids(self.id_manager, ids_filename)
        index_filename = 'Index/index.mir'
        Serialization.write_to_file(self.index_db, index_filename, compress)

    def load(self, compress: bool):
        ids_filename = 'Index/ids.mir'
        self.id_manager = Serialization.load_ids(ids_filename)
        index_filename = 'Index/index.mir'
        self.index_db = Serialization.read_from_file(index_filename, compress)

    def search(self, query: str):
        for token in query.split(' '):
            for term in self.preprocessor.pre_process(token):
                posting_list = self.index_db.find(term)
                term_frequency = len(posting_list)
