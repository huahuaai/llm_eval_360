from typing import Any
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from templates import get_template

#first complete the version without accelerte
class LLM():
    def __init__(
        self,
        model_name_or_path: str,
        use_accelerate: bool=False,
        device_map: str='auto',
        load_in_8bit: bool=False,
        load_in_4bit: bool=False
    ):
        self.model = self.create_model(

        )

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name_or_path,
            device_map=device_map,
            load_in_4bit=load_in_4bit,
            load_in_8bit=load_in_8bit
        )
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def generate_oneturn(self):
        x=0
    def decode_token_to_text(self):
        x=0
    def tokenize_text_to_token(self):
        x=0
    def get_prompt(self):
        x=0
    def create_model(self):
        x=0
    