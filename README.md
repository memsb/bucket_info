# S3 Bucket Info

Manually exploring S3 bucket contents will show you lots of the details, but a high level summary can sometimes be what you need.
Built using Python, Boto, Numpy and Matplotlib

memsb-lambda-source
![memsb-lambda-source](https://github.com/memsb/bucket_info/blob/main/output/memsb-lambda-source.png?raw=true)

buckleytech.co.uk
![buckleytech.co.uk](https://github.com/memsb/bucket_info/blob/main/output/buckleytech.co.uk.png?raw=true)

martin-laura.com
![martin-laura.com](https://github.com/memsb/bucket_info/blob/main/output/martin-laura.com.png?raw=true)

lcmillsconsulting.com
![lcmillsconsulting.com](https://github.com/memsb/bucket_info/blob/main/output/lcmillsconsulting.com.png?raw=true)

## Installation 
```commandline
cd bucket_info
pipenv install
```

## Running 

Listing your buckets
```commandline
pipenv run python list_buckets.py
```

Getting Summary of bucket stats
```commandline
pipenv run python bucket_info.py martin-laura.com.png
```

Getting summary of prefix
```commandline
pipenv run python bucket_info.py martin-laura.com.png assets/
```