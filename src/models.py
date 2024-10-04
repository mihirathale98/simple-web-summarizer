from together import Together
from openai import OpenAI
from anthropic import Anthropic


class TogetherModel:
    def __init__(self):
        self.together_client = Together()


    def generate(self, prompt, model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"):
        completion = self.together_client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                )
        return completion.choices[0].message.content


class OpenAIModel:
    def __init__(self):
        self.openai_client = OpenAI()


    def generate(self, prompt, model="gpt-3.5-turbo"):
        completion = self.openai_client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                )
        return completion.choices[0].message.content


class AnthropicModel:
    def __init__(self):
        self.anthropic_client = Anthropic()

    def generate(self, prompt, model="claude-v1.3-100k"):
        completion = self.anthropic_client.completion(
                prompt=prompt,
                model=model,
                )
        return completion
