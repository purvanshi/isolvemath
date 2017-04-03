# Natural Language Parser
A natural language parser is a program that is used for computing the grammatical structure of sentences. For example - in a sentence, if we have to find which groups of words go together (as "phrases") and which words are the subject or object of a verb, we can use a parser. 

Parsers use knowledge of the language gained from hand-parsed sentences (manual parsing) to try to produce the most likely analysis of new sentences (automatic parsing).

## Stanford Dependency Parser
The Stanford Dependency Parser, as the name suggests, is a parser concocted by professors of Stanford University, made to construct dependency trees of various sentences inputted. 

It was originally written in Java but has been extended for various languages (ex - C#, PHP) and various languages (Chinese, French, German, Spanish).

## Getting started
We will deal with the installation of the Stanford Parser on Linux (and its derivatives), with the following prerequisites:
1. Python (>=3.5)
2. NLTK (>=3.1) - can be installed by running `sudo pip install nltk`
3. Java (>=1.8) - almost always comes pre-installed, but if not, Google is your friend.

Assuming you have set up all of the requirements, the next steps are as follows:

* Download the Stanford NLP Tools:

`cd`

`wget --read-timeout=10 http://nlp.stanford.edu/software/stanford-ner-2016-10-31.zip`

`wget --read-timeout=10 http://nlp.stanford.edu/software/stanford-postagger-full-2016-10-31.zip`

`wget --read-timeout=10 http://nlp.stanford.edu/software/stanford-parser-full-2015-10-31.zip`

* Unzip the files downloaded:

`unzip stanford-ner-2016-10-31.zip`

`unzip stanford-parser-full-2016-10-31.zip`

`unzip stanford-postagger-full-2016-10-31.zip`

* Add environment variables to your path:
    
     1. Add the StanfordToolsDir variable:
         
        `export STANFORDTOOLSDIR=$HOME`
     2. Add the Java ClassPath variable (so that Java knows where to find the JAR files for the Parser etc.):
         
        `export CLASSPATH=$STANFORDTOOLSDIR/stanford-postagger-full-2016-10-31/stanford-postagger.jar:$STANFORDTOOLSDIR/stanford-ner-2016-10-31/stanford-ner.jar:$STANFORDTOOLSDIR/stanford-parser-full-2016-10-31/stanford-parser.jar:$STANFORDTOOLSDIR/stanford-parser-full-2016-10-31/stanford-parser-3.7.0-models.jar`
     3. Add the StanfordModels variable (so that Java can find the POS Tagger models directory and the NER Tagger classifiers directory).
         
        `export STANFORD_MODELS=$STANFORDTOOLSDIR/stanford-postagger-full-2016-10-31/models:$STANFORDTOOLSDIR/stanford-ner-2016-10-31/classifiers`

## Testing

* For testing, fire up your Python shell and run the following commands - 

`from nltk.parse.stanford import StanfordDependencyParser`

`dep_parser=StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")`

`print ([parse.tree() for parse in dep_parser.raw_parse("The quick brown fox jumps over the lazy dog.")]) `

* Another alternative would be to run the supplied Python script (SDP.py) in the repository and run it with a string as an argument. For example, 

`python SDP.py "The quick brown fox jumps over the lazy dog."`




