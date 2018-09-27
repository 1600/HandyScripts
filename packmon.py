import os
import re
import shutil
from pprint import pprint

import requests
from lxml import html

fname = 'centos-packlist.html'

if not (os.path.isfile(fname) and os.path.getsize(fname) >= 10):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
        "Accept":
        "text/plain"
    }

    r = requests.get(
        "http://mirror.centos.org/centos-7/7/updates/x86_64/Packages/",
        headers=headers,
        stream=True)

    with open(fname, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

with open(fname, 'r') as f:
    page = f.read()

tree = html.fromstring(page)

# kernel-3.10.0-862.11.6.el7.x86_64.rpm
target = [i for i in tree.xpath('/html//a/@href') if re.match(r'kernel-3\.10\.0-.*el7.x86_64\.rpm',i)]
pprint(target)


def version_parser():
    pass