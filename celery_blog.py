import requests
from celery import Celery

app = Celery('celery_blog', broker='redis://localhost:6379/0')


@app.task
def fetch_url(url):
    resp = requests.get(url)
    print str(resp.status_code) + ' (' + url + ')'


def func(urls):
    for url in urls:
        fetch_url.delay(url)


if __name__ == "__main__":
    func(["http://google.com", "https://amazon.in", "https://facebook.com", "https://twitter.com", "https://alexa.com"])

'''
Start three terminals
 - On first terminal, run redis using redis-server.
 - On second terminal, run celery worker using celery worker -A celery_blog -l info -c 5. By seeing the output, you will
 be able to tell that celery is running.
 - On third terminal, run your script, python celery_blog.py.
'''
