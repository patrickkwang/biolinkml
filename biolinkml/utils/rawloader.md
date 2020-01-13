# BiolinkML rawloader 

[biolinkml/utils/rawloader.py]() implements a single method, `load_raw_schema`, which takes:
* `data` - can be a relative or absolute file name, a relative or absolute URL, the text of a YAML file, an open file, or 
a dictionary that matches the form of SchemaDefintion.

`load_raw_schema` has two paths.  The first, on [biolinkml/utils/rawloader.py#36]() reconciles a file name or yaml text and
converts it into either an open file or a dictionary.  The second, [biolinkml/utils/rawloader.py#71]() invokes the YAML
loader if necessary and produces a SchemaDefinition conformatn dictionary.

Theoretically, it is possible for multiple schemas to be defined in the same file, in the form:
```yaml
schema1:
    id: ...
    title: ...

    prefixes:
      ...

    imports:
      ...

    ...

schema2:
    id: ...
    title: ...

```

While we are not aware of anyone that has taken advantage of this feature, the raw loader massages its input to match
this form, taking a single schema in the form:
```yaml
id: https://w3id.org/biolink/biolinkml/meta
title: Biolink Schema Metamodel
name: metamodel
description: A metamodel for defining biolink related schemas
license: https://creativecommons.org/publicdomain/zero/1.0/
version: 1.4.3
    ...
```
to
```yaml
metamodel:
    id: https://w3id.org/biolink/biolinkml/meta
    title: Biolink Schema Metamodel
    description: A metamodel for defining biolink related schemas
    license: https://creativecommons.org/publicdomain/zero/1.0/
    version: 1.4.3
    ...
```

Note that the schema name is currently optional.  If absent, it is generated from the last segment of the `id` URI (e.g. `id: https://w3id.org/biolink/biolinkml/meta` yields `name: meta`)

The raw loader then proceeds to perform some basic validation and minor "tweaks" including:
1) Make sure that the schema has the four basic (possibly empty) components, creating empty entries if necessary, and 
raising an error if any of them are not dictionaries.
2) Convert `in_subset` and `apply_to` schema entries into lists if they single entries
3) Convert `inports` into lists if they are single entries (not sure why this is a separate step)
4) Convert any classes that are declared but not populated into dictionaries
5) Convert any empty slot_usages within classes into dictionaries
6) Fill in the `domain` field of any slots that appear in the slot_usages

Finally, the list of schema definitions is flattened, with the first schema in the file becoming the "master" and the
remaining schemas merged into it.

