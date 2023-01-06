# Lecture 2
## Reiter & Dale '97 (Building Applied Natural Language Generation Systems)
### Introduction
* NLG is a subfield of AI+CL
    * Systems to produce understandable texts in NLs
    * from non-linguistic information source
* Here: applications, tasks, algorithms, knowledge aggregation

### Using NLG
* Applications
    * present data in easily understandable way
    * authoring aids

### Requirements Analysis and System Specification
* Corpus-based approach 
    * get initial corpus
    * make target corpus
    * analyse information

### The Architecture and Components of an NLG System
* Tasks
    * content determination: messages
    * discourse planning: order of messages
    * sentence aggregation: grouping messages
    * lexicalisation: selecting words
    * referring expression generation
    * linguistic realisation: grammar, spelling
* Architecture
    * text planning: 1, 2
    * sentence planning: 3, 4, 5
    * linguistic realisation
* Intermediate reps
    * text plans: trees
    * sentence plans
        * templates
        * abstract representations

### Text Planning
* content determination
    * plan recognition (reasoning)
    * domain-specific (corpus analysis)
* discourse planning
    * RST
    * planning-based approach
    * schema-based approach

### Sentence Planning
* sentence aggregation
    * conjunction, ellipsis, set formation, embedding
    * rules
* lexicalisation
    * graph-to-graph
* referring expression generation
    * initial introduction, pronouns, definite descriptions

### Linguistic Realisation
* inverse of parsing
    * bidirectional grammars
* systemic grammars
    * functions to surface forms
* meaning-text grammars
    * deep syntax, surface syntax, morph, graph, formatter
* templates
    * limited syntactic variability

### Conclusions

## Bender & Koller '20 (Climbing towards NLU – On Meaning, Form and Understanding in the Age of Data)
**Abstract.** a system trained only on form has a priori no way to learn meaning

### Introduction
* BERT is doing well. it doesn't "understand"
* LM only uses form; cannot lead to meaning
* definition of meaning, impossible to learn without being trained, human NL acquisition, grounding

### Large LMs: Hype and Analysis
* "understand", "recall" bs
* we don't know what LMs have
    * BERTology
* tend to leverage artefacts in data
    * easily defeasible

### What is Meaning?
* form: observable realisation of language
    * meaning: relation between form and external
    * external: communicative intent
* form is not enough to learn reln between form and intent
* Searle's Chinese Room
    * symbol grounding problem

### The Octopus Test
* can an intelligent eavesdropping octopus imitate a participant in the conversation?

### More Constrained Thought Experiments
* train on Java programs and expect output
* train on English and photos (no connection) and expect descriptions/QA

### Human Language Acquisition
* it's grounded only
    * joint attention is required

### Distributional Semantics
* augment corpora with perceptual data
* interaction data w/ success annotations

### On Climbing the Right Hills
* BERT embeddings help
* doesn't apply to reading comprehension? what???

### Some Possible Counterarguments
* definition of meaning
* external data

* unsupervised MT systems might actually work out?

### Conclusion

## Bender et al. '21 (On the Dangers of Stochastic Parrots – Can Language Models Be Too Big?)
### Introduction
* LMs gettin biiig
* environmental risks
* documentation debt
* hype
* biases

### Background
* n gram models
* word embeddings
* lstms, transformers
* scale up was in: training data, sphere of influence

### Environmental and Financial Cost
* lots of CO2
* lots of paisa

### Unfathomable Training Data
* size != diversity
* value-lock
* bias

### Down the Garden Path
* BERT understands nothing

### Stochastic Parrots
* coherence
* dissemination by people

### Paths Forward
* consider everything

### Conclusion