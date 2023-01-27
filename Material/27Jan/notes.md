# Liu+ '21 (Pre-train, Prompt and Predict – A Systematic Survey of Prompting Methods in Natural Language Processing)
* Abstract: survey of "prompt-based learning", which enables few-/zero-shot learning

## Two Sea Changes in NLP
* fully supervised learning has been central
    * early models used feature engg
    * NNs shifted to architecture engg
* 2017-19: pre-train and finetune
    * model is pretrained as LM
    * LM adapted by adding params and finetuning
    * now "objective engg"
* 2021: pre-train, prompt, predict
    * tasks reformulated as LM
    * unsupervised LM can be versatile
    * "prompt engg"

## A Formal Description of Prompting
### Supervised Learning in NLP
* $P(y \mid x, \theta)$.

### Prompting Basics
* prompt addition: template with two slots; fill input
    * cloze (answer in middle); prefix (answer at end)

* answer search: look for z to maximise LM score

* answer mapping: get answer from LM output

### Design Considerations
* model choice
* prompt engineering
* answer engineering
* expanding paradigm
* training strategies

## Pre-trained LMs
### Training Objective
* standard LM (SLM)
    * predict P(x); autoregressive
* corrupted text reconstruction (CTR)
    * loss over noised parts
* full text reconstruction (FTR)

### Noising Functions
* masking
* replacement
* deletion
* permutation (of spans)

### Directionality of Representation
* left-to-right
* bidirectional

### Typical Pre-training Methods
* left-to-right LMs
* masked LMs
* prefix and encoder-decoder
* prefix LM
* encoder-decoder

## Prompt Engg
### Prompt Shape
* cloze
* prefix

### Manual Template Engg

### Automated Template Learning
* static/dynamic
* discrete/continuous
    * discrete
        * prompt mining
        * prompt paraphrasing
        * gradient-based search
        * prompt generation
        * prompt scoring
    * continuous
        * prefix tuning
        * tuning initialised w discrete prompts
        * hard-soft prompt hybrid tuning

## Answer Engg
### Answer Shape
* tokens
* span (cloze)
* sentence (prefix)

### Answer Space Design Methods
* manual design
    * unconstrained spaces: all tokens, fixed-length spans, etc.
    * constrained spaces: need mapping
* discrete answer search
    * answer paraphrasing
    * prune-then-search
    * label decomposition
* continuous answer search

## Multi-prompt Learning
### Prompt Ensembling
* uniform averaging
* weighted averaging
* majority voting
* knowledge distillation
* prompt ensembling for text generation

### Prompt Augmentation
* sample selection
* sample ordering

### Prompt Composition

### Prompt Decomposition

## Training Strategies for Prompting Methods
### Training Settings
* zero-shot
* full-data
* few-shot

### Parameter Update Methods
* promptless finetuning
* tuning-free prompting
* fixed-LM prompt tuning
* fixed-prompt LM tuning
* prompt+LM tuning

## Applications
### Knowledge Probing
* factual probing: how much info in reps (cloze)
* linguistic probing: analogy, negn, etc.

### Classification-Based Tasks
* text classification: cloze, prompt/answer engg
* NLI

### Information Extraction
* relation extraction
* semantic parsing
* NER

### Reasoning in NLP
* commonsense reasoning
* mathematical reasoning

### Question Answering
* extractive/MCQ/free-form

### Text Generation
* prefix prompts
* in-context learning

### Automatic Evaluation of Text Generation

### Multi-modal Learning

### Meta-Applications
* domain adaptation
* debiasing
* dataset construction

### Resources

## Prompt-relevant Topics
* ensemble learning
    * multiple systems
* few-shot learning
* larger-context learning
* query reformulation
* QA-based task formulation
* controlled generation
* supervised attention
* data augmentation

## Challenges
### Prompt Design
* tasks beyond classification and generation
* prompting with structured information
* entanglement of template and answer

### Answer Engineering
* many-class and long-answer classification tasks
* multiple answers

### Selection of Tuning Strategy

### Multiple Prompt Learning
* prompt ensembling
    * space/time complexity
    * prompt selection
* prompt composition and decomposition
* prompt augmentation
    * input length
    * order
* prompt sharing

### Selection of Pre-trained Model

### Theoretical and Empirical Analysis of Prompting

### Transferability of Prompts

### Combination of Different Paradigms

### Calibration of Prompting Methods
* models are not well calibrated
* sensitive to last input

## Meta Analysis
### Timeline

### Trend Analysis
* year
* tasks
* prompt vs answer search
* discrete vs. continuous search

## Conclusion
* promising new paradigm

# Li+ '21 (Prefix-Tuning – Optimising Continuous Prompts for Generation)
* Abstract: optimise continuous task-specific vector

* train sequence of continuous task-specific vectors
    * "virtual tokens"
* LM remains unmodified
    * allows personalisation

* prefix-tuning: proper context can steer LM
* but NL context fails
* train continuous vector
* can reduce parameter space by reparametrising with MLP

results
* table-to-text generation: better
* summarisation: lower than FT
* low-data setting: better
* extrapolation: comparable to adapter-tuning

intrinsic evaluation
* prefix length: increases
* full vs embedding-only: full better
* prefixing vs infixing: pre > in
* initialisation: better with real words

discussion
* personalisation: user privacy
* batching across users
* inductive bias