## Biolink Validation Service

[![Build Status](https://travis-ci.org/TranslatorIIPrototypes/BLComplianceService.svg?branch=master)](https://travis-ci.org/TranslatorIIPrototypes/BLComplianceService)

Validates a ReasonerAPI message for BioLink compliance


### Geting started

This service requires python 3.7+

    pip install -r requirements.txt
    uvicorn bl_compliance.server:app --reload --port 8000
    
### Background

In the first phase of Translator, the knowledge graph standards working group
created a standard schema for data transfer between reasoners, and a standard
for representing graphs called the BioLink model. The knowledge graph portion of the
reasoner schema defines the graph required to answer a query. For practical reasons,
this schema is a more liberal superset of the BioLink Model schema.

This service validates the knowledge graph portion of a ReasonerAPI message. Users
can submit either a message object, or the knowledge graph portion of the Reasoner API standard.

Reasoner API examples:  
Robokop: https://robokop.renci.org/apidocs/  
ICEES: https://icees.renci.org/apidocs/  
RTX: https://arax.rtx.ai/api/rtx/v1/ui/  

### Related Repos

BioLink Model: https://github.com/biolink/biolink-model  
Translator Reasoners API: https://github.com/NCATS-Tangerine/NCATS-ReasonerStdAPI  
Reasoner API validation service: http://transltr.io:7071/apidocs  
