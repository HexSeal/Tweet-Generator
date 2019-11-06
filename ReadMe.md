# CS 1.2: How Data Structures Work

## Course Description

A project based course that looks under the hood at data structures and algorithms to see how they work. In addition to implementing these structures in an application; students will build them from scratch, analyze their complexity, and benchmark their performance to gain an understanding of their tradeoffs and when to use them in practice. Students will write scripts, functions, and library modules to use text processing tools like regular expressions, construct and sample probability distributions to create a Markov language model and gain insight into how grammar works and natural language processing techniques.

## Heroku: 


Questions for class:
* What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?
    * App.py has the flask web route(s)
    * histogram.py formats the source text
    * Sample.py gets a word through stochastic sampling
* Are the names of files, modules, functions, and variables appropriate and accurate? Would a new programmer be able to understand the names without too much contextual knowledge?
    * The names themselves aren’t too hard to understand individually, but their relationship to one another would be hard for a newer programmer to understand. Also, things such as the histogram.py file have names that need more context or explanation to understand in the scheme of the whole code.
* What are the scopes of variables and are they appropriate for their use case? If there are global variables, why are they needed?
    * There are no global variables to allow the code to be reusable as possible, and uphold the DRY principle. Global variables make it hard to use the file from other places. 
* Are the functions small and clearly specified, with as few side effects as possible?
    * Yes, there are also helper functions to make sure everything is as reusable as possible while also making it easy to hunt down errors. Side effects are minimal if any, right now the only one is that extra punctuation isn’t stripped for some reason.
* Are there functions that could be better organized in an Object-Oriented Programming style by defining them as methods of a class?
    * Yes, as classes would make it easier to reuse code even more and allow for the code to possibly be used in other projects. Using objects allows those objects to be manipulated for specific purposes of the projects while also remaining reusable.
* Can files be used as both modules and as scripts?
    * No, for the most part I focused on the overall project, but some things such as rearrange.py can be used as scripts as well.
* Do modules all depend on each other or can they be used independently?
    * Most modules must be used with the others. Histogram formats the code for sample.py to then use. This is the base of how we’re going to use Markov language chains to be able to generate fake tweets.
