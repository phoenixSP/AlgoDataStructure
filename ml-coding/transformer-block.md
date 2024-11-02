# Transformer Block

It's finally time to code up the `TransformerBlock` class. This is the most important class to write in defining the GPT model. It is the gray rectangular box repeated “Nx” times, and it is a giant neural network that uses Multi Headed Attention, among other neural network layers that are given in the starter code.

Note that you should ignore the multi-headed attention and add & norm that comes right before the feedforward block for LLMs. Check out this [video](https://www.youtube.com/watch?v=V3-SD68CWWg) for a full explanation.

Your `forward()` method should return a `(batch_size, context_length, model_dim)` tensor.

Your `forward()` method should return a `(batch_size, context_length, model_dim)` tensor.

![](https://imagedelivery.net/CLfkmk9Wzy8\_9HRyug4EVA/c8de1893-4ee5-4bd4-22e6-e64131c8f100/sharpen=1)

**Inputs:**

* `model_dim` - the dimension for embeddings and attention, the same number is often used for both. `model_dim > 0`.
* `num_heads` - the number of self-attention instances. `num_heads > 0` and `model_dim % num_heads = 0`.
* `embedded` - the input to `forward()`. `embedded.shape = (batch_size, context_length, model_dim)`.
