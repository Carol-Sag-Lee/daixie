CREATE DATABASE  IF NOT EXISTS `daixie` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `daixie`;
-- MySQL dump 10.13  Distrib 5.5.32, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: daixie
-- ------------------------------------------------------
-- Server version	5.5.32-0ubuntu0.12.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(45) NOT NULL,
  `passwd` varchar(45) NOT NULL,
  `type` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'ls09@software.nju.edu.cn','96e79218965eb72c92a549dd5a330112','0');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order` (
  `id` int(11) NOT NULL,
  `user_id` int(11) unsigned NOT NULL COMMENT '用户id',
  `cs_id` int(11) unsigned NOT NULL COMMENT '客服id',
  `solver_id` int(11) unsigned NOT NULL COMMENT '解题员id',
  `status` tinyint(4) NOT NULL COMMENT '订单状态',
  `create_time` datetime NOT NULL,
  `require_time` datetime NOT NULL COMMENT '要求时间',
  `expect_time` datetime NOT NULL COMMENT '预计时间',
  `title` varchar(45) DEFAULT NULL COMMENT '标题',
  `description` varchar(4096) DEFAULT NULL COMMENT '描述',
  `supp_info` varchar(1024) DEFAULT NULL COMMENT '辅助信息',
  `log` varchar(1024) DEFAULT NULL COMMENT '日志',
  `expect_hour` float DEFAULT NULL COMMENT '预计耗时',
  `actual_hour` float DEFAULT NULL COMMENT '实际耗时',
  `extra_item` varchar(45) DEFAULT NULL COMMENT '其他事项',
  `extra_money` varchar(45) DEFAULT NULL COMMENT '其他金额',
  `order_price` float DEFAULT NULL COMMENT '订单价格',
  PRIMARY KEY (`id`),
  KEY `fk_order_1_idx` (`user_id`,`cs_id`),
  KEY `fk_order_2_idx` (`cs_id`),
  KEY `fk_order_1_idx1` (`user_id`,`solver_id`),
  KEY `fk_order_2_idx1` (`solver_id`),
  CONSTRAINT `fk_order_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_2` FOREIGN KEY (`solver_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_3` FOREIGN KEY (`cs_id`) REFERENCES `admin` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,3,1,4,0,'2014-02-20 00:00:00','2014-02-21 00:00:00','2014-02-21 00:00:00','title','description','supp_info','log',4,5,'extra_item','extra_money',100);
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(45) NOT NULL,
  `passwd` varchar(45) NOT NULL,
  `activate` int(11) DEFAULT NULL,
  `type` int(11) NOT NULL,
  `nickname` varchar(45) DEFAULT NULL,
  `sex` int(11) DEFAULT NULL,
  `description` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (3,'ls09@software.nju.edu.cn','96e79218965eb72c92a549dd5a330112',1,0,'Routh_Luo',0,'Routh...'),(4,'mf1332041@software.nju.edu.cn','96e79218965eb72c92a549dd5a330112',1,1,'mf1332041',0,'mf1332041');
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

-- Dump completed on 2014-02-22 12:23:09
