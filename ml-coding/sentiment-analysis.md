# Sentiment Analysis

Your task is to implement a neural network that can recognize positive or negative emotion in an input sentence. This application of work embeddings is the first step in building ChatGPT. To learn more about word embeddings, check out this [video](https://www.youtube.com/watch?v=8dRLaVOlTYA).

_The background video is critical to completely understanding the ML concepts involved in this problem._

For the model architecture, first use an embedding layer of size 16. Compute the average of the embeddings to remove the time dimension, and end with a single-neuron linear layer followed by a sigmoid. The averaging is called the "Bag of Words" model in NLP.

Implement the constructor and `forward()` pass that outputs the model's prediction as a number between 0 and 1 (completely negative vs. completely positive). Do _not_ train the model.

**Inputs:**

* `vocabulary_size` - the number of different words the model should be able to recognize
* `x` - a list of strings, each with negative emotion
