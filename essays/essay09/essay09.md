# JSON: Overview

[JavaScript Object Notation (JSON)](https://en.wikipedia.org/wiki/JSON) is a plain-text file format for storing and sharing data. 

It was originally intended to be a subset of the JavaScript language, but is language-independent: that is, serializing data to JSON and deserializing data from JSON is supported by many programming languages ([Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON), [C](https://github.com/DaveGamble/cJSON), [Ruby](http://flori.github.io/json/), [Python](https://docs.python.org/2/library/json.html), [Go](https://golang.org/pkg/encoding/json/), [R](https://cran.r-project.org/web/packages/rjson/index.html), and [many others](http://www.json.org)).

The data format was invented by [Douglas Crockford](https://en.wikipedia.org/wiki/Douglas_Crockford) in the early 2000s. A JSON file consists of basically a string, which is easy to transmit between Web servers and browers.

### Schema and Accepted Data Types

The data format supports a limited number of data types:
- Number: a signed integer or floating point number that can use [scientific notation](https://en.wikipedia.org/wiki/Scientific_notation#E-notation) but cannot include values like `NaN` or `Inf`
- String: a sequence of characters in [Unicode](https://en.wikipedia.org/wiki/Unicode) that is bounded by quotation marks
- Boolean: either a `true` or `false`
- Array: an ordered list of values (any of the data types listed here) bounded between `[` and `]`
- Object: an unordered group of key-value pairs, where the keys are strings, keys and values are separated by colons, key-value pairs are delimited by commas, and the whole group is bounded by `{` and `}` 
- `null`: an empty value

### Comparison with Other Data Formats

### References
- Talk from Douglas Crockford discussing the history and development of JSON: https://www.youtube.com/watch?v=-C-JoyNuQJs

Author: Allie Morgan (allison.morgan@colorado.edu)
