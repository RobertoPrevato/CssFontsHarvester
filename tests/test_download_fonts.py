import asyncio
import aiohttp
import unittest
from core.fetchfiles import download_fonts


class TestDownloadFonts(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.get_event_loop()

    def test_download_fonts(self):
        """Create account without confirmation by provider options, must return a confirmed account"""
        async def go():
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            }

            urls = [
                'https://fonts.gstatic.com/s/materialicons/v36/flUhRq6tzZclQEJ-Vdg-IuiaDsNc.woff2',
                'https://fonts.gstatic.com/s/roboto/v18/KFOlCnqEu92Fr1MmSU5fCRc4EsA.woff2'
            ]

            loop = asyncio.get_event_loop()
            async with aiohttp.ClientSession(loop=loop, headers=headers) as session:
                await download_fonts(urls, session)

        self.loop.run_until_complete(go())
