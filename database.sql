-- CREATE DATABASE pet_hotel

CREATE TABLE "owner" (
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR (80) NOT NULL,
    "pets_id" INT, 
    FOREIGN KEY (pets_id) REFERENCES pets(id)
);

CREATE TABLE "pets" (
    "id" SERIAL PRIMARY KEY,
    "pet_name" VARCHAR (80) NOT NULL,
    "breed" VARCHAR (100) NOT NULL,
    "color" VARCHAR (100) NOT NULL,
    "checked_in" BOOLEAN DEFAULT false 
);

INSERT INTO "pets" (pet_name, breed, color, checked_in) VALUES ( %s, %s, %s, %s);

INSERT INTO "owner" (name, pets_id) VALUES ( %s, %s );

-- test data 

INSERT INTO "pets" (pet_name, breed, color, checked_in) VALUES 
('Charlie', 'Shih-tzu', 'Black', false ), 
('Thorin', 'Rabbit', 'White', false), 
('Gatsby', 'Cat', 'White', true),
('Juniper', 'Cat', 'Tabby', false);

INSERT INTO "owner" (name, pets_id) VALUES ( 'Chris', 1 ), ('Ally', 3), ('Dane', 4);