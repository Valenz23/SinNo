CREATE DATABASE IF NOT EXIST sonder;
USE sonder;

CREATE TABLE IF NOT EXIST cancion (
    id INT PRIMARY KEY,
    artista VARCHAR(255),
    titulo VARCHAR(255),
    letra TEXT,
    popularidad DECIMAL(5, 2)
);