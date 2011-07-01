import os

os.system('appcfg.py upload_data --application=s~tuiliclub --config_file=bulkloader.yaml --filename=../data/articles.csv --batch_size=10 --log_file=/dev/null --kind=Item --url=http://tuiliclub.appspot.com/remote_api .')
os.system('appcfg.py upload_data --application=s~tuiliclub --config_file=bulkloader.yaml --filename=../data/users.csv --batch_size=10 --log_file=/dev/null --kind=User --url=http://tuiliclub.appspot.com/remote_api .')
os.system('appcfg.py upload_data --application=s~tuiliclub --config_file=bulkloader.yaml --filename=../data/status.csv --batch_size=10 --log_file=/dev/null --kind=Status --url=http://tuiliclub.appspot.com/remote_api .')
os.system('appcfg.py upload_data --application=s~tuiliclub --config_file=bulkloader.yaml --filename=../data/reviews.csv --batch_size=10 --log_file=/dev/null --kind=Review --url=http://tuiliclub.appspot.com/remote_api .')
#os.system('appcfg.py upload_data --application=s~tuiliclub --config_file=bulkloader_book.yaml --filename=../data/books.csv --batch_size=10 --log_file=/dev/null --kind=Item --url=http://tuiliclub.appspot.com/remote_api .')
