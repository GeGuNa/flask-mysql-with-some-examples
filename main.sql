-- MySQL dump 10.19  Distrib 10.3.39-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: qwerty
-- ------------------------------------------------------
-- Server version	10.3.39-MariaDB-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `apartments`
--

DROP TABLE IF EXISTS `apartments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `apartments` (
  `uid` bigint(64) NOT NULL AUTO_INCREMENT,
  `titlea` text DEFAULT '',
  `when_posted` bigint(64) DEFAULT 0,
  `picurl` text DEFAULT '',
  `postedby` bigint(64) DEFAULT 0,
  `details` text DEFAULT '',
  `where` text DEFAULT '',
  `size` text DEFAULT '',
  `floor` text DEFAULT '',
  PRIMARY KEY (`uid`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apartments`
--

LOCK TABLES `apartments` WRITE;
/*!40000 ALTER TABLE `apartments` DISABLE KEYS */;
INSERT INTO `apartments` VALUES (1,'qqqqqq',0,'',0,'zzzzz:15,aae12:151','','1454',''),(2,'qqqqqq22222',0,'',0,'zzzzz:15,aae12:1551','','14544',''),(3,'qqqqqq22222',0,'',0,'zzzzz:15,aae12:1551','','14544',''),(4,'qqqqqq22222',0,'',0,'zzzzz:15,aae12:1551','','14544',''),(5,'qqqqqq22222',0,'',0,'zzzzz:15,aae12:1551','','14544',''),(6,'qqqqqq22222',0,'',0,'zzzzz:15,aae12:1551','','14544',''),(7,'qqqqqq22222',0,'',0,'zzzzz:15,aae12:1551','','1645454','');
/*!40000 ALTER TABLE `apartments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog`
--

DROP TABLE IF EXISTS `blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog` (
  `uid` bigint(64) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT '',
  `text` longtext DEFAULT NULL,
  `when` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `unix_time` bigint(64) DEFAULT NULL,
  `user` bigint(64) NOT NULL,
  `cat_id` bigint(64) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` VALUES (1,'ahaha','whocares????','2024-03-23 20:50:23',NULL,1,NULL),(2,'ahaha2','whocares????2','2024-03-23 20:50:32',NULL,12,NULL),(3,'ahaha24','whocares????3333333333333333332','2024-03-23 20:50:40',NULL,123,NULL);
/*!40000 ALTER TABLE `blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `name` text DEFAULT NULL,
  `surname` text DEFAULT NULL,
  `added_time` int(32) NOT NULL,
  `gender` set('male','female','who_cares') DEFAULT 'male',
  `username` varchar(100) DEFAULT '',
  `email` varchar(1000) DEFAULT '',
  `password` varchar(1024) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'eqqweqweqwe','qweqweqweq',124123,'male','','',''),(2,'eqqweqweqwe','qweqweqweq',124123,'male','','',''),(3,'eqqweqweqwe','qweqweqweq',124123,'male','','',''),(4,'eqqweqweqwe','qweqweqweq',124123,'male','','',''),(5,'eqqweqweqwe_42','qweqweqweeeeeeeq',112412333,'male','','',''),(6,'aba','qweqweqweeeeeeeq',112412333,'male','','',''),(7,'aba','qweqweqweeeeeeeq',112412333,'male','','',''),(8,'abuhuh','qwe_11',12412313,'male','','',''),(9,'abuhuh','qwe_11',12412313,'male','','',''),(10,'abuhuhqwe_123','qwe_11',12412313,'male','','',''),(11,'abuhuhqwe_123','qwe_11',12412313,'male','','',''),(12,'qq_1','surname',12313,'male','FoLLeN','gegs@gmail.com','123456');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-29  1:15:12
