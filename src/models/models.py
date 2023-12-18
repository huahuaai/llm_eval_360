from typing import Any
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from templates import get_template
# from peft import PeftModel

#first complete the version without accelerte
class LLM():
    def __init__(
        self,
        args
    ):
        self.llm = AutoModelForCausalLM.from_pretrained(
            model_name_or_path=args.model_name_or_path,
            device_map=args.device_map,
            load_in_4bit=args.load_in_4bit,
            load_in_8bit=args.load_in_8bit
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name_or_path=args.model_name_or_path,
            
        )
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def generate_text(self):
        x=0
    def decode_token_to_text(self, input):
        return self.tokenizer.decode(input, skip_special_tokens=True).strip()
    
    def tokenize_text_to_token(self, input):
        return self.tokenizer(input)

    def get_prompt(self):
        x=0