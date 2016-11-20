-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.1.18-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- vic 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `vic` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `vic`;


-- 테이블 vic.ck_troop 구조 내보내기
DROP TABLE IF EXISTS `ck_troop`;
CREATE TABLE IF NOT EXISTS `ck_troop` (
  `ID` int(11) NOT NULL,
  `location` varchar(50) DEFAULT NULL,
  `culture` varchar(50) NOT NULL,
  `heavyinf` int(10) unsigned zerofill NOT NULL,
  `lightinf` int(10) unsigned zerofill NOT NULL,
  `pikes` int(10) unsigned zerofill NOT NULL,
  `archers` int(10) unsigned zerofill NOT NULL,
  `knights` int(10) unsigned zerofill NOT NULL,
  `special` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 vic.ck_troop:~0 rows (대략적) 내보내기
DELETE FROM `ck_troop`;
/*!40000 ALTER TABLE `ck_troop` DISABLE KEYS */;
/*!40000 ALTER TABLE `ck_troop` ENABLE KEYS */;


-- 테이블 vic.indy 구조 내보내기
DROP TABLE IF EXISTS `indy`;
CREATE TABLE IF NOT EXISTS `indy` (
  `indy_id` int(11) NOT NULL AUTO_INCREMENT,
  `indy_loc` int(11) NOT NULL,
  `required_res` varchar(50) DEFAULT NULL,
  `produce` varchar(50) NOT NULL,
  `jobs` int(11) NOT NULL,
  PRIMARY KEY (`indy_id`),
  KEY `FK_rgo_province` (`indy_loc`),
  CONSTRAINT `FK_rgo_province` FOREIGN KEY (`indy_loc`) REFERENCES `province` (`prov_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 vic.indy:~0 rows (대략적) 내보내기
DELETE FROM `indy`;
/*!40000 ALTER TABLE `indy` DISABLE KEYS */;
/*!40000 ALTER TABLE `indy` ENABLE KEYS */;


-- 테이블 vic.market 구조 내보내기
DROP TABLE IF EXISTS `market`;
CREATE TABLE IF NOT EXISTS `market` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `prod_name` char(50) NOT NULL,
  `price` decimal(10,0) NOT NULL,
  `stock` int(10) unsigned zerofill NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 vic.market:~0 rows (대략적) 내보내기
DELETE FROM `market`;
/*!40000 ALTER TABLE `market` DISABLE KEYS */;
/*!40000 ALTER TABLE `market` ENABLE KEYS */;


-- 테이블 vic.party 구조 내보내기
DROP TABLE IF EXISTS `party`;
CREATE TABLE IF NOT EXISTS `party` (
  `party_id` int(11) NOT NULL,
  `party_name` varchar(50) DEFAULT NULL,
  `ideology` varchar(50) DEFAULT NULL,
  `trade` varchar(50) DEFAULT NULL,
  `economy` varchar(50) DEFAULT NULL,
  `religion` varchar(50) DEFAULT NULL,
  `citizen` varchar(50) DEFAULT NULL,
  `military` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`party_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 vic.party:~2 rows (대략적) 내보내기
DELETE FROM `party`;
/*!40000 ALTER TABLE `party` DISABLE KEYS */;
INSERT INTO `party` (`party_id`, `party_name`, `ideology`, `trade`, `economy`, `religion`, `citizen`, `military`) VALUES
	(1, 'conservatives', 'conservative', 'free', 'laissez', 'moralism', 'residency', 'jingo'),
	(2, 'liberal', 'liberal', 'protect', 'interventionism', 'pluralism', 'full', 'pro');
/*!40000 ALTER TABLE `party` ENABLE KEYS */;


-- 테이블 vic.pop 구조 내보내기
DROP TABLE IF EXISTS `pop`;
CREATE TABLE IF NOT EXISTS `pop` (
  `pop_id` int(11) NOT NULL AUTO_INCREMENT,
  `occupation` int(11) DEFAULT '0',
  `location` int(11) DEFAULT NULL,
  `popclass` char(50) DEFAULT 'workers',
  `ideology` char(50) DEFAULT NULL,
  `religion` char(50) DEFAULT NULL,
  `population` int(11) DEFAULT NULL,
  `primeissue` char(50) DEFAULT NULL,
  `secissue` char(50) DEFAULT NULL,
  `conscious` int(11) DEFAULT '0',
  `revanchism` int(11) DEFAULT '0',
  `money` double DEFAULT '10',
  `one_party` char(50) DEFAULT NULL,
  `two_party` char(50) DEFAULT NULL,
  `support` int(11) DEFAULT '10',
  PRIMARY KEY (`pop_id`),
  KEY `FK_pop_province` (`location`),
  KEY `FK_pop_rgo` (`occupation`),
  KEY `FK_pop_party` (`one_party`),
  KEY `FK_pop_party_2` (`two_party`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- 테이블 데이터 vic.pop:~21 rows (대략적) 내보내기
DELETE FROM `pop`;
/*!40000 ALTER TABLE `pop` DISABLE KEYS */;
INSERT INTO `pop` (`pop_id`, `occupation`, `location`, `popclass`, `ideology`, `religion`, `population`, `primeissue`, `secissue`, `conscious`, `revanchism`, `money`, `one_party`, `two_party`, `support`) VALUES
	(2, 0, NULL, 'farmers', 'anarcho-liberal', 'taoist', 41411, 'anti', 'residency', 0, 0, 10, NULL, NULL, 10),
	(3, 0, NULL, 'slaves', 'liberal', 'taoist', 76585, 'free', 'jingo', 0, 0, 10, NULL, NULL, 10),
	(4, 0, NULL, 'clerks', 'fascist', 'taoist', 17728, 'laissez', 'free', 0, 0, 10, NULL, NULL, 10),
	(5, 0, NULL, 'soldiers', 'communist', 'taoist', 36920, 'anti', 'protect', 0, 0, 10, NULL, NULL, 10),
	(6, 0, NULL, 'capitalists', 'reactionary', 'taoist', 47515, 'free', 'limited', 0, 0, 10, NULL, NULL, 10),
	(7, 0, NULL, 'officers', 'conservative', 'taoist', 49365, 'state', 'secular', 0, 0, 10, NULL, NULL, 10),
	(8, 0, NULL, 'craftsmen', 'reactionary', 'taoist', 71003, 'anti', 'pluralism', 0, 0, 10, NULL, NULL, 10),
	(9, 0, NULL, 'craftsmen', 'fascist', 'taoist', 50157, 'planned', 'free', 0, 0, 10, NULL, NULL, 10),
	(10, 0, NULL, 'clerks', 'reactionary', 'taoist', 65672, 'jingo', 'laissez', 0, 0, 10, NULL, NULL, 10),
	(11, 0, NULL, 'laborers', 'reactionary', 'taoist', 29260, 'pro', 'full', 0, 0, 10, NULL, NULL, 10),
	(12, 0, NULL, 'capitalists', 'reactionary', 'taoist', 58056, 'moralism', 'pacifist', 0, 0, 10, NULL, NULL, 10),
	(13, 0, NULL, 'slaves', 'communist', 'taoist', 53417, 'state', 'limited', 0, 0, 10, NULL, NULL, 10),
	(14, 0, NULL, 'breaucrats', 'reactionary', 'taoist', 16109, 'protect', 'limited', 0, 0, 10, NULL, NULL, 10),
	(15, 0, NULL, 'farmers', 'liberal', 'taoist', 41313, 'moralism', 'free', 0, 0, 10, NULL, NULL, 10),
	(16, 0, NULL, 'artisans', 'fascist', 'taoist', 62345, 'laissez', 'anti', 0, 0, 10, NULL, NULL, 10),
	(17, 0, NULL, 'breaucrats', 'communist', 'taoist', 48656, 'residency', 'laissez', 0, 0, 10, NULL, NULL, 10),
	(18, 0, NULL, 'slaves', 'communist', 'taoist', 65085, 'residency', 'protect', 0, 0, 10, NULL, NULL, 10),
	(19, 0, NULL, 'soldiers', 'liberal', 'taoist', 40185, 'pluralism', 'planned', 0, 0, 10, NULL, NULL, 10),
	(20, 0, NULL, 'laborers', 'fascist', 'taoist', 69650, 'moralism', 'state', 0, 0, 10, NULL, NULL, 10),
	(21, 0, NULL, 'slaves', 'fascist', 'taoist', 72779, 'secular', 'protect', 0, 0, 10, NULL, NULL, 10),
	(22, 0, NULL, 'capitalists', 'communist', 'taoist', 70320, 'residency', 'anti', 0, 0, 10, NULL, NULL, 10);
/*!40000 ALTER TABLE `pop` ENABLE KEYS */;


-- 테이블 vic.province 구조 내보내기
DROP TABLE IF EXISTS `province`;
CREATE TABLE IF NOT EXISTS `province` (
  `prov_id` int(11) NOT NULL AUTO_INCREMENT,
  `prov_name` char(50) NOT NULL,
  `resource` char(50) NOT NULL,
  `rgo` int(11) NOT NULL,
  `industryjobs` int(11) NOT NULL,
  `industry` char(50) NOT NULL,
  `life` int(11) NOT NULL DEFAULT '50',
  `corruption` char(50) DEFAULT NULL,
  PRIMARY KEY (`prov_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 vic.province:~0 rows (대략적) 내보내기
DELETE FROM `province`;
/*!40000 ALTER TABLE `province` DISABLE KEYS */;
/*!40000 ALTER TABLE `province` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
