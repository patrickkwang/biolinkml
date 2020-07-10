
# Type: gene to expression site association


An association between a gene and an expression site, possibly qualified by stage/timing info.

URI: [biolink:GeneToExpressionSiteAssociation](https://w3id.org/biolink/vocab/GeneToExpressionSiteAssociation)


![img](images/GeneToExpressionSiteAssociation.svg)

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [gene to expression site association➞object](gene_to_expression_site_association_object.md)  <sub>REQ</sub>
    * range: [AnatomicalEntity](AnatomicalEntity.md)
 * [gene to expression site association➞quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md)  <sub>OPT</sub>
    * range: [OntologyClass](OntologyClass.md)
 * [gene to expression site association➞relation](gene_to_expression_site_association_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [gene to expression site association➞stage qualifier](gene_to_expression_site_association_stage_qualifier.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
 * [gene to expression site association➞subject](gene_to_expression_site_association_subject.md)  <sub>REQ</sub>
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)

### Inherited from association:

 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **See also:** | | h |
|  | | t |
|  | | t |
|  | | p |
|  | | s |
|  | | : |
|  | | / |
|  | | / |
|  | | g |
|  | | i |
|  | | t |
|  | | h |
|  | | u |
|  | | b |
|  | | . |
|  | | c |
|  | | o |
|  | | m |
|  | | / |
|  | | m |
|  | | o |
|  | | n |
|  | | a |
|  | | r |
|  | | c |
|  | | h |
|  | | - |
|  | | i |
|  | | n |
|  | | i |
|  | | t |
|  | | i |
|  | | a |
|  | | t |
|  | | i |
|  | | v |
|  | | e |
|  | | / |
|  | | i |
|  | | n |
|  | | g |
|  | | e |
|  | | s |
|  | | t |
|  | | - |
|  | | a |
|  | | r |
|  | | t |
|  | | i |
|  | | f |
|  | | a |
|  | | c |
|  | | t |
|  | | s |
|  | | / |
|  | | t |
|  | | r |
|  | | e |
|  | | e |
|  | | / |
|  | | m |
|  | | a |
|  | | s |
|  | | t |
|  | | e |
|  | | r |
|  | | / |
|  | | s |
|  | | o |
|  | | u |
|  | | r |
|  | | c |
|  | | e |
|  | | s |
|  | | / |
|  | | B |
|  | | G |
|  | | e |
|  | | e |
