import os

os.system('echo "1" | appcfg.py --application=dev~tuiliclub upload_data --email=dev@localhost.com --passin --config_file=bulkloader.yaml --filename=../data/articles.csv --batch_size=50 --log_file=/dev/null --kind=Item --url=http://localhost:8080/remote_api .')
os.system('echo "1" | appcfg.py --application=dev~tuiliclub upload_data --email=dev@localhost.com --passin --config_file=bulkloader.yaml --filename=../data/users.csv --batch_size=50 --log_file=/dev/null --kind=User --url=http://localhost:8080/remote_api .')
os.system('echo "1" | appcfg.py --application=dev~tuiliclub upload_data --email=dev@localhost.com --passin --config_file=bulkloader.yaml --filename=../data/status.csv --batch_size=50 --log_file=/dev/null --kind=Status --url=http://localhost:8080/remote_api .')
os.system('echo "1" | appcfg.py --application=dev~tuiliclub upload_data --email=dev@localhost.com --passin --config_file=bulkloader.yaml --filename=../data/reviews.csv --batch_size=50 --log_file=/dev/null --kind=Review --url=http://localhost:8080/remote_api .')
os.system('echo "1" | appcfg.py --application=dev~tuiliclub upload_data --email=dev@localhost.com --passin --config_file=bulkloader.yaml --filename=../data/tags.csv --batch_size=50 --log_file=/dev/null --kind=Tag --url=http://localhost:8080/remote_api .')
os.system('echo "1" | appcfg.py --application=dev~tuiliclub upload_data --email=dev@localhost.com --passin --config_file=bulkloader_book.yaml --filename=../data/books_dev.csv --batch_size=50 --log_file=/dev/null --kind=Item --url=http://localhost:8080/remote_api .')
