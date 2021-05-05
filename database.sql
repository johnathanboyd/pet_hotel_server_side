-- CREATE DATABASE pet_hotel

CREATE TABLE "owner" (
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR (80) NOT NULL,
    "#_of_pets" INT DEFAULT '0'
);

CREATE TABLE "pets" (
    "id" SERIAL PRIMARY KEY,
    "pet_name" VARCHAR (80) NOT NULL,
    "owner_name" VARCHAR (80) NOT NULL,
    "breed" VARCHAR (100) NOT NULL,
    "color" VARCHAR (100) NOT NULL,
    "checked_in" BOOLEAN DEFAULT false 
);

INSERT INTO "pets" (pet_name, owner_name, breed, color, checked_in) VALUES ( %s, %s, %s, %s, %s);

INSERT INTO "owner" (name, "#_of_pets") VALUES ( %s, %s );

-- test data 

INSERT INTO "pets" (pet_name, owner_name, breed, color, checked_in) VALUES 
('Charlie', 'Chris', 'Shih-tzu', 'Black', false ), 
('Thorin', 'Chris', 'Rabbit', 'White', false), 
('Gatsby', 'Ally', 'Cat', 'White', true),
('Juniper', 'Dane', 'Cat', 'Tabby', false);

INSERT INTO "owner" (name, "#_of_pets") VALUES ( 'Chris', 2), ('Ally', 1), ('Dane', 1);