# BiolinkML Generator class

`Generator` ([biolinkml/utils/generator.py]()) is the abstract base class for all BiolinkML model code generators.  Its constructor takes the following arguments:
* `schema` - this can be a file name, a URI, YAML text, a TextIO stream, an instance of the BiolinkML `SchemaDefinition` class or
another instance of the `Generator` class. This allows a user to pass (optionally opened) YAML file, to programatically _create_ the schema.  The generator instance
form allows the RDF generator to use the same parsed schemas multiple times -- as exemplified by the RDF generator that uses both the JSON and JSON-LD Context generators
to create the final RDF.
* `format` - the expected output format.  The meaning of this attribute is determined by the implementing class (e.g. `Markdown` 
generator requires "md", the `ShExGenerator` needs one of "shex", "rdf", or "json").
* `emit_metadata` - some generators include information about source file, generation date, generator version, etc. in their
output.  This flag can be set fo `False` to keep metatada out of the output for unit tests and the like.  *Note:* By and large we
no longer use this in the `BiolinkML` unit tests, instead using filters (see: [tests/utils/metadata_filters.py]). This still may
have value to end-users, however
* `useuris` - The `class_uri`, `slot_uri` and `type_uri` attributes allow external URI's to be assigned to class_definition, slot_definition and
type_definition instances.  If `useuris` is `True` (the default), the URI's emitted in the JSON-LD context, RDF and OWL generators will be the
`X_uri` if present and, if absent, the combination of defining schema `id` and the class, slot or type name.  See: [#Model URIs]().  Note also that `uri` is the
alias for the `type_uri` slot.
* `import_map` - (optional) - if supplied, this maps the import statements in the BiolinkML Schema to local file names.  See: [#Import Maps]()
for more details.

The `Generator` invokes the [SchemaLoader.md](SchemaLoader) constructor, followed by its `resolve()` function.  It then loads the set of
variables that are needed by the visitor and serialize functions.

## Import Maps
The BiolinkML `import` statement can be a file name or URI and can either be relative or absolute.  Circumstances arise
in a testing environment where you need to point these elsewhere and do not want to (or cannot) edit the source.  This map
is a JSON document with simple key/value pairs.  see [tests/source/local_import_map.json]() and [tests/source/biolink_import_map.json]()
for examples.  Note that it is possible to include multiple entries for the same target.  As an example:
```yaml
{
  "biolinkml:types": "includes/types",
  "includes/types": "/opt/include/locals/includes/types",
}
```

Will map both:
```yaml
   imports:
     - biolinkml:types
```
and

```yaml
   imports:
     - includes/types
```
To `/opt/include/locals/includes/types.yaml`

It should also be noted that the URL form of `imports` statements reference UR**L**'s.  It is considered good practice
that all imports entries be either relative or absolute URI/L's (vs. file names) and, ideally, the referenced URI should
be the same the `id` of the imported source (**TODO:** consider enforcing this in a future release).  If this is the case,
it may also be necessary to use an import map to go from URI to URL if, for some reason, the URI is not directly referencable.



## Slot Aliases
Slot names must be globally unique in a given BiolinkML Schema and all of its imports. Some modeling languages, such as UML, accomplish 
this by either assigning secondary identifiers to its modeling artifacts.  Others, such as FHIR and the OMG's Onotology Definition
Metamodel (ODM) accomplish this through fully qualified path names.  BiolinkML uses non-unique aliases that can be used in situations 
where the context renders the slot name unambiguous.  

**Note:** This section applies to the slot named "`alias`".  Somewhat confusingly there is also a slot named "`aliases`", which is used
to assign alternative names to model artifacts.  These alternative names are strictly used for documentation purposes.

A slot alias can be explicitly declared -- as an example, the https://biolink.github.io/biolinkml/docs/description, https://biolink.github.io/biolinkml/docs/alt_description_text
and https://biolink.github.io/biolinkml/docs/value_description slots are all referenced as `description` within the context of the mode.

A slot alias is also generated implicitly by the `slot_usage` attribute, which is used to refine domain, range or other
aspects of an inherited class slot. (Note: as shown in [biolinkml/utils/schemaloader.py#L381]() - `process_slot_usages`.  It is also
possible to declare a `slot_usage` entry for slots that are _not_ defined by the parent class -- [biolinkml/utils/schemaloader.py#L389]().  It is
also possible to define a slot _directly_ within a class context.  In the latter case, a slot alias is not created.




## Name Mangling
`class` and `slot` names are "mangled" when generating python, RDF and other output forms.  The rules are:
* `class` and `type - leading and trailing white space, commas, spaces and '+' signs are removed.  The first letter of each word is upshifted. 
See `camlecase` in [biolinkml/utils/formatutils.py]().
* `slot` - leading and trailing white space and commas are removed. Spaces are replaced with underscores. See `underscore()` in [biolinkml/utils/formatutils.py]().
Note that, depending upon the usage, the `slot_name_for()` function in [biolinkml/utils/schemaloader.py]() returns the mangled slot _alias_ is one exists rather
than the name itself.

**Note:** Currently, there is no central `class_name_for` function -- `camelcase` is called directly for mangling class names.

**Note:** `type` and `subset` names are not mangled.  The convention currently used for type names and subsets is all lower case w/ underscores ('_').

## Model URIs
Every type, slot or class in a Schema is associated with two (potentially identical) URIs:
* The "model URI" - this is the concatenation of the schema `id` with the mangled slot
* The "class/slot/type URI" - this is the model URI if the 