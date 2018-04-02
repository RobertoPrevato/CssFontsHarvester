"""
 * CssFontsHarvester 1.0.0 Python font files bulk downloader
 * https://github.com/RobertoPrevato/CssFontsHarvester
 *
 * Copyright 2018, Roberto Prevato
 * https://robertoprevato.github.io
 *
 * Licensed under the MIT license:
 * http://www.opensource.org/licenses/MIT
"""
import sys
is_less_than_35 = sys.version_info <= (3, 5)

separator = "===========================================================\n"

banner = """
===========================================================
  CssFontsHarvester | fonts bulk downloader.             
  Written by Roberto Prevato <roberto.prevato@gmail.com>   
==========================================================="""


def sep_print(message):
    print("[*]")
    print("[*] " + message)
    print("[*]")


if is_less_than_35:
    print(banner)
    sep_print("CssFontsHarvester requires Python 3.5 or greater")
    sys.exit(1)


import argparse


parser = argparse.ArgumentParser(description="CssFontsHarvester | fonts bulk downloader",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog="{}\n{}".format("author: Roberto Prevato roberto.prevato@gmail.com", separator))

parser.add_argument("-s", "--source", dest="source", required=True,
                    help="source file with http links")

options = parser.parse_args()

import asyncio
import aiohttp
from core.fetchfiles import harvest_fonts


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()

        async def go():
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            }

            loop = asyncio.get_event_loop()
            async with aiohttp.ClientSession(loop=loop, headers=headers) as session:
                await harvest_fonts(options.source, session)

        loop.run_until_complete(go())

    except FileNotFoundError:
        sep_print("Error: file not found")

    except RuntimeError as re:
        sep_print("Runtime Error: " + str(re))

    except KeyboardInterrupt:
        sep_print("User interrupted...")