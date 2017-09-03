import boto3
import argparse
import os

"""
Script to write names of articles stored in S3 to a local text file for later use.

Usage:
------
python --bucket <bucket_name> --directory <bucket_subdirs>

Output:
-------
<bucket_subdir>/<article0_name>
<bucket_subdir>/<article1_name>
<bucket_subdir>/<article1_name>
...

>> article_names.txt
"""

s3 = boto3.client('s3')

def write_keys(list_of_keys):
    """
    Writes list of articles to 'articles_names.txt'

    Parameters:
    -----------
    list_of_keys : list, The article names.
    """
    if os.path.isfile('article_names.txt'):
        os.remove('article_names.txt')
    with open('article_names.txt', 'w') as f:
        for article in list_of_keys:
            f.write(article + '\n')

def get_list_of_articles(bckt, direct=False):
    """
    Pulls list of articles from S3 bucket.

    Parameters:
    -----------
    bckt : string, Name of S3 bucket.

    direct : string, Directory where articles are stored in S3, if multiple directories
             use '1st_directory/2nd_directory'
    """
    paginator = s3.get_paginator('list_objects')
    if direct:
        operation_parameters = {'Bucket': bckt,
                            'Prefix': direct + '/'}
    else:
        operation_parameters = {'Bucket': bucket}

    page_iterator = paginator.paginate(**operation_parameters)

    objs = []
    for page in page_iterator:
        for item in page["Contents"]:
            objs.append(item['Key'])
    return objs

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Module for creating a list of articles inside a bucket for later reference.')
    parser.add_argument('--bucket', help='Directory ')
    parser.add_argument('--directory', help='Directory inside the bucket that the articles are saved.')
    args = parser.parse_args()
    list_of_articles = get_list_of_articles(args.bucket, args.directory)
    write_keys(list_of_articles)
