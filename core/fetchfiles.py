import asyncio
import os
import re
import ntpath
from os import path
import errno


css_url_rx = re.compile('url\(([^)]+)\)')


def ensure_folder(p):
    """
    Makes sure that a folder exists. If it doesn't, it creates it.

    :param p: folder to be ensured.
    """
    try:
        os.makedirs(p)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def get_url_links_from_css(text):
    return css_url_rx.findall(text)


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def get_last_leaf(url):
    if '/' in url:
        return url[url.rindex('/') + 1:]
    return url


sema = asyncio.BoundedSemaphore(100)


def create_new_css(source_file_path, text, urls):
    new_text = text

    for url in urls:
        new_text = new_text.replace(url, f'/fonts/{get_last_leaf(url)}')

    file_name = path_leaf(source_file_path)
    destination_path = path.join('out', file_name)

    with open(destination_path, mode='wt') as destination_file:
        destination_file.write(new_text)


async def process_file(url, session):
    file_name = get_last_leaf(url)
    file_path = path.join('out', file_name)

    if os.path.isfile(file_path):
        print('[*] Skipping because it exists: ', file_name)
        return

    print('[*] Downloading: ', file_name)

    with await sema:
        with open(file_path, 'wb') as f:
            async with session.get(url) as resp:
                b = await resp.read()
                f.write(b)


async def download_fonts(urls, session):
    await asyncio.wait([process_file(a, session) for a in urls])


async def harvest_fonts(source_file_path, session):
    if not source_file_path:
        raise ValueError('missing file source path')
    if not session:
        raise ValueError('missing http client session')

    ensure_folder('out')

    with open(source_file_path, mode='rt') as source_file:
        text = source_file.read()

    urls = get_url_links_from_css(text)

    if len(urls) > 0:
        await download_fonts(urls, session)
    else:
        'No url found in source file'

    print('[*] Generating new css:')
    create_new_css(source_file_path, text, urls)