DROP TABLE IF EXISTS HechosCrimen;
DROP TABLE IF EXISTS Delito;
DROP TABLE IF EXISTS Fecha;
DROP TABLE IF EXISTS Ubicacion;
DROP TABLE IF EXISTS Persona;
DROP TABLE IF EXISTS GeoPoint;

/* Completa 


CREATE TABLE crimenes_cdmx (
	idCarpeta INTEGER PRIMARY KEY,
	Dia INTEGER,
	Mes VARCHAR(50),
	Año YEAR,
	Fecha DATE,
	Hora TIME,
	Delito VARCHAR(250),
	CalidadJuridica VARCHAR(250),
	Categoria VARCHAR(250),
	Colonia VARCHAR(250),
	Alcalia VARCHAR(150),
	Sexo VARCHAR(50),
	Edad INTEGER,
	TipoPersona VARCHAR(100),
	longitud DOUBLE,
	latitud DOUBLE
);

*/

/* ######################################################################*/



/* Delito */

CREATE TABLE Delito (
	idDelito INTEGER NOT NULL AUTO_INCREMENT,
	Delito VARCHAR(300),
	Categoria VARCHAR(200),
	Competencia VARCHAR(200),
	PRIMARY KEY (idDelito)
	
)ENGINE=innodb;

/* Ubicacion */

CREATE TABLE Ubicacion (
	idUbicacion INTEGER NOT NULL AUTO_INCREMENT,
	Alcaldia VARCHAR(150),
	Colonia VARCHAR(250),
	PRIMARY KEY (idUbicacion)
)ENGINE=innodb;

/* Geopoint */

CREATE TABLE GeoPoint (
	idGeoPoint INTEGER NOT NULL AUTO_INCREMENT,
	longitud DOUBLE,
	latitud DOUBLE,
	PRIMARY KEY (idGeoPoint)
)ENGINE=innodb;


/* Persona */

CREATE TABLE Persona (
	idPersona INTEGER NOT NULL AUTO_INCREMENT,
	Sexo VARCHAR(50),
	Edad INTEGER,
	TipoPersona VARCHAR(100),
	CalidadJuridica VARCHAR(100),
	PRIMARY KEY (idPersona)
)ENGINE=innodb;

/* Fecha */

CREATE TABLE Fecha (
	idFecha INTEGER NOT NULL AUTO_INCREMENT,
	Dia INTEGER,
	Mes VARCHAR(20),
	Año YEAR,
	Fecha DATE,
	Hora TIME,
	PRIMARY KEY (idFecha)
)ENGINE=innodb;

/* HechosCrimen */

CREATE TABLE HechosCrimen (
	idHechosCrimen INTEGER NOT NULL AUTO_INCREMENT,
	id_Delito INTEGER NOT NULL,
	id_Persona INTEGER NOT NULL,
	id_Fecha INTEGER NOT NULL,
	id_Ubicacion INTEGER NOT NULL,
	id_GeoPoint INTEGER NOT NULL,
	PRIMARY KEY (idHechosCrimen),
	FOREIGN KEY (id_Delito) REFERENCES Delito (idDelito),
	FOREIGN KEY (id_Persona) REFERENCES Persona (idPersona),
	FOREIGN KEY (id_Fecha) REFERENCES Fecha (idFecha),
	FOREIGN KEY (id_Ubicacion) REFERENCES Ubicacion (idUbicacion),
	FOREIGN KEY (id_GeoPoint) REFERENCES GeoPoint (idGeoPoint)

)ENGINE=innodb;

ALTER TABLE HechosCrimen ADD FOREIGN KEY (id_Delito) REFERENCES Delito (idDelito);
ALTER TABLE HechosCrimen ADD FOREIGN KEY (id_Ubicacion) REFERENCES Ubicacion (idUbicacion);
ALTER TABLE HechosCrimen ADD FOREIGN KEY (id_Fecha) REFERENCES Fecha (idFecha);
ALTER TABLE HechosCrimen ADD FOREIGN KEY (id_Persona) REFERENCES Persona (idPersona);
ALTER TABLE HechosCrimen ADD FOREIGN KEY (id_GeoPoint) REFERENCES GeoPoint (idGeoPoint);



/*  
LOAD DATA LOCAL INFILE '/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaDelito.csv' INTO TABLE Delito FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';	

LOAD DATA LOCAL INFILE '/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaFecha.csv' INTO TABLE Fecha  FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaUbicaion.csv' INTO TABLE Ubicacion  FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaPersona.csv' INTO TABLE Persona  FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

*/


CREATE INDEX id_GeoPoint ON HechosCrimen (id_GeoPoint);