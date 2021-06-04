# Comments.bot

<p align="center">
<a href="https://pypi.org/project/comments.bot/"><img src="https://img.shields.io/pypi/v/comments.bot" alt="PyPI"></a>
<a href="https://pypi.org/project/comments.bot/"><img src="https://img.shields.io/pypi/pyversions/comments.bot.svg" alt="Supported Python Versions"></a>
<a href="https://pepy.tech/project/comments.bot"><img src="https://pepy.tech/badge/comments.bot" alt="Downloads"></a>
</p>

A simple API wrapper to interact with [comments.bot](https://comments.bot) api.


## Installation

The latest version of comments.bot is available via `pip`:

```shell
pip install --upgrade comments.bot
```

Also, you can download the source code and install using:

```shell
poetry install
```

**Note:** You need to have [poetry](https://python-poetry.org/) installed on your system

## Usage

The library can be used in both Sync and Async!
For both there are 2 client which can be imported from comments_bot - SyncClient, AsyncClient.

```python3
from comments_bot import SyncClient, AsyncClient
from asyncio import run

asyncClient = AsyncClient(api_key="some api key", owner_id=12345678)  # Async Client
syncClient = SyncClient(api_key="some api key", owner_id=12345678)  # Sync Client

# Both of the clients have same function - createPost, editPost, deletePost
post_text_id, link_text = syncClient.createPost(text="hey")  # Post a text message
post_photo_id, link_photo = syncClient.createPost(type="photo", photo_url="some url", caption="some text for caption")  # Post a photo

status, post_text_id = syncClient.editPost(post_id=post_text_id, text="some other message")

status = syncClient.deletePost(post_id=post_id)  # Deletes the post from comments.bot
```

You can use the below methods for both SyncClient and AsyncClient.

## Methods Available:

### createPost() arguments:

- owner_id:
  - required if not passed on Client.

- type:
  - must be `text` or `photo`. `text` is used by default if not specified.

- text:
  - required if `type` equals to `text`. It must be a string betwen 0-4056 characters.

- photo_url:
  - required if `type` equals to `photo`. It must be a string containing a link to the image.

- caption:
  - Caption for the image. Only valid for `photo` type.

- parse_mode:
  - Parse mode for the text/caption. It must be `markdown` or `html`.

- administrators:
  - A string with user_ids (numbers) separated by comma. Example: `123456789,987654321,012345678`.

- disable_notifications:
  - Pass True if you don't want to receive notifications about new comments for your post.

### editPost() arguments:

- type:
  - must be `text` or `photo`. `text` is used by default if not specified.

- text:
  - required if `type` equals to `text`. It must be a string betwen 0-4056 characters.

- photo_url:
  - required if `type` equals to `photo`. It must be a string containing a link to the image.

- caption:
  - Caption for the image. Only valid for `photo` type.

- parse_mode:
  - Parse mode for the text/caption. It must be `markdown` or `html`.

### deletePost() arguments:

- post_id:
  - Pass the post id to be deleted


## Contribuiting

Wanna help and improve this project?

Make sure to follow these before opening a PR:

- Make sure your PR passes the test and is formatted according to pre-commit.
- Make sure the package is working without any issues!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
