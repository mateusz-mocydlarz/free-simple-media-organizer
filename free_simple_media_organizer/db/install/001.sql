-- version 001

-- tables

CREATE TABLE "db_informations" (
	"information"	TEXT NOT NULL UNIQUE,
	"value"	        TEXT NOT NULL,
	"created_by"	TEXT,
	"created"	    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"modified_by"	TEXT,
	"modified"	    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("information")
);

CREATE TABLE "db_settings" (
	"setting"	    TEXT NOT NULL UNIQUE,
	"value"	        TEXT NOT NULL,
	"created_by"	TEXT,
	"created"	    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"modified_by"	TEXT,
	"modified"	    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("setting")
);

CREATE TABLE "sources" (
	"id"	        INTEGER NOT NULL UNIQUE,
	"source_path"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "paths" (
	"id"	        INTEGER NOT NULL UNIQUE,
	"source_id"    	INTEGER NOT NULL,
	"path"	        TEXT NOT NULL UNIQUE,
	FOREIGN KEY("source_id") REFERENCES "sources"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "files" (
	"id"	            INTEGER NOT NULL UNIQUE,
	"path_id"    		INTEGER NOT NULL,
	"name"              TEXT NOT NULL,
	"extension"         TEXT NOT NULL,
	"size"              INT NOT NULL,
	FOREIGN KEY("path_id") REFERENCES "paths"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);


--triggers

CREATE TRIGGER upd_db_informations AFTER UPDATE ON db_informations
BEGIN
	UPDATE db_informations SET modified = CURRENT_TIMESTAMP
	WHERE information = OLD.information;
END;

CREATE TRIGGER upd_db_settings AFTER UPDATE ON db_settings
BEGIN
	UPDATE db_settings SET modified = CURRENT_TIMESTAMP
	WHERE setting = OLD.setting;
END;