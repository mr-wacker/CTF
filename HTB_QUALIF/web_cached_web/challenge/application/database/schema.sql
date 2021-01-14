DROP TABLE IF EXISTS screenshots;

CREATE TABLE screenshots (
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	url TEXT NOT NULL, 
	filename TEXT NOT NULL, 
	created_at NOT NULL DEFAULT CURRENT_TIMESTAMP
);