import requests as req
import time
import numpy as np
import boto3
import os

if __name__ == '__main__':
    s3 = boto3.client("s3")
    with open("bucket_source.txt", 'r') as f:
        info = f.read().split()
    bucket = info[0]
    article_source = info[1]
    n1 = 1002
    broken = False
    articles = 0
    while n1 < 2000:
        n2 = 0
        errors = 0
        while not errors > 10:
            r = np.random.randint(-2,2)
            n2 += 1
            ind = '%04d' % n2
            tag = "{}.{}".format(n1, ind)

            article_get = req.get("{}{}.pdf".format(article_source, tag))

            if article_get.status_code == 200:
                name = '{}'.format(tag + '.pdf')
                with open(name, 'w') as f:
                    f.write(article_get.content)
                    articles += 1
                s3.upload_file(name, bucket, 'articles/{}'.format(name))
                os.remove(name)
                print "Saved {} articles.".format(articles)

            elif article_get.status_code != 200:
                errors += 1
                print "{} error.".format(errors)
            time.sleep(10 + r)
        n2 += 1
