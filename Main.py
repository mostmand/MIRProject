from PositionalIndexer import PositionalIndexer

persian_files_path = 'Files/PersianData/'
english_files_path = 'Files/EnglishData'

positional_indexer = PositionalIndexer()


def index_persian_documents():
    print('Indexing Persian files...')
    positional_indexer.index(persian_files_path)
    print('done!!!')


def get_input_from_user():
    user_input = input('Enter the specified number for the option you want:\n'
                       '1.Index Persian documents\n'
                       '2.Index English documents\n'
                       '3.Search\n'
                       '4.Save\n'
                       '5.Load\n'
                       '0.Exit\n')

    exit_requested = False
    if user_input == '0':
        exit_requested = True
    if user_input == '1':
        index_persian_documents()
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        compress = input('Do you want to save in compressed format?\n'
                         '1.Yes\n'
                         '2.No\n')
        if compress == '1':
            positional_indexer.save(True)
        elif compress == '2':
            positional_indexer.save(False)
        else:
            print('Command not recognized.')
    elif user_input == '5':
        compress = input('Is the saved file in compressed format?\n'
                         '1.Yes\n'
                         '2.No\n')
        if compress == '1':
            positional_indexer.load(True)
        elif compress == '2':
            positional_indexer.load(False)
        else:
            print('Command not recognized.')
    else:
        print('Command not recognized')

    return exit_requested


while True:
    exit_requested = get_input_from_user()
    if exit_requested:
        break
