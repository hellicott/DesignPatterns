# Design Patterns
## Contents
[Creational Design Patterns](#creational)
- [Singleton](#singleton)

[Structural Design Patterns](#structural)


[Behavioural Design Patterns](#behavioural)


## Creational
### Singleton
[[code](singleton_pattern)]

My implementation of this pattern contains a singleton class `Logger` and a couple of
classes which use it, `Usage` and `Another Usage`. To test that only one instance was 
being made I added some print statements. This was the result, showing only one instance of
`Logger` being created, and that same instance being used to log.

![alt text](docs/singleton.PNG "Singleton command line output")

#### What is it?
A class which can only have one instance.

#### When is it useful?
An application needs only one instance of an object which can be globally accessed.

A common use for the singleton pattern is for logging. Often you want one instance
of the logging class in your program, but wish to use it throughout. Therefore you
benefit from having a global single instance of this class. You can see this example
implemented in the code

#### When is it *not* useful?
It shouldn't be used as a global variable. Whilst it acts a bit like one, you should really be asking yourself
> Why do I want to make this thing global?

Not 
> How can I make this thing global?

This is a code smell, implying bad design. 

This pattern is also not necessarily appropriate in multithreaded programs which are asynchronous,
it could still create multiple instances.

### Builder
[[code](builder)]

#### What is it?

#### When is it useful?

#### When is it *not* useful?

[[Back To Top](#design-patterns)]
## Structural


[[Back To Top](#design-patterns)]
## Behavioural


[[Back To Top](#design-patterns)]

# References/further reading
[source making](https://sourcemaking.com/design_patterns) contains a good reference for many design patterns

[geeks for geeks](https://www.geeksforgeeks.org/software-design-patterns/) had some good base knowledge, as well as 
example implementations of many patterns

[toptal](https://www.toptal.com/python/python-design-patterns) has useful python implementations of design patterns
(most I found were in Java)

[[Back To Top](#design-patterns)]