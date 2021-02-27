<center>

# String generator API Docs

by Alexander Pietsch

</center>

---

## Basic syntax

For a request you need 2 parameters. These are:

* The type of the string which should be generated (mode)
* The length of the string which should be generated (length)

The basic URL to make a request is:

[http://alexpts.de:8000/api/v1.0/generate?mode={mode}&length={length}](http://alexpts.de:8000/api/v1.0/generate?mode=allChar&length=5)

---



## Modes parameter

There are 6 different types of strings to generate. These are:

1. numbers (returns an integer)
2. letters
3. uppercaseLetters
4. lowercaseLetters
5. punctuation
6. allChar

To see how they work and view their output click on a mode and view the example oder explore them below.

---

## Length parameter

The `length` parameter simply says how long the string to generate should be.

The maximum length is 120 characters. The minimum is 1 (who’d have thought).

---

## Examples

Modes and their example output

### numbers

Returns an integer of length N.

Example URL: [http://alexpts.de:8000/api/v1.0/generate?mode=numbers&length=5](http://alexpts.de:8000/api/v1.0/generate?mode=numbers&length=5)

output:
```json
[
   {
      "generatedString": 17181,
      "mode": "numbers",
      "stringLength": 5
   }
]
```

### letters 

Returns a string of length N.

Example URL: [http://alexpts.de:8000/api/v1.0/generate?mode=letters&length=5](http://alexpts.de:8000/api/v1.0/generate?mode=letters&length=5)

output:

```json
[
   {
      "generatedString": "VSNrT",
      "mode": "letters",
      "stringLength": 5
   }
]
```

### uppercaseLetters

Returns a string of length N. 

Example URL: [http://alexpts.de:8000/api/v1.0/generate?mode=uppercaseLetters&length=5](http://alexpts.de:8000/api/v1.0/generate?mode=uppercaseLetters&length=5)

```json
[
   {
      "generatedString": "SBOWL",
      "mode": "uppercaseLetters",
      "stringLength": 5
   }
]
```

### lowercaseLetters

Returns a string of length N. 

Example URL: [http://alexpts.de:8000/api/v1.0/generate?mode=lowercaseLetters&length=5](http://alexpts.de:8000/api/v1.0/generate?mode=lowercaseLetters&length=5)

```json
[
   {
      "generatedString": "kxzyr",
      "mode": "lowercaseLetters",
      "stringLength": 5
   }
]
```


### punctuation

Returns a string of length N. 

Example URL: [http://alexpts.de:8000/api/v1.0/generate?mode=punctuation&length=5](http://alexpts.de:8000/api/v1.0/generate?mode=punctuation&length=5)

```json
[
   {
      "generatedString": "^>(=$",
      "mode": "punctuation",
      "stringLength": 5
   }
]
```


### allChar

Returns a string of length N. 

Example URL: [http://alexpts.de:8000/api/v1.0/generate?mode=allChar&length=5](http://alexpts.de:8000/api/v1.0/generate?mode=allChar&length=5)

```json
[
   {
      "generatedString": "8.A$vR",
      "mode": "allChar",
      "stringLength": 5
   }
]
```


---
