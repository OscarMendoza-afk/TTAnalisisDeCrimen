DROP TABLE IF EXISTS Fecha;
DROP TABLE IF EXISTS Persona;
DROP TABLE IF EXISTS Ubicacion;
DROP TABLE IF EXISTS Delito;


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
	idCarpeta INTEGER,
	Delito VARCHAR(500),
	CalidadJuridica VARCHAR(500),
	Categoria VARCHAR(500),
	PRIMARY KEY (idCarpeta)
	
)ENGINE=innodb;

/* Ubicacion */

CREATE TABLE Ubicacion (
	idUbicacion INTEGER,
	Colonia VARCHAR(250),
	Alcaldia VARCHAR(150),
	longitud DOUBLE,
	latitud DOUBLE,
	FOREIGN KEY(idUbicacion) REFERENCES Delito(idCarpeta)
	ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=innodb;


/* Persona */

CREATE TABLE Persona (
	idPersona INTEGER,
	Sexo VARCHAR(50),
	Edad INTEGER,
	TipoPersona VARCHAR(100),
	FOREIGN KEY(idPersona) REFERENCES Delito(idCarpeta)
	ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=innodb;

/* Fecha */

CREATE TABLE Fecha (
	idFecha INTEGER,
	Dia INTEGER,
	Mes VARCHAR(50),
	Año YEAR,
	Fecha DATE,
	Hora TIME,
	FOREIGN KEY(idFecha) REFERENCES Delito(idCarpeta)
	ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=innodb;

/* ######################################################################*/
LOAD DATA LOCAL INFILE '/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaDelito.csv' INTO TABLE Delito FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';	

LOAD DATA LOCAL INFILE '/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaFecha.csv' INTO TABLE Fecha  FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaUbicaion.csv' INTO TABLE Ubicacion  FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaPersona.csv' INTO TABLE Persona  FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
