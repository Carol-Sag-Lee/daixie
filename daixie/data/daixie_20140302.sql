CREATE DATABASE  IF NOT EXISTS `daixie` /*!40100 DEFAULT CHARACTER SET utf8 */;
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
  `type` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'admin@admin.com','96e79218965eb72c92a549dd5a330112',1),(2,'cs01@cs01.com','96e79218965eb72c92a549dd5a330112',0),(4,'air_don@qq.com','96e79218965eb72c92a549dd5a330112',0);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
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
  `grade` int(11) DEFAULT NULL,
  `expect_hour` float DEFAULT NULL COMMENT '预计耗时',
  `actual_hour` float DEFAULT NULL COMMENT '实际耗时',
  `extra_item` varchar(45) DEFAULT NULL COMMENT '其他事项',
  `extra_money` varchar(45) DEFAULT NULL COMMENT '其他金额',
  `order_price` float DEFAULT NULL COMMENT '订单价格',
  PRIMARY KEY (`id`),
  KEY `fk_order_1_idx` (`user_id`,`cs_id`),
  KEY `fk_order_1_idx1` (`user_id`,`solver_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,6,2,6,0,'2014-03-02 13:11:33','2014-02-25 00:00:00','2014-02-28 00:00:00','数据库作业','数据库两次作业','几份作业文件','创建订单。',0,6,NULL,'认真完成','20',NULL),(2,5,2,6,0,'2014-03-02 13:22:58','2014-02-25 00:00:00','2014-02-28 00:00:00','质量管理论文','软件质量管理期末论文','无','创建订单。',0,15,NULL,'不得抄袭','100',NULL),(3,8,4,11,0,'2014-03-02 14:38:53','2014-04-05 00:00:00','2014-04-01 00:00:00','java 2','first order','fuzhu','log1',2,5,0,'no have','20',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (3,'ls09@software.nju.edu.cn','96e79218965eb72c92a549dd5a330112',1,0,'Routh_Luo',0,'Routh...'),(4,'mf1332041@software.nju.edu.cn','96e79218965eb72c92a549dd5a330112',1,1,'mf1332041',0,'mf1332041'),(5,'262617697@qq.com','e10adc3949ba59abbe56e057f20f883e',0,0,'',0,''),(6,'routh@foxmail.com','e10adc3949ba59abbe56e057f20f883e',0,0,'',0,''),(8,'mf1332018@software.nju.edu.cn','96e79218965eb72c92a549dd5a330112',1,0,'',0,''),(9,'air_don@qq.com','96e79218965eb72c92a549dd5a330112',0,0,'',0,''),(11,'solver@qq.com','96e79218965eb72c92a549dd5a330112',0,1,'',0,'');
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

-- Dump completed on 2014-03-02 21:00:38
