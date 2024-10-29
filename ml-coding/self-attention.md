# 🔴 Self Attention

We're finally ready to code up self-attention. This is the main part of Transformers like ChatGPT. Check out this [video](https://www.youtube.com/watch?v=6rnRvrvjYUg) for an explanation of the concepts.

_The background video is critical to completely understanding the ML concepts involved in this problem. It is a bit lengthy, but is worth the time investment. This problem teaches you, at the lowest level, how LLMs read like humans and focus on what's important. This is definitely the hardest problem in the series._

The class which will be used as a layer in the GPT class just like `nn.Linear()`. `Forward()` should return a `(batch_size, context_length, attention_dim)`tensor.

**Inputs:**

* `embedding_dim` - the input dimensionality where `embedding_dim > 0`.
* `attention_dim` - the head size where `attention_dim > 0`.
* `embedded` - the input to `forward()`. `embedded_shape = (batch_size, context_length, embedding_dim)`. This tuple format is PyTorch convention for 3-D.

![](https://imagedelivery.net/CLfkmk9Wzy8\_9HRyug4EVA/340c4c5c-0707-4487-5abd-e8abb4540c00/sharpen=1)

**Example 1:**

```java
Input:
embedding_dim = 2
attention_dim = 3
embedded = [
  [[-1.4381, 0.1232],
   [-0.1080, 0.3458]],
  [[0.1929, -0.8567],
   [-0.1160, 1.2547]]
]


Output:[
  [[-0.9737, 0.4302, -0.4216],
   [-2.4031, 1.4092, 1.3797]],
  [[ 1.7862, -2.1856, 0.2375],
   [-0.7592, -0.1953, -0.4658]]
]
```

Note: This example is to help you understand the shape of the output. We can infer batch\_size = 2 and context\_length = 2 for this example.

**Intuition:**

![](https://imagedelivery.net/CLfkmk9Wzy8\_9HRyug4EVA/04ed32e4-5c82-4def-ceff-8f4773cd9e00/sharpen=1)

The above image shows the intermediate `context_length * context_length`tensor with attention affinities. Notice that the row for '?' and the column for ‘How’ is high, with a score of 73. This indicates that this pair of tokens is important for understanding the meaning of the input. The fact that the 'How' is strongly associated with the '?' helps the model learn that 'How' is being used to ask a question, rather than describe something, i.e. “That's **how** that works”

```python
import torch
import torch.nn as nn
from torchtyping import TensorType

class SingleHeadAttention(nn.Module):
    
    def __init__(self, embedding_dim: int, attention_dim: int):
        super().__init__()
        torch.manual_seed(0)
        self.w_k = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.w_q = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.w_v = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.d_k = attention_dim
        self.softmax = nn.Softmax(dim=-1)
    
    def forward(self, embedded: TensorType[float]) -> TensorType[float]:
        key = self.w_k(embedded)
        query = self.w_q(embedded)
        value = self.w_v(embedded)

        attention_scores = query @ torch.transpose(key, 1, 2) # @ is the same as torch.matmul()
        context_length = key.shape[-2]
        lower_triangular = torch.tril(torch.ones(context_length, context_length))
        mask = lower_triangular == 0
        attention_scores = attention_scores.masked_fill(mask, float('-inf'))
        attention_weights = self.softmax(attention_scores/(self.d_k ** 0.5))

        return torch.round(attention_weights @ value, decimals=4)
```
