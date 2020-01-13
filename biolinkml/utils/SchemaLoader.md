# BiolinkML SchemaLoader

The [biolinkml/utils/schemaloader.py]() has a constructor and a resolver.  The constructor takes roughly the same set
of arguments as the [Generator.md](Generator).  It converts the input data into a schema via the `load_raw_schema` function
and then initializes the class variables for use by the `resolve` step.

The `resolve()` method validates and massages the schema using the following steps:
1) Default the default_range for types to `string` if it is omitted, issuing a warning
2) Establish the default prefix.  If not declared, it is set to the rightmost element of the schema `id`
3) Add the declared prefixes to the namespace map
4) Iterate over the default curie maps, fetching them from the namespaces.org server and adding them to the namespace map
5) Establish a default prefix for the schema

It then proceeds to iterate over the import declarations, using the `load_raw_schema` function and mergint the
results into the base schema, followed by:

 
