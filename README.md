# `schema-first` 

`schema-first` is a concept that uses json schema to manage models and versions. 

## why

`hatch` makes it easier to include build-time assets in python projects.
i've been curious how `jsonschema` can play bigger role in python for a long time.

schema are useful because:

* the describe 
* the have unique identifiers
* the change infrequently
* they are `json` and generally useful.

go from jsonschema->python file at build time, the module imports derived models as import time