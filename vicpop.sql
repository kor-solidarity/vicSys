-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.1.16-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

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
  `party_ID` int(11) NOT NULL,
  `partyname` varchar(50) DEFAULT NULL,
  `ideology` varchar(50) DEFAULT NULL,
  `trade` varchar(50) DEFAULT NULL,
  `economy` varchar(50) DEFAULT NULL,
  `religion` varchar(50) DEFAULT NULL,
  `citizen` varchar(50) DEFAULT NULL,
  `military` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`party_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 vic.party:~0 rows (대략적) 내보내기
DELETE FROM `party`;
/*!40000 ALTER TABLE `party` DISABLE KEYS */;
/*!40000 ALTER TABLE `party` ENABLE KEYS */;


-- 테이블 vic.pop 구조 내보내기
DROP TABLE IF EXISTS `pop`;
CREATE TABLE IF NOT EXISTS `pop` (
  `pop_id` int(11) NOT NULL AUTO_INCREMENT,
  `occupation` int(11) NOT NULL DEFAULT '0',
  `location` int(11) NOT NULL,
  `popclass` char(50) NOT NULL DEFAULT 'workers',
  `ideology` char(50) NOT NULL,
  `religion` char(50) NOT NULL,
  `population` int(11) NOT NULL,
  `primeissue` char(50) NOT NULL,
  `secissue` char(50) NOT NULL,
  `conscious` int(11) NOT NULL DEFAULT '0',
  `revanchism` int(11) NOT NULL,
  `money` int(11) NOT NULL,
  `one_party` int(11) NOT NULL,
  `two_party` int(11) DEFAULT NULL,
  `support` int(11) NOT NULL DEFAULT '10',
  PRIMARY KEY (`pop_id`),
  KEY `FK_pop_province` (`location`),
  KEY `FK_pop_rgo` (`occupation`),
  KEY `FK_pop_party` (`one_party`),
  KEY `FK_pop_party_2` (`two_party`),
  CONSTRAINT `FK_pop_party` FOREIGN KEY (`one_party`) REFERENCES `party` (`party_ID`),
  CONSTRAINT `FK_pop_party_2` FOREIGN KEY (`two_party`) REFERENCES `party` (`party_ID`),
  CONSTRAINT `FK_pop_province` FOREIGN KEY (`location`) REFERENCES `province` (`prov_ID`),
  CONSTRAINT `FK_pop_rgo` FOREIGN KEY (`occupation`) REFERENCES `indy` (`indy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 vic.pop:~0 rows (대략적) 내보내기
DELETE FROM `pop`;
/*!40000 ALTER TABLE `pop` DISABLE KEYS */;
/*!40000 ALTER TABLE `pop` ENABLE KEYS */;


-- 테이블 vic.province 구조 내보내기
DROP TABLE IF EXISTS `province`;
CREATE TABLE IF NOT EXISTS `province` (
  `prov_ID` int(11) NOT NULL AUTO_INCREMENT,
  `prov_name` char(50) NOT NULL,
  `resource` char(50) NOT NULL,
  `rgo` int(11) NOT NULL,
  `industryjobs` int(11) NOT NULL,
  `industry` char(50) NOT NULL,
  `life` int(11) NOT NULL DEFAULT '50',
  `corruption` char(50) DEFAULT NULL,
  PRIMARY KEY (`prov_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 vic.province:~0 rows (대략적) 내보내기
DELETE FROM `province`;
/*!40000 ALTER TABLE `province` DISABLE KEYS */;
/*!40000 ALTER TABLE `province` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
