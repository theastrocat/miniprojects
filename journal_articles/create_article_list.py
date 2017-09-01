import boto3
import argparse

s3 = boto3.client('s3')

def write_keys(list_of_keys):
    with open('article_names.txt', 'w') as f:
        for article in list_of_keys:
            f.write(article + '\n')

def get_list_of_articles(bckt, direct=False):
    """

    """
    paginator = s3.get_paginator('list_objects')
    if direct:
        operation_parameters = {'Bucket': bckt,
                            'Prefix': direct + '/'}
    else:
        operation_parameters = {'Bucket': bucket,
                           'Prefix': direct + '/'}

    page_iterator = paginator.paginate(**operation_parameters)

    objs = []
    for page in page_iterator:
        for item in page["Contents"]:
            objs.append(item['Key'])
    write_keys(objs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Module for creating a list of articles inside a bucket for later reference.')
    parser.add_argument('--bucket', help='Directory ')
    parser.add_argument('--directory', help='Directory inside the bucket that the articles are saved.')
    args = parser.parse_args()
    get_list_of_articles(args.bucket, args.directory)
