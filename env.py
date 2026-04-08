from typing import Dict
import random

class EmailEnv:
    def __init__(self):
        self.emails = [
            {"text": "Win money now!!!", "type": "spam"},
            {"text": "Meeting at 5pm", "type": "important"},
            {"text": "Job interview tomorrow", "type": "urgent"},
        ]
        self.current = None

    def reset(self):
        self.current = random.choice(self.emails)
        return {"email": self.current["text"]}

    def step(self, action: str):
        correct = self.current["type"]
        reward = 1.0 if action == correct else 0.0

        return {
            "observation": {"email": self.current["text"]},
            "reward": reward,
            "done": True,
            "info": {"correct": correct}
        }

    def state(self):
        return self.current