# Bestemmie.org API for lazy person


Simple wrapped [Bestemmie.org](http://bestemmie.org) [api](http://bestemmie.org/api) pip package

## Installation

`pip install bestemmie`

## Usage

#### Get random bestemmia

```
from bestemmie import Bestemmie
Bestemmie().random()
```
Return a simple bestemmia

`DIO CANE`

### Get all bestemmie

```
from bestemmie import Bestemmie
Bestemmie().all()
```
Return array of bestemmie objects with the single count of how many time was inserted
```
[
    {
        "bestemmia": "DIO CANE",
        "count": 2
    },
    ...
]
```

### Add bestemmia

```
from bestemmie import Bestemmie
Bestemmie().add(bestemmia, *False)
```

*You can pass an optional bool params for printing a success message
