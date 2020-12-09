import hashlib
import json

from DecoratorLogger import decorator_param_logger, decorator_simple_logger

if __name__ == '__main__':

    @decorator_simple_logger
    def jsonCountryReaderIter(json_filename: str):
        with open(json_filename, 'r', encoding='utf8') as file:
            countries = json.load(file)
            for country in countries:
                yield country['name']['common']

    @decorator_param_logger(filename='param_logger.txt')
    def textCountryReaderIter(text_filename: str):
        with open(text_filename, 'r', encoding='utf8') as file:
            for line in file:
                yield hashlib.md5(line.encode()).hexdigest()


    with open('countries.txt', 'w', encoding='utf8') as countries_file:
        print(f'Parsing json to {countries_file.name}')
        for country in jsonCountryReaderIter('countries.json'):
            countries_file.write(f'{country}\n')

    with open('hashes.txt', 'w', encoding='utf8') as hash_file:
        print(f'Making hashes at {hash_file.name}')
        for country in textCountryReaderIter('countries.txt'):
            hash_file.write(f'{country}\n')

    print('Finished! Please check param_logger.txt and simple_log.txt')
