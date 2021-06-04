from json import dumps

from ._utils import AioHttp
from .errors import CommentsError

headers = {"Content-Type": "application/json"}


class AsyncClient:
    def __init__(self, api_key, owner_id=None):
        self.api_key = api_key
        self.owner_id = owner_id

    async def createPost(
        self,
        owner_id=None,
        type="text",
        text=None,
        photo_url=None,
        caption=None,
        parse_mode=None,
        administrators=None,
        disable_notifications=None,
    ):
        owner_id = owner_id or self.owner_id
        value_dict = {
            "text": {
                "api_key": self.api_key,
                "owner_id": owner_id,
                "type": type,
                "text": text,
                "parse_mode": parse_mode,
                "administrators": administrators,
            },
            "photo": {
                "api_key": self.api_key,
                "owner_id": owner_id,
                "type": type,
                "photo_url": photo_url,
                "caption": caption,
                "parse_mode": parse_mode,
                "administrators": administrators,
                "disable_notifications": disable_notifications,
            },
        }

        if type.lower() in ("text", "photo"):
            data = value_dict[type.lower()]
        else:
            raise ValueError("Unsupported type '%s'" % type)

        # Clear None values from dict to avoid API errors
        data = {x: y for x, y in data.items() if y is not None}
        json_, _ = await AioHttp.post_json(
            "https://api.comments.bot/createPost",
            headers=headers,
            data=dumps(data),
        )
        if not json_["ok"]:
            raise CommentsError(json_["error"])

        return json_["result"]["post_id"], json_["result"]["link"]

    async def editPost(
        self,
        post_id,
        text=None,
        photo_url=None,
        caption=None,
        parse_mode=None,
    ):
        data = {
            "api_key": self.api_key,
            "post_id": post_id,
            "text": text,
            "photo_url": photo_url,
            "caption": caption,
            "parse_mode": parse_mode,
        }

        # Clear None values from dict to avoid API errors
        data = {x: y for x, y in data.items() if y is not None}
        json_, _ = await AioHttp.post_json(
            "https://api.comments.bot/editPost",
            headers=headers,
            data=dumps(data),
        )
        return json_["ok"]

    async def deletePost(self, post_id):
        data = {"api_key": self.api_key, "post_id": post_id}
        json_, _ = await AioHttp.post_json(
            "https://api.comments.bot/deletePost",
            headers=headers,
            data=dumps(data),
        )
        return json_["ok"]
