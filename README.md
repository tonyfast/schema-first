# `schema-first` 

__the dream__: json schema as a generic interface for development and co-development of software.

the adoption of type interfaces in typescript and python have enabled teams to build larger communities around their software. type interfaces, or specifications, operate as a community contracts that codify the vocabularies used by its members. type systems in different languages can be semantically the same, but they will by syntactically different. as a result, type system conventions are not generally portable across languages.

json schema can be interpretted as a type specification written in `json` syntax. while `json` may seem like just another syntax its form is general enough to be used by most programming languages.

in this demonstration, we use json schema as a precursor for python models and implementations. we further show how this design decision immediately offers value in testing and documentation.

## details

in `src/schema` there is a json schema model we use for demonstration. when our python package is built, the `datamodel-codegen` tool is used to generate `pydantic` models found in `src/my_schema_project/models`. 

`hatch` is used to comply with modern python packaging conventions. `datamodel-codegen` is a build time dependency and is not needed by our consumers. when someone imports `my_schema_project` they only depend on `pydantic`, and their experience should be improve by mitigating a blocking code generation call. 

`hatch-vcs` is used to manage the versioning based on git tags. by using this best practice we find that we've generated very nice identifiers for our schema per version. for example, tag `v0.1.2` has an identifier @ https://github.com/tonyfast/schema-first/blob/v0.1.2/src/schema/my_schema_model.json . at the scale of the url of this url we can understand how developers and co-developers can arrive at this definitions to understand the vocabulary of a project.

## testing and docs

the schema used to generate `pydantic` models in python code servers two other purposes in this demonstration:

1. the schema generates documentation using the `sphinx-jsonschema` .

    hatch run docs:html

    ```{toctree}
    src/docs
    ```

2. the schema generates tests using the `hypothesis-jsonschema` package.

    hatch run tests:cov
    hatch run tests:html

    ```{toctree} 
    coverage <htmlcov/index.html>
    test results <pytest.html>
    ```


> `hatch` is our development tool. in the `pyproject.toml`, we define `hatch.envs` to `test` and generates `docs`. 

## schema vs code


a difference between schema and code is the frequency of change. schema are expected to change slowly; this feature makes caching valuable for web applications serving schema. since schema change slowly they can be used a common interface for folks to co-develop features around a common language.

the slower change of schema is a feature of this approach. schema can be used to define the vocabulary of software.
with a explicit schema defined other co-developers like designers, advocates, and users can rely on schema 
to define the vocabulary of a piece of software.

## done

json schema plays a big role in keeping software projects honest, and there may be some bigger roles it could play.

## appendix

good types tell good stories.

### input formats

the input format of the schema likely doesn't matter. we could use:

* boring, old, unfun to write `json`
* a more forgiving a modern `json5`
* `toml` for those desiring a more minimal markdown language. `toml` doesn't have a `null` value which is okay against the `jsonschema` specification.
 `json`, `toml`, `yaml`, `json5` based on the literacies of our co-developers. 
* `yaml` could work, but `i say: no`. seriously, how are going to choose a library?

[484]: https://peps.python.org/pep-0484/