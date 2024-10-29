# 🟡 Multi Headed Self Attention

It's time to implement multi-headed self-attention. This layer is what makes LLMs so good at talking like real people. Check out this [video](https://www.youtube.com/watch?v=C3qrTe-iYvk) for an explanation of the concepts

Fortunately, this problem is a LOT easier than Self Attention. It's recommended to solve that problem first!

Your task is to code up the `MultiHeadedSelfAttention`class making use of the given `SingleHeadAttention` class. The forward method should return a `(batch_size, context_length, attention_dim)` tensor.

**Inputs:**

* `embedding_dim` - the input dimensionality where `embedding_dim > 0`.
* `attention_dim` - the output dimensionality where `attention_dim > 0`.
* `num_heads` - number of self-attention instances where `num_heads > 0` and `attention_dim % num_heads = 0`.
* `embedded` - the input to `forward()` where `embedded.shape = (batch_size, context_length, embedding_dim)`.

![](https://imagedelivery.net/CLfkmk9Wzy8\_9HRyug4EVA/1cd8c9dd-6700-4b1d-a6f1-b36064cbb200/sharpen=1)

> FC stands for Fully Connected or a Linear Layer in the diagram above.

```python
import torch
import torch.nn as nn
from torchtyping import TensorType

class MultiHeadedSelfAttention(nn.Module):
    
    def __init__(self, embedding_dim: int, attention_dim: int, num_heads: int):
        super().__init__()
        torch.manual_seed(0)
        # Hint: nn.ModuleList() will be useful. It works the same as a Python list
        # but is useful here since instance variables of any subclass of nn.Module
        # must also be subclasses of nn.Module

        # Use self.SingleHeadAttention(embedding_dim, head_size) to instantiate. You have to calculate head_size.
        # here attention_dim is the entire attention dim, i.e. num_heads x attention_dim_each_attentionhead
        
        self.heads = [self.SingleHeadAttention(embedding_dim, attention_dim//num_heads) for _ in range(num_heads)]

    def forward(self, embedded: TensorType[float]) -> TensorType[float]:
        # Return answer to 4 decimal places
        return torch.round(torch.cat([head(embedded) for head in self.heads], dim=-1), decimals=4)

        
    class SingleHeadAttention(nn.Module):
        def __init__(self, embedding_dim: int, attention_dim: int):
            super().__init__()
            torch.manual_seed(0)
            self.key_gen = nn.Linear(embedding_dim, attention_dim, bias=False)
            self.query_gen = nn.Linear(embedding_dim, attention_dim, bias=False)
            self.value_gen = nn.Linear(embedding_dim, attention_dim, bias=False)
        
        def forward(self, embedded: TensorType[float]) -> TensorType[float]:
            k = self.key_gen(embedded)
            q = self.query_gen(embedded)
            v = self.value_gen(embedded)

            scores = q @ torch.transpose(k, 1, 2) # @ is the same as torch.matmul()
            context_length, attention_dim = k.shape[1], k.shape[2]
            scores = scores / (attention_dim ** 0.5)

            lower_triangular = torch.tril(torch.ones(context_length, context_length))
            mask = lower_triangular == 0
            scores = scores.masked_fill(mask, float('-inf'))
            scores = nn.functional.softmax(scores, dim = 2)

            return scores @ v
```
