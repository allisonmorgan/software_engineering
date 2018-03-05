# Go: Overview

The story goes that while waiting for their C software to build at Google, Robert Griesemer, Rob Pike and Ken Thompson started to whiteboard a language which was easy to use while still efficient at compile and run times. From the [FAQs](https://golang.org/doc/faq#creating_a_new_language) of the Go website:

> Go was born out of frustration with existing languages and environments for systems programming. Programming had become too difficult and the choice of languages was partly to blame. One had to choose either efficient compilation, efficient execution, or ease of programming; all three were not available in the same mainstream language.

In this essay, I'll highlight a few of the ways in which Go handles some of the [common pain points](https://talks.golang.org/2012/splash.article) of programming languages: (1) slow builds, (2) code can be hard to read, and (3) scalability.

### Speed

One of the motivating factors for the development of Go was to increase the speed of code builds. Go handles this issue through several interesting programmatic decisions. 

First, if a piece of code imports any **unused dependencies**, that results in an error upon program compilation. This is very unlike languages like Python and C, and results in many less file reads for dependencies. Also particular to Go is the order in which dependencies are managed. For example if a piece of code `A` imports package `B`, and that package `B`imports `C`, it is [more efficient](https://talks.golang.org/2012/splash.article#TOC_7.) to import `C`, then `B`, then `A`. Another interesting decision within the language Go, is that programs cannot present dependency cycles (`A` imports `B` and `B` imports `A`). This can also lead to slow builds and encourages more readable code. In combination with decisions of syntax, which I will discuss shortly, dependency management within Go can be very efficient.

Second, at the expense of some latency and complexity, the Go programming language features **garbarge collection**. The developers point out that the management of memory can place a relatively large burden on programmers, and mismanagement can be expensive. A new Go programmer can rest easy that memory is being used and released efficiently, but a more experience Go programmer can control the memory allocation of data structures. For example, an array could be initialized with relatively large size (`var x []int`), or with a specific budget in mind (`var x [5]int`).

### Understandability

Go's [syntax](https://golang.org/doc/faq#types) for defining functions is explicitly typed, and can be either explicitly or implicitly typed for variables. That is, when defining a function, the syntax looks like:

```go
func multiply(a int, b int) int { return a*b }
```

This can be helpful for others reading your code to recognize that this function accepts two integers and is expected to return one integer. This also puts some burden on the programmer to then make sure that the values passed to `multiply` are in fact integers. (Also, the brace bounded blocks [more clearly define](https://talks.golang.org/2012/splash.article#TOC_4.) the beginning and ending of a function.) When it comes to new variables, the syntax looks like:

```go
var x int    // explicit
x := 0       // implicit
```

Note, the `:=` initializes the value and type of a variable. Again, this might be a feature which helps others understand variable type. Another interesting feature of Go, is the distinction of public and local variables by [capitalization](https://talks.golang.org/2012/splash.article#TOC_11.). As a developer this helps one more clearly define variables which we would like other pieces of code to have access to. This also helps with fast code builds by limiting the number of variables that need to be exported.

### Scalability

As we have been talking about in class, concurrency is important for the efficient and accurate evaluation of distributed software. From Go's [documentation](https://talks.golang.org/2012/splash.article#TOC_13.):

> Go's concurrent features work well in a context familiar to most programmers. Go enables simple, safe concurrent programming ...

[Inherent to Go](https://tour.golang.org/concurrency/1), are "goroutines" (threads) and channels. We can also apply a ["mutex"](https://tour.golang.org/concurrency/9) to variables, when we want to avoid conflicts and allow only one goroutine to access a variable at a time. Concurrency is a relatively new idea to me and I rarely used it when programming in Go, but I get the impression that [concurrency within Go](https://www.youtube.com/watch?v=f6kdp27TYZs) is a relatively unique and useful idea.

### References

- Adaptation of Rob Pike's [talk about Go](https://talks.golang.org/2012/splash.article)
- More information about the [cute gopher mascot](https://blog.golang.org/gopher)
- [Wikipedia entry](https://en.wikipedia.org/wiki/Go_(programming_language)) for Go
- [Tour of Go](https://tour.golang.org/welcome/1), [Sandbox](https://play.golang.org)

Author: Allie Morgan (allison.morgan@colorado.edu)