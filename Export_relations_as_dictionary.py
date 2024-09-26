# -*- coding: utf-8 -*-
"""
/***************************************************************************
 EXPORT QGIS RELATIONS AS A DICTIONARY
                              -------------------
        copyright: (C) 2024 by Federico Gianoli
        license: CC BY 4.0
 ***************************************************************************/
"""
from qgis.core import QgsProject


project = QgsProject.instance()
project_relation = project.relationManager()

relation_list = []

for relation in project_relation.relations().values():
    relazione_dict = {
        "name_relation": relation.name(),
        "id_relation": relation.id(),
        "name_parent": project.mapLayer(relation.referencedLayerId()).name(),
        "name_child": project.mapLayer(relation.referencingLayerId()).name(),
        "key_field_parent": list(relation.fieldPairs().keys())[0],  
        "key_field_child": list(relation.fieldPairs().values())[0]  
    }
    
    relation_list.append(relazione_dict)

print(relation_list)
