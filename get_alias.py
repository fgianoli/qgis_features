# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GET ALIAS NAME
                              -------------------
        copyright: (C) 2024 by Federico Gianoli
        license: CC BY 4.0
 ***************************************************************************/
"""

from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def get_field_alias(field_name, feature, parent):
    """
    Retrieves the alias of a field specified in the current layer..
    <ul> </ul>
    <h2>Example usage:</h2>
    <ul>
      <li>get_field_alias('Field_Name') -> 'FieldAlias'</li>
    </ul>
    """
    layer = feature.fields()
    field_index = layer.indexOf(field_name)
    
    if field_index != -1:
        alias = layer[field_index].alias()
        return alias
    else:
        return f"Field '{field_name}' not found."
