# from qgis.core import QgsProject

# def aggiorna_filtri(nuova_data):
#     """
#     Aggiorna i filtri sui layer di QGIS basati sulla colonna 'date'.
    
#     :param nuova_data: La nuova data da utilizzare nel filtro (formato 'yyyy-MM-dd').
#     """
#     # Itera attraverso tutti i layer nel progetto
#     for layer in QgsProject.instance().mapLayers().values():
#         current_filter = layer.subsetString()
        
#         if 'date' in current_filter:
#             # Rimuovi temporaneamente il filtro
#             layer.setSubsetString("")
            
#             # Crea il nuovo filtro con la nuova data
#             nuovo_filtro = current_filter.replace(current_filter.split('=')[1].strip(), f"'{nuova_data}'")
            
#             # Riapplica il filtro con la nuova data
#             layer.setSubsetString(nuovo_filtro)
            
#             print(f"Filtro aggiornato per il layer {layer.name()} a: {nuovo_filtro}")

#     print("Aggiornamento dei filtri completato.")


import re
from qgis.core import QgsProject

def aggiorna_filtri(nuova_data):
    """
    Aggiorna i filtri sui layer di QGIS modificando solo la parte relativa alla data.

    :param nuova_data: La nuova data da utilizzare nel filtro (formato 'yyyy-MM-dd').
    """
    # Itera attraverso tutti i layer nel progetto
    for layer in QgsProject.instance().mapLayers().values():
        current_filter = layer.subsetString()
        
        # Se il filtro contiene una condizione per la data
        if 'date' in current_filter:
            # Usa una regex per trovare la condizione sulla data e aggiornarla
            nuovo_filtro = re.sub(r'"date"\s*=\s*\'\d{4}-\d{2}-\d{2}\'', f'"date" = \'{nuova_data}\'', current_filter)
            
            # Riapplica il filtro con la nuova data
            layer.setSubsetString(nuovo_filtro)
            print(f"Filtro aggiornato per il layer {layer.name()} a: {nuovo_filtro}")
    
    print("Aggiornamento dei filtri completato.")