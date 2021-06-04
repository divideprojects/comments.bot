from aiohttp import ClientSession


class AioHttp:
    """class for helping get the data from url using aiohttp."""

    @staticmethod
    async def post_json(link: str, **kwargs):
        """POST RAW data from the provided link."""
        async with ClientSession() as sess:
            async with sess.post(link, **kwargs) as resp:
                return await resp.json(), resp
