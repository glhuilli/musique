import json
import os
from typing import Iterable

import openai

from musique.utils.json_schema import JSON_SCHEMA
from musique.types import Song

openai.api_key = os.getenv("OPENAI_API_KEY")

_MODEL = 'gpt-3.5-turbo'


def ask_chatgpt(prompt: str) -> Iterable[Song]:
    """
    Return processed answer from chatGPT given a prompt
    """
    prompt_with_format = f'{prompt} in using the following json schema {JSON_SCHEMA}'
    response = openai.ChatCompletion.create(model=_MODEL,
                                            messages=[{
                                                "role":
                                                "user",
                                                "content":
                                                prompt_with_format
                                            }])
    return _parse_response(response)


def _parse_response(response) -> Iterable[Song]:
    """
    Process the OpenAIObject and returns the message content
    """
    content = response.choices[0].message.content
    return _get_songs(content)


def _get_songs(content: str) -> Iterable[Song]:
    """
    Retrieves all songs from ChatGPT content
    """
    songs = json.loads(content).get('songs')
    for song in songs:
        artist = song.get('artist')
        title = song.get('title')
        if artist and title:
            yield Song(artist=artist, title=title)
