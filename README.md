# `schema-first` 

`schema-first` is a concept that uses json schema to manage models and versions. 

the general concept behind this demonstration is that `jsonschema` can used as a portable interface
for defining models. the `jsonschema` can be extended to python code in the module and documentation.
this project demonstrates how one could structure a project around schema.

at build time and import time our project will require different dependencies.
when our package is built we use `datamodel-codegen` to convert schema into python code.
the generated python code then depends on `pydantic`.
to summarize, json schema is converted to pydantic data models that can be reused.

the ability to acheive this is aided by `hatch` which makes life much easier
than past `setuptools` approaches. this design choice means that our approach is consistent
with modern python packaging conventions.

## features

* a custom `hatchling` build hook that translates schema 
* a `pyproject.toml` configuration that includes version management, docs, and tests
    * the expanded `hatch` cli is used for development tasks.
* a `src` layout that contains:
    * a python module call `my_schema_project`
    * a folder of `schema` to generate python code from


## schema


a difference between schema and code is the frequency of change. schema are expected to change slowly; this feature makes caching valuable for web applications serving schema. since schema change slowly they can be used a common interface for folks to co-develop features around a common language.

schema define types, or the extent of possible objects the type can become. schema are a specification independent of an implementation.
generally, software implementations change more frequently than their specifications (or type interfaces).

the slower change of schema is a feature of this approach. schema can be used to define the vocabulary of software.
with a explicit schema defined other co-developers like designers, advocates, and users can rely on schema 
to define the vocabulary of a piece of software.

## versioning

in this demonstration, the build system using `hatch-vcs`, a system similar to `setuptools-scm`, that provides dynamic version support based on git tags. 
based on the assumption of tagging git references, this schema first approach provides natural identifiers to the schema for each version. for example, we've created a tag for `v0.1.2` with naturally creates an identifier to our versions schema @ https://github.com/tonyfast/schema-first/blob/v0.1.2/src/schema/my_schema_model.json

the reference to past schema and future/development schema provides a reliable interface for developers and co-developers alike. the flux of change of software implementations occurs faster its specification/type interface.

type interfaces have proven valuable in scaling software projects (typescript/python). schema, specifically json schema, are even more portable type interfaces because they are language independent.
when schema are represented as data like json, yaml, or toml the interfaces are extended to those with non-code literaices. a shared schema between developers, designers, and consumers establishes a common vocabulary.



`hatch` makes it easier to include build-time assets in python projects.
i've been curious how `jsonschema` can play bigger role in python for a long time.



schema are useful because:

* the describe 
* the have unique identifiers
* the change infrequently
* they are `json` and generally useful.

go from jsonschema->python file at build time, the module imports derived models as import time