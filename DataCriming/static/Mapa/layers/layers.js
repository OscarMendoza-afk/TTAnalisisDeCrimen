var wms_layers = [];


        var lyr_GoogleSatellite_0 = new ol.layer.Tile({
            'title': 'Google Satellite',
            'type': 'base',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
    attributions: ' ',
                url: 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}'
            })
        });

        var lyr_GoogleMaps_1 = new ol.layer.Tile({
            'title': 'Google Maps',
            'type': 'base',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
    attributions: ' ',
                url: 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}'
            })
        });

        var lyr_CartoLight_2 = new ol.layer.Tile({
            'title': 'Carto Light',
            'type': 'base',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
    attributions: ' ',
                url: 'https://a.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.pn'
            })
        });
var format_Alcaldias_3 = new ol.format.GeoJSON();
var features_Alcaldias_3 = format_Alcaldias_3.readFeatures(json_Alcaldias_3, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_Alcaldias_3 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_Alcaldias_3.addFeatures(features_Alcaldias_3);
var lyr_Alcaldias_3 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_Alcaldias_3, 
                style: style_Alcaldias_3,
                interactive: true,
                title: '<img src="styles/legend/Alcaldias_3.png" /> Alcaldias'
            });
var format_AZCAPOTZALCOfraude_4 = new ol.format.GeoJSON();
var features_AZCAPOTZALCOfraude_4 = format_AZCAPOTZALCOfraude_4.readFeatures(json_AZCAPOTZALCOfraude_4, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_AZCAPOTZALCOfraude_4 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_AZCAPOTZALCOfraude_4.addFeatures(features_AZCAPOTZALCOfraude_4);
var lyr_AZCAPOTZALCOfraude_4 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_AZCAPOTZALCOfraude_4, 
                style: style_AZCAPOTZALCOfraude_4,
                interactive: true,
                title: '<img src="styles/legend/AZCAPOTZALCOfraude_4.png" /> AZCAPOTZALCOfraude'
            });

lyr_GoogleSatellite_0.setVisible(true);lyr_GoogleMaps_1.setVisible(true);lyr_CartoLight_2.setVisible(true);lyr_Alcaldias_3.setVisible(true);lyr_AZCAPOTZALCOfraude_4.setVisible(true);
var layersList = [lyr_GoogleSatellite_0,lyr_GoogleMaps_1,lyr_CartoLight_2,lyr_Alcaldias_3,lyr_AZCAPOTZALCOfraude_4];
lyr_Alcaldias_3.set('fieldAliases', {'id': 'id', 'fid': 'fid', 'nomgeo': 'nomgeo', 'cve_mun': 'cve_mun', 'cve_ent': 'cve_ent', 'cvegeo': 'cvegeo', });
lyr_AZCAPOTZALCOfraude_4.set('fieldAliases', {'idCarpeta': 'idCarpeta', 'Dia': 'Dia', 'Mes': 'Mes', 'Año': 'Año', 'Fecha': 'Fecha', 'Hora': 'Hora', 'Delito': 'Delito', 'CalidadJuridica': 'CalidadJuridica', 'Categoria': 'Categoria', 'Colonia': 'Colonia', 'Alcalia': 'Alcalia', 'Sexo': 'Sexo', 'Edad': 'Edad', 'TipoPersona': 'TipoPersona', 'longitud': 'longitud', 'latitud': 'latitud', });
lyr_Alcaldias_3.set('fieldImages', {'id': 'TextEdit', 'fid': 'Range', 'nomgeo': 'TextEdit', 'cve_mun': 'TextEdit', 'cve_ent': 'TextEdit', 'cvegeo': 'TextEdit', });
lyr_AZCAPOTZALCOfraude_4.set('fieldImages', {'idCarpeta': '', 'Dia': '', 'Mes': '', 'Año': '', 'Fecha': '', 'Hora': '', 'Delito': '', 'CalidadJuridica': '', 'Categoria': '', 'Colonia': '', 'Alcalia': '', 'Sexo': '', 'Edad': '', 'TipoPersona': '', 'longitud': '', 'latitud': '', });
lyr_Alcaldias_3.set('fieldLabels', {'id': 'no label', 'fid': 'no label', 'nomgeo': 'no label', 'cve_mun': 'no label', 'cve_ent': 'no label', 'cvegeo': 'no label', });
lyr_AZCAPOTZALCOfraude_4.set('fieldLabels', {'idCarpeta': 'no label', 'Dia': 'no label', 'Mes': 'no label', 'Año': 'no label', 'Fecha': 'no label', 'Hora': 'inline label', 'Delito': 'no label', 'CalidadJuridica': 'no label', 'Categoria': 'no label', 'Colonia': 'no label', 'Alcalia': 'no label', 'Sexo': 'no label', 'Edad': 'no label', 'TipoPersona': 'no label', 'longitud': 'no label', 'latitud': 'no label', });
lyr_AZCAPOTZALCOfraude_4.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});