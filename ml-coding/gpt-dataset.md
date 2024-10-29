# 🟡 GPT Dataset

Before we can train a transformer like GPT, we need to define the dataset. We take a giant body of text and we can create examples for the model to predict the next token based on different contexts. This is what “ChatGPT was trained on the entire internet” means.

Your task is to write the `batch_loader()` function which will generate a `batch_size * context_length` dataset and its labels. Use `torch.randint()` to pick `batch_size` different starting words for each sequence.

**Inputs:**

* `raw_dataset` - a body of text. `len(raw_dataset) > 0`.
* `context_length` - how many tokens back the model can read. `context_length > 0`.
* `batch_size` - how many sequences to generate. `batch_size > 0`.

Return the input dataset `X` and the labels `Y`. `len(X) = len(Y)`.

```python
import torch
from typing import List, Tuple

class Solution:
    def batch_loader(self, raw_dataset: str, context_length: int, batch_size: int) -> Tuple[List[List[str]]]:
        # You must start by generating batch_size different random indices in the appropriate range
        # using a single call to torch.randint()
        torch.manual_seed(0)
        
        dataset = raw_dataset.split()
        max_size = len(dataset)
        X = []
        Y = []
        indices = torch.randint(high=max_size-context_length, size=(batch_size,))
        for idx in indices:
            X.append(dataset[idx: idx + context_length])
            Y.append(dataset[idx+1: idx + context_length+1])

        return X, Y
```
