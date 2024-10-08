-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: cadastro
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `cadastro`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `cadastro` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `cadastro`;

--
-- Table structure for table `favoritos_visualizar`
--

DROP TABLE IF EXISTS `favoritos_visualizar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favoritos_visualizar` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ano` varchar(50) DEFAULT NULL,
  `modalidade` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favoritos_visualizar`
--

LOCK TABLES `favoritos_visualizar` WRITE;
/*!40000 ALTER TABLE `favoritos_visualizar` DISABLE KEYS */;
/*!40000 ALTER TABLE `favoritos_visualizar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  `senha` varchar(50) DEFAULT NULL,
  `adm` tinyint(1) DEFAULT NULL,
  `ativo` tinyint DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'eduardo','123456',1,0),(2,'bernardo','123456',1,0),(3,'leonardo','123456',1,0),(4,'visualizar','123456',0,0);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Current Database: `olimpiadas`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `olimpiadas` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `olimpiadas`;

--
-- Table structure for table `2008_futebol_feminino`
--

DROP TABLE IF EXISTS `2008_futebol_feminino`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `2008_futebol_feminino` (
  `posição` int NOT NULL AUTO_INCREMENT,
  `pais` varchar(50) DEFAULT NULL,
  `total_gols` int DEFAULT NULL,
  `pênaltis` int DEFAULT NULL,
  `gols_sofridos` int DEFAULT NULL,
  `vitorias` int DEFAULT NULL,
  `empates` int DEFAULT NULL,
  `derrotas` int DEFAULT NULL,
  `cartões_amarelos` int DEFAULT NULL,
  `dois_cartões_amarelos` int DEFAULT NULL,
  `cartões_vermelhos` int DEFAULT NULL,
  PRIMARY KEY (`posição`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `2008_futebol_feminino`
--

LOCK TABLES `2008_futebol_feminino` WRITE;
/*!40000 ALTER TABLE `2008_futebol_feminino` DISABLE KEYS */;
INSERT INTO `2008_futebol_feminino` VALUES (1,'EUA',12,0,5,5,0,1,5,0,0),(2,'BRASIL',11,0,5,4,1,1,9,0,0),(3,'ALEMANHA',7,0,4,4,1,1,5,0,0);
/*!40000 ALTER TABLE `2008_futebol_feminino` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `2012_boxe_92kg`
--

DROP TABLE IF EXISTS `2012_boxe_92kg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `2012_boxe_92kg` (
  `posição` int NOT NULL AUTO_INCREMENT,
  `pais` varchar(50) DEFAULT NULL,
  `atleta` varchar(50) DEFAULT NULL,
  `numero_de_rodadas` int DEFAULT NULL,
  `total_de_pontos` int DEFAULT NULL,
  `pontos_marcados` int DEFAULT NULL,
  `pontos_sofridos` int DEFAULT NULL,
  PRIMARY KEY (`posição`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `2012_boxe_92kg`
--

LOCK TABLES `2012_boxe_92kg` WRITE;
/*!40000 ALTER TABLE `2012_boxe_92kg` DISABLE KEYS */;
INSERT INTO `2012_boxe_92kg` VALUES (1,'UCRÂNIA','Oleksandr Usyk',3,81,52,29),(2,'ITÁLIA','Clemente Russo',3,75,38,37),(3,'AZERBAIJÃO','Teymur Mammadov',3,89,44,45);
/*!40000 ALTER TABLE `2012_boxe_92kg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `2012_futebol_feminino`
--

DROP TABLE IF EXISTS `2012_futebol_feminino`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `2012_futebol_feminino` (
  `posição` int NOT NULL AUTO_INCREMENT,
  `pais` varchar(50) DEFAULT NULL,
  `total_gols` int DEFAULT NULL,
  `pênaltis` int DEFAULT NULL,
  `gols_sofridos` int DEFAULT NULL,
  `vitorias` int DEFAULT NULL,
  `empates` int DEFAULT NULL,
  `derrotas` int DEFAULT NULL,
  `cartões_amarelos` int DEFAULT NULL,
  `dois_cartões_amarelos` int DEFAULT NULL,
  `cartões_vermelhos` int DEFAULT NULL,
  PRIMARY KEY (`posição`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `2012_futebol_feminino`
--

LOCK TABLES `2012_futebol_feminino` WRITE;
/*!40000 ALTER TABLE `2012_futebol_feminino` DISABLE KEYS */;
INSERT INTO `2012_futebol_feminino` VALUES (1,'EUA',16,1,6,2,2,0,4,0,0),(2,'JAPAO',7,0,4,3,2,1,1,0,0),(3,'CANADA',12,0,8,3,1,2,3,0,0);
/*!40000 ALTER TABLE `2012_futebol_feminino` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `2016_basquete`
--

DROP TABLE IF EXISTS `2016_basquete`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `2016_basquete` (
  `posição` int NOT NULL AUTO_INCREMENT,
  `pais` varchar(50) DEFAULT NULL,
  `cestas` int DEFAULT NULL,
  `três_pontos` int DEFAULT NULL,
  `lances_livres` int DEFAULT NULL,
  `assistências` int DEFAULT NULL,
  `rebotes` int DEFAULT NULL,
  `rebotes_ofensivos` int DEFAULT NULL,
  `rebotes_defensivos` int DEFAULT NULL,
  `roubos_de_bola` int DEFAULT NULL,
  `bloqueios` int DEFAULT NULL,
  `turnovers` int DEFAULT NULL,
  `faltas_pessoais` int DEFAULT NULL,
  PRIMARY KEY (`posição`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `2016_basquete`
--

LOCK TABLES `2016_basquete` WRITE;
/*!40000 ALTER TABLE `2016_basquete` DISABLE KEYS */;
INSERT INTO `2016_basquete` VALUES (1,'EUA',278,83,168,191,364,129,235,70,28,94,171),(2,'SERVIA',237,59,132,177,289,87,202,67,16,117,197),(3,'ESPANHA',243,78,125,164,306,88,218,60,24,89,171);
/*!40000 ALTER TABLE `2016_basquete` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `2016_boxe_92kg`
--

DROP TABLE IF EXISTS `2016_boxe_92kg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `2016_boxe_92kg` (
  `posição` int NOT NULL AUTO_INCREMENT,
  `pais` varchar(50) DEFAULT NULL,
  `atleta` varchar(50) DEFAULT NULL,
  `numero_de_rodadas` int DEFAULT NULL,
  `total_de_pontos` int DEFAULT NULL,
  `pontos_marcados` int DEFAULT NULL,
  `pontos_sofridos` int DEFAULT NULL,
  PRIMARY KEY (`posição`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `2016_boxe_92kg`
--

LOCK TABLES `2016_boxe_92kg` WRITE;
/*!40000 ALTER TABLE `2016_boxe_92kg` DISABLE KEYS */;
INSERT INTO `2016_boxe_92kg` VALUES (1,'FRANÇA','Tony Yoka',4,12,10,2),(2,'GRÃ-BRETANHA','Joseph Joyce',4,12,10,2),(3,'CROÁCIA','Filip Hrgovic',3,9,7,2);
/*!40000 ALTER TABLE `2016_boxe_92kg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `2016_futebol_feminino`
--

DROP TABLE IF EXISTS `2016_futebol_feminino`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `2016_futebol_feminino` (
  `posição` int NOT NULL AUTO_INCREMENT,
  `pais` varchar(50) DEFAULT NULL,
  `total_gols` int DEFAULT NULL,
  `pênaltis` int DEFAULT NULL,
  `gols_sofridos` int DEFAULT NULL,
  `vitorias` int DEFAULT NULL,
  `empates` int DEFAULT NULL,
  `derrotas` int DEFAULT NULL,
  `cartões_amarelos` int DEFAULT NULL,
  `dois_cartões_amarelos` int DEFAULT NULL,
  `cartões_vermelhos` int DEFAULT NULL,
  PRIMARY KEY (`posição`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `2016_futebol_feminino`
--

LOCK TABLES `2016_futebol_feminino` WRITE;
/*!40000 ALTER TABLE `2016_futebol_feminino` DISABLE KEYS */;
INSERT INTO `2016_futebol_feminino` VALUES (1,'ALEMANHA',14,2,6,4,1,1,5,0,0),(2,'SUECIA',4,0,8,1,3,2,9,0,0),(3,'CANADA',10,1,5,5,0,1,12,0,1);
/*!40000 ALTER TABLE `2016_futebol_feminino` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `2020_basquete`
--

DROP TABLE IF EXISTS `2020_basquete`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `2020_basquete` (
  `posição` int NOT NULL AUTO_INCREMENT,
  `pais` varchar(50) DEFAULT NULL,
  `cestas` int DEFAULT NULL,
  `três_pontos` int DEFAULT NULL,
  `lances_livres` int DEFAULT NULL,
  `assistências` int DEFAULT NULL,
  `rebotes` int DEFAULT NULL,
  `rebotes_ofensivos` int DEFAULT NULL,
  `rebotes_defensivos` int DEFAULT NULL,
  `roubos_de_bola` int DEFAULT NULL,
  `bloqueios` int DEFAULT NULL,
  `turnovers` int DEFAULT NULL,
  `faltas_pessoais` int DEFAULT NULL,
  PRIMARY KEY (`posição`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `2020_basquete`
--

LOCK TABLES `2020_basquete` WRITE;
/*!40000 ALTER TABLE `2020_basquete` DISABLE KEYS */;
INSERT INTO `2020_basquete` VALUES (1,'EUA',218,80,78,146,222,59,163,59,31,62,122),(2,'FRANÇA',186,58,85,145,258,68,190,37,15,91,124),(3,'AUSTRALIA',195,75,76,148,221,68,153,58,10,75,99);
/*!40000 ALTER TABLE `2020_basquete` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `2020_boxe_92kg`
--

DROP TABLE IF EXISTS `2020_boxe_92kg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `2020_boxe_92kg` (
  `posição` int NOT NULL AUTO_INCREMENT,
  `pais` varchar(50) DEFAULT NULL,
  `atleta` varchar(50) DEFAULT NULL,
  `numero_de_rodadas` int DEFAULT NULL,
  `total_de_pontos` int DEFAULT NULL,
  `pontos_marcados` int DEFAULT NULL,
  `pontos_sofridos` int DEFAULT NULL,
  PRIMARY KEY (`posição`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `2020_boxe_92kg`
--

LOCK TABLES `2020_boxe_92kg` WRITE;
/*!40000 ALTER TABLE `2020_boxe_92kg` DISABLE KEYS */;
INSERT INTO `2020_boxe_92kg` VALUES (1,'CUBA','Julio Cesar La Cruz',4,20,18,2),(2,'RUSSIA','Muslim Gadzhimagomedov',4,20,14,6),(3,'BRASIL','Abner Teixeira',3,15,9,6);
/*!40000 ALTER TABLE `2020_boxe_92kg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `2020_futebol_feminino`
--

DROP TABLE IF EXISTS `2020_futebol_feminino`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `2020_futebol_feminino` (
  `posição` int NOT NULL AUTO_INCREMENT,
  `pais` varchar(50) DEFAULT NULL,
  `total_gols` int DEFAULT NULL,
  `pênaltis` int DEFAULT NULL,
  `gols_sofridos` int DEFAULT NULL,
  `vitorias` int DEFAULT NULL,
  `empates` int DEFAULT NULL,
  `derrotas` int DEFAULT NULL,
  `cartões_amarelos` int DEFAULT NULL,
  `dois_cartões_amarelos` int DEFAULT NULL,
  `cartões_vermelhos` int DEFAULT NULL,
  PRIMARY KEY (`posição`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `2020_futebol_feminino`
--

LOCK TABLES `2020_futebol_feminino` WRITE;
/*!40000 ALTER TABLE `2020_futebol_feminino` DISABLE KEYS */;
INSERT INTO `2020_futebol_feminino` VALUES (1,'CANADA',6,2,4,2,4,0,6,0,0),(2,'SUECIA',14,1,4,5,1,0,2,0,0),(3,'EUA',12,0,10,2,2,2,5,0,0);
/*!40000 ALTER TABLE `2020_futebol_feminino` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `2024_basquete`
--

DROP TABLE IF EXISTS `2024_basquete`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `2024_basquete` (
  `posição` int NOT NULL AUTO_INCREMENT,
  `pais` varchar(50) DEFAULT NULL,
  `cestas` int DEFAULT NULL,
  `três_pontos` int DEFAULT NULL,
  `lances_lives` int DEFAULT NULL,
  `assistências` int DEFAULT NULL,
  `rebotes` int DEFAULT NULL,
  `rebotes_ofensivos` int DEFAULT NULL,
  `rebotes_defensivos` int DEFAULT NULL,
  `roubos_de_bola` int DEFAULT NULL,
  `bloqueios` int DEFAULT NULL,
  `turnovers` int DEFAULT NULL,
  `faltas_pessoais` int DEFAULT NULL,
  PRIMARY KEY (`posição`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `2024_basquete`
--

LOCK TABLES `2024_basquete` WRITE;
/*!40000 ALTER TABLE `2024_basquete` DISABLE KEYS */;
INSERT INTO `2024_basquete` VALUES (1,'EUA',154,57,50,112,158,41,117,34,20,45,56),(2,'FRANÇA',107,33,66,73,123,39,84,27,17,53,80),(3,'SERVIA',134,45,61,100,134,27,107,30,17,49,71);
/*!40000 ALTER TABLE `2024_basquete` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `2024_boxe_92kg`
--

DROP TABLE IF EXISTS `2024_boxe_92kg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `2024_boxe_92kg` (
  `posição` int NOT NULL AUTO_INCREMENT,
  `pais` varchar(50) DEFAULT NULL,
  `atleta` varchar(50) DEFAULT NULL,
  `numero_de_rodadas` int DEFAULT NULL,
  `total_de_pontos` int DEFAULT NULL,
  `pontos_marcados` int DEFAULT NULL,
  `pontos_sofridos` int DEFAULT NULL,
  PRIMARY KEY (`posição`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `2024_boxe_92kg`
--

LOCK TABLES `2024_boxe_92kg` WRITE;
/*!40000 ALTER TABLE `2024_boxe_92kg` DISABLE KEYS */;
INSERT INTO `2024_boxe_92kg` VALUES (1,'UZBEQUISTÃO','Lazizbek Mullojonov',2,10,9,1),(2,'AZERBAIJÃO','Loren Berto Alfonso Dominguez',2,10,4,6),(3,'TAJIQUISTÃO','Davlat Boltaev',1,5,1,4);
/*!40000 ALTER TABLE `2024_boxe_92kg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `2024_futebol_feminino`
--

DROP TABLE IF EXISTS `2024_futebol_feminino`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `2024_futebol_feminino` (
  `posição` int NOT NULL AUTO_INCREMENT,
  `pais` varchar(50) DEFAULT NULL,
  `total_gols` int DEFAULT NULL,
  `pênaltis` int DEFAULT NULL,
  `gols_sofridos` int DEFAULT NULL,
  `vitorias` int DEFAULT NULL,
  `empates` int DEFAULT NULL,
  `derrotas` int DEFAULT NULL,
  `cartões_amarelos` int DEFAULT NULL,
  `dois_cartões_amarelos` int DEFAULT NULL,
  `cartões_vermelhos` int DEFAULT NULL,
  PRIMARY KEY (`posição`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `2024_futebol_feminino`
--

LOCK TABLES `2024_futebol_feminino` WRITE;
/*!40000 ALTER TABLE `2024_futebol_feminino` DISABLE KEYS */;
INSERT INTO `2024_futebol_feminino` VALUES (1,'EUA',12,0,2,6,0,0,5,0,0),(2,'BRASIL',7,0,7,3,0,3,11,1,1),(3,'ALEMANHA',6,1,6,3,1,2,7,0,0);
/*!40000 ALTER TABLE `2024_futebol_feminino` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anos`
--

DROP TABLE IF EXISTS `anos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `anos` (
  `ano` int NOT NULL,
  `basquete` tinyint(1) DEFAULT NULL,
  `futebol_feminino` tinyint(1) DEFAULT NULL,
  `boxe_92kg` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ano`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anos`
--

LOCK TABLES `anos` WRITE;
/*!40000 ALTER TABLE `anos` DISABLE KEYS */;
INSERT INTO `anos` VALUES (2008,0,1,0),(2012,0,1,1),(2016,1,1,1),(2020,1,1,1),(2024,1,1,1);
/*!40000 ALTER TABLE `anos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-07 11:49:49
