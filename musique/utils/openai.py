import os
from typing import Any, Dict, List
import json

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

_MODEL = "text-davinci-003"
_TEMPERATURE = 0.7
_MAX_TOKENS = 60
_TOP_P = 1.0
_FREQUENCY_PENALTY = 0.0
_PRESENCE_PENALTY = 1


def ask_chatgpt(prompt: str) -> Dict[str, Any]:
    """
    Return processed answer from chatGPT given a prompt
    """
    response = openai.Completion.create(
      model=_MODEL,
      prompt=prompt,
      temperature=_TEMPERATURE,
      max_tokens=_MAX_TOKENS,
      top_p=_TOP_P,
      frequency_penalty=_FREQUENCY_PENALTY,
      presence_penalty=_PRESENCE_PENALTY
    )
    return _parse_response(response)


def _parse_response(response) -> List[str]:
    """
    TODO
    {
      "choices": [
        {
          "finish_reason": "stop",
          "index": 0,
          "logprobs": null,
          "text": "\n\nThis is indeed a test!"
        }
      ],
      "created": 1682843554,
      "id": "cmpl-7AwludjmaCwpALLbEt0iOoBzbCyDN",
      "model": "text-davinci-003",
      "object": "text_completion",
      "usage": {
        "completion_tokens": 8,
        "prompt_tokens": 6,
        "total_tokens": 14
      }
    }
    """
    # data = json.load(response)
    # print(type(response))
    # print(response)

    return [x.text for x in response.choices]
