# JSON: Overview

[JavaScript Object Notation (JSON)](https://en.wikipedia.org/wiki/JSON) is a plain-text file format for storing and sharing data. It is a commonly used data format returned by many APIs.

It was originally intended to be a subset of the JavaScript language, but is language-independent: that is, serializing data to JSON and deserializing data from JSON is supported by many programming languages ([Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON), [C](https://github.com/DaveGamble/cJSON), [Ruby](http://flori.github.io/json/), [Python](https://docs.python.org/2/library/json.html), [Go](https://golang.org/pkg/encoding/json/), [R](https://cran.r-project.org/web/packages/rjson/index.html), and [many others](http://www.json.org)).

The data format was invented by [Douglas Crockford](https://en.wikipedia.org/wiki/Douglas_Crockford) in the early 2000s. A JSON file consists of basically a string, which is easy to transmit between Web servers and browers. (Its media type ([MIME](https://en.wikipedia.org/wiki/Media_type)) is `application/json`.)

### Schema and Accepted Data Types

The data format supports a limited number of data types:
- Number: a signed integer or floating point number that can use [scientific notation](https://en.wikipedia.org/wiki/Scientific_notation#E-notation) but cannot include values like `NaN` or `Inf`
- String: a sequence of characters in [Unicode](https://en.wikipedia.org/wiki/Unicode) that is bounded by quotation marks
- Boolean: either a `true` or `false`
- Array: an ordered list of values (any of the data types listed here) bounded between `[` and `]`
- Object: an unordered group of key-value pairs, where the keys are strings, keys and values are separated by colons, key-value pairs are delimited by commas, and the whole group is bounded by `{` and `}` 
- `null`: an empty value

Here's an `example.json` from [Wikipedia](https://en.wikipedia.org/wiki/JSON#Data_types,_syntax_and_example):

>```json
>{
>  "firstName": "John",
>  "lastName": "Smith",
>  "isAlive": true,
>  "age": 27,
>  "address": {
>    "streetAddress": "21 2nd Street",
>    "city": "New York",
>    "state": "NY",
>    "postalCode": "10021-3100"
>  },
>  "phoneNumbers": [
>    {
>      "type": "home",
>      "number": "212 555-1234"
>    },
>    {
>      "type": "office",
>      "number": "646 555-4567"
>    },
>    {
>      "type": "mobile",
>      "number": "123 456-7890"
>    }
>  ],
>  "children": [],
>  "spouse": null
>}
>```

### [Comparison with Other Data Formats](https://en.wikipedia.org/wiki/JSON#Comparison_with_other_formats)

JSON is often preferred to [Extensible Markup Language (XML)](https://en.wikipedia.org/wiki/XML) which has strong data types, predefined attributes, and a more formal, ordered structure. For example, the JSON object above could be rewritten in XML as so:
```xml
<person>
  <firstName>John</firstName>
  <lastName>Smith</lastName>
  <isAlive>true</isAlive>
  <age>25</age>
  <address>
    <streetAddress>21 2nd Street</streetAddress>
    <city>New York</city>
    <state>NY</state>
    <postalCode>10021-3100</postalCode>
  </address>
  <phoneNumber>
    <type>home</type>
    <number>212 555-1234</number>
  </phoneNumber>
  <phoneNumber>
    <type>office</type>
    <number>646 555-4567</number>
  </phoneNumber>
  <phoneNumber>
    <type>mobile</type>
    <number>123 456-7890</number>
  </phoneNumber>
  <children></children>
</person>
```

Note both markup formats are human-readable and hierarchical, but people often prefer JSON since it is [quicker to read and write](https://www.w3schools.com/js/js_json_xml.asp).

Another popular format is called [YAML](https://en.wikipedia.org/wiki/YAML) ("YAML Ain't Markup Language", a [recursive acronym](https://en.wikipedia.org/wiki/Recursive_acronym)). People sometimes prefer YAML to JSON becuase it's [easier to read](https://stackoverflow.com/questions/1726802/what-is-the-difference-between-yaml-and-json-when-to-prefer-one-over-the-other) since syntax is even more lightweight. For example, the above JSON and XML files can be re-written in YAML as:

```yaml
firstName: John
lastName: Smith
isAlive: true
age: 25
address: 
  streetAddress: 21 2nd Street
  city: New York
  state: NY
  postalCode: '10021-3100'
phoneNumber: 
- type: home
  number: 212 555-1234
- type: office
  number: 646 555-4567
- type: mobile
  number: 123 456-7890
gender: 
  type: male
```

Note here how the delimiters like `[` and `{` have been replaced with indentation, and the quotation marks have been removed. Unlike JSON, both XML and YAML support comments.

### Serialization / Deserialization

Here's how you can serialize -- turn a data structure into JSON -- in Python:

```python
>>> import json
>>> phoneNumbers = [
>>>		{"type": "home", "number": "212 555-1234"}, 
>>>		{"type": "office", "number": "646 555-4567"}, 
>>>		{"type": "mobile","number": "123 456-7890"}
>>> ]
>>> address = {
>>>		"streetAddress": "21 2nd Street", 
>>>		"city": "New York", 
>>>		"state": "NY", 
>>>		"postalCode": "10021-3100"
>>> }
>>> person = {
>>>		"firstName": "John", 
>>>		"lastName": "Smith", 
>>>		"isAlive": True, 
>>>		"age": 27, 
>>>		"address": address, 
>>>		"phoneNumbers": phoneNumbers, 
>>>		"children": [], 
>>>		"spouse": None
>>> }
> json.dumps(person)
'{"phoneNumbers": [{"type": "home", "number": "212 555-1234"}, {"type": "office", "number": "646 555-4567"}, {"type": "mobile", "number": "123 456-7890"}], "isAlive": true, "firstName": "John", "address": {"postalCode": "10021-3100", "city": "New York", "streetAddress": "21 2nd Street", "state": "NY"}, "lastName": "Smith", "age": 27, "spouse": null, "children": []}'
```

If you'd like to deserialize an object -- parse a JSON file and return it as an object -- try:
```python
>>> import json
>>> personStr = '{"phoneNumbers": [{"type": "home", "number": "212 555-1234"}, {"type": "office", "number": "646 555-4567"}, {"type": "mobile", "number": "123 456-7890"}], "isAlive": true, "firstName": "John", "address": {"postalCode": "10021-3100", "city": "New York", "streetAddress": "21 2nd Street", "state": "NY"}, "lastName": "Smith", "age": 27, "spouse": null, "children": []}'
>>> json.loads(personStr)
{u'phoneNumbers': [{u'type': u'home', u'number': u'212 555-1234'}, {u'type': u'office', u'number': u'646 555-4567'}, {u'type': u'mobile', u'number': u'123 456-7890'}], u'isAlive': True, u'firstName': u'John', u'lastName': u'Smith', u'age': 27, u'address': {u'postalCode': u'10021-3100', u'city': u'New York', u'streetAddress': u'21 2nd Street', u'state': u'NY'}, u'spouse': None, u'children': []}
```

Above I am using Python's built-in [JSON package](https://docs.python.org/2/library/json.html).

### References
- Wikipedia for JSON: https://en.wikipedia.org/wiki/JSON
- Talk from Douglas Crockford discussing the history and development of JSON: https://www.youtube.com/watch?v=-C-JoyNuQJs

Author: Allie Morgan (allison.morgan@colorado.edu)
