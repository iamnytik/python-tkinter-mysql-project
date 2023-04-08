-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: dbmsproject
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `username` char(20) NOT NULL,
  `password` char(20) NOT NULL,
  `id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('joker','circus',1);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logistic_units`
--

DROP TABLE IF EXISTS `logistic_units`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logistic_units` (
  `logistic_unit_id` int NOT NULL,
  `trans_type` char(20) DEFAULT NULL,
  `rent` int DEFAULT NULL,
  `available` char(5) DEFAULT NULL,
  PRIMARY KEY (`logistic_unit_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logistic_units`
--

LOCK TABLES `logistic_units` WRITE;
/*!40000 ALTER TABLE `logistic_units` DISABLE KEYS */;
INSERT INTO `logistic_units` VALUES (0,'airplanes',8000,'y'),(2,'ship',100000000,'y'),(5,'rail',3,'y'),(11,'lorry',8080,'y'),(25,'ship',50,'y');
/*!40000 ALTER TABLE `logistic_units` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manages`
--

DROP TABLE IF EXISTS `manages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manages` (
  `user_id` int NOT NULL,
  `logistic_unit_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manages`
--

LOCK TABLES `manages` WRITE;
/*!40000 ALTER TABLE `manages` DISABLE KEYS */;
INSERT INTO `manages` VALUES (5,0),(6,0),(7,2),(10,0);
/*!40000 ALTER TABLE `manages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `price`
--

DROP TABLE IF EXISTS `price`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `price` (
  `cost` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `rent` int DEFAULT NULL,
  `time` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `price`
--

LOCK TABLES `price` WRITE;
/*!40000 ALTER TABLE `price` DISABLE KEYS */;
INSERT INTO `price` VALUES (300000000,4,100000000,3),(800000000,7,100000000,8);
/*!40000 ALTER TABLE `price` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `summary`
--

DROP TABLE IF EXISTS `summary`;
/*!50001 DROP VIEW IF EXISTS `summary`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `summary` AS SELECT 
 1 AS `logistic_unit_id`,
 1 AS `user_id`,
 1 AS `name`,
 1 AS `email`,
 1 AS `time`,
 1 AS `rent`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `temp`
--

DROP TABLE IF EXISTS `temp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `temp` (
  `logistic_unit_id` int NOT NULL,
  `trans_type` char(20) DEFAULT NULL,
  `rent` int DEFAULT NULL,
  `available` char(5) DEFAULT NULL,
  PRIMARY KEY (`logistic_unit_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `temp`
--

LOCK TABLES `temp` WRITE;
/*!40000 ALTER TABLE `temp` DISABLE KEYS */;
/*!40000 ALTER TABLE `temp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `name` char(20) DEFAULT NULL,
  `email` char(20) DEFAULT NULL,
  `startdate` date NOT NULL,
  `loc` char(20) DEFAULT NULL,
  `time` int NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (5,'john','xyz@gmail.com','2000-12-25','ssss',12),(6,'Nobdy','abc@email.com','2000-12-23','middle of nowhere',2),(7,'Nytik','xyz@gmail.com','2012-12-12','baci',8),(10,'somename','somemail@yahoo.com','2022-12-01','bengalurur',4),(15,'Rama','newram@ram.com','2022-12-01','hosur',5);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `validate_time` BEFORE INSERT ON `users` FOR EACH ROW BEGIN CALL validate_customer( NEW.time); END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `summary`
--

/*!50001 DROP VIEW IF EXISTS `summary`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `summary` AS select `manages`.`logistic_unit_id` AS `logistic_unit_id`,`manages`.`user_id` AS `user_id`,`users`.`name` AS `name`,`users`.`email` AS `email`,`users`.`time` AS `time`,`logistic_units`.`rent` AS `rent` from ((`manages` join `users` on((`manages`.`user_id` = `users`.`user_id`))) join `logistic_units` on((`manages`.`logistic_unit_id` = `logistic_units`.`logistic_unit_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-02  2:28:35
