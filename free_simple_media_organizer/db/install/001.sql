-- version 001


-- tables

CREATE TABLE "db_informations" (
	"information"	TEXT NOT NULL UNIQUE,
	"value"	        TEXT NOT NULL,
	"created_by"	TEXT,
	"created"	    TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"modified_by"	TEXT,
	"modified"	    TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("information")
);

CREATE TABLE "db_settings" (
	"setting"	    TEXT NOT NULL UNIQUE,
	"value"	        TEXT NOT NULL,
	"created_by"	TEXT,
	"created"	    TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"modified_by"	TEXT,
	"modified"	    TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("setting")
);

CREATE TABLE "directories" (
	"id"	        INTEGER NOT NULL UNIQUE,
	"path"	        TEXT NOT NULL UNIQUE,
	"created_by"	TEXT,
	"created"	    TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"modified_by"	TEXT,
	"modified"	    TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "files" (
	"id"	            INTEGER NOT NULL UNIQUE,
	"directories_id"    INTEGER NOT NULL,
	"path"	            TEXT NOT NULL,
	"name"              TEXT NOT NULL,
	"size"              INT NOT NULL,
	"created_by"	    TEXT,
	"created"	        TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"modified_by"	    TEXT,
	"modified"	        TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY("directories_id") REFERENCES "directories"("id"),
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

CREATE TRIGGER upd_directories AFTER UPDATE ON directories
BEGIN
	UPDATE directories SET modified = CURRENT_TIMESTAMP
	WHERE id = OLD.id;
END;

CREATE TRIGGER upd_files AFTER UPDATE ON files
BEGIN
	UPDATE files SET modified = CURRENT_TIMESTAMP
	WHERE id = OLD.id;
END;