import math
import numpy as np
import random
import sklearn.metrics
import evaluate
import logging
eval_logger = logging.getLogger("llm_eval_360")

def metric_decorator(metric_dict):
    def decorator(fn):
        metric_name = fn.__name__
        metric_dict[metric_name] = fn
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        
        return wrapper
    return decorator
metrics = {}
register_metric = metric_decorator(metrics)


@register_metric
def acc():
    x=0

@register_metric
def f1_score_text():
    x=0

@register_metric
def exact_match():
    x=0


@register_metric
def bleu():
    x=0
