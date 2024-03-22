import anthropic
import time
from anthropic import AI_PROMPT, HUMAN_PROMPT
from mindflow.utils import save_file, open_file

class Completions:
    MODEL_NAME = "claude-2.0"
    MAX_TOKENS_TO_SAMPLE = 2000

    def __init__(self):
        api_key = open_file("/Users/jameswinans/.anthropic_key")
        self.c = anthropic.AsyncAnthropic(api_key=api_key)

    def create(self, prompt, stream=False):
        save_file("api_logs/complete_%s.txt" % time(), prompt)
        response = self.c.completions.create(
            prompt=f"{prompt}{AI_PROMPT}",
            stop_sequences=[HUMAN_PROMPT],
            max_tokens_to_sample=self.MAX_TOKENS_TO_SAMPLE,
            model=self.MODEL_NAME,
            stream=stream,
        )
        return response