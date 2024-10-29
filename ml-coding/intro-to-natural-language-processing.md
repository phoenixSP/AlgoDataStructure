# 🟡 Intro to Natural Language Processing

In this problem, you will load in a raw body of text and set it up for training. ChatGPT uses the entire text of the internet for training, but in this problem we will use Amazon product reviews and Tweets from X.

Your task is to encode the input dataset of strings as an integer tensor of size 2⋅N×T2⋅N×T, where TT is the length of the longest string. The lexicographically first word should be represented as **1**, the second should be **2**, and so on. In the final tensor, list the positive encodings, in order, before the negative encodings.&#x20;

**Inputs:**

* `positive` - a list of strings, each with positive emotion
* `negative` - a list of strings, each with negative emotion

```python
import torch
import torch.nn as nn
from torchtyping import TensorType

# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        
        combined = positive + negative
        vocab = set([word for sentence in combined for word in sentence.split()])
        vocab = sorted(vocab)
        vocab = {word: i+1 for i, word in enumerate(vocab)}

        res = []
        for sentence in combined: 
            res.append(torch.tensor([vocab[word] for word in sentence.split()]))

        res = torch.nn.utils.rnn.pad_sequence(res, batch_first=True)
        return res
```
