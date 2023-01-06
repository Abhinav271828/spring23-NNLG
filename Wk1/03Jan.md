---
title: Neural Network Language Generation (CL3.407)
subtitle: |
          | Spring 2023, IIIT Hyderabad
          | 03 January, Tuesday (Lecture 1)
author: Taught by Profs. Vasudev Varma and Manish Shrivastava
header-includes:
- \newfontfamily\devanagarifont{KohinoorDevanagari-Regular}
---

# Text Generation
## The Task
We may required text to be generated from any one of many sources – text, data (images/audio), graphs (knowledge bases) or tables, for instance.  
Any model we create to this end must be able to generate large amounts of text in a *grounded* manner, *i.e.*, without hallucinating.

Examples of tasks that require text to be generated from text include dialogue, style transfer, summarisation and translation.  
Data-to-text tasks include image captioning and visual storytelling.

## The Process
The generation process fundamentally has two functions – *control* (which affects the actual text being generated) and *grounding* (which affects its factuality/validity).

Control involves keeping track of all aspects of the output, like style, content, and structure.  
Grounding, in essence, is a fact-checking process. It is supported by an external resource that provides world knowledge against which to verify assertions, like a knowledge base or a domain-specific database.

The generation of the output is followed by *evaluation*, which is used to improve the generation process. At this stage, we must be careful of social biases entering into the evaluation, which can cause the model itself to have the same biases.

## Subtasks
The larger task of text generation includes a number of smaller subtasks. For instance,

* content determination
* document structuring
* lexicalisation (choice of words)
* referring expression generation (anaphora resolution$^-1$)

Generation as a whole can be approached in three ways:

* reconstitution of existing components (words/sentences) without understanding
* content determination $\to$ planning $\to$ generation
* "understanding" $\to$ planning $\to$ generation

The first two approaches are, in a sense, devoid of understanding – they work with language as an independent system. A neural model's only conception of meaning is *distributional* – it related to connections among words, rather than connections between words and concepts or entities.  
It has, however, been claimed that "a system trained on form has no a priori way to learn meaning."