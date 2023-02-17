.open votes.db
.mode box
.headers on
.changes on

DROP TABLE IF EXISTS photos;

  
CREATE TABLE photos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  caption TEXT NOT NULL,
  img TEXT NOT NULL UNIQUE,
  puppy_name TEXT,
  votes INTEGER DEFAULT 0
);

INSERT INTO photos (caption, puppy_name, img, votes)
  VALUES ("Nap time", "Max", "max.jpg",20),
         ("I miss my hammer", "Thor", "thor.jpg",25),
         ("Cool Dog", "Tango", "tango.jpg",2),
         ("I'm a Queen", "Lady", "lady.jpg",27),
         ("Did you say treat?", "Sadie", "sadie.jpg",22),
         ("When will it snow?", "Kyle", "kyle.jpg",16),
         ("I love a fresh mow", "Bella", "bella.jpg",26),
         ("I love my blanket", "Buster", "buster.jpg",10),
         ("There's a cat, you say?", "Cooper", "cooper.jpg",18),
         ("Who needs rescued?", "Baxter", "baxter.jpg",27);