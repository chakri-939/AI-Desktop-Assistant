import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="write the importance of artificial intelligence\n\nArtificial Intelligence (AI) has become increasingly important in recent years. AI is critical for businesses, governments, and researchers to take advantage of advancements such as automation, robotics, machine learning, deep learning, natural language processing, and computer vision. AI plays a large role in transforming the way we interact with and think about the world, from improving healthcare and transportation to paving the way for self-driving cars and deep learning-driven digital assistants. AI can also help businesses to more accurately target and analyze their customers, provide better customer experiences, and improve their operations. The potential of AI is only just beginning to be explored and its applications have only started to be utilized, making it an exciting field to explore and be a part of.",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)


'''
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": ""
    }
  ],
  "created": 1685960741,
  "id": "cmpl-7O1h7e4TKK5jY6Z4HdymuCr1EK3j4",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "prompt_tokens": 155,
    "total_tokens": 155
  }
}'''