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

-- test 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `test` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `test`;


-- 테이블 test.pop 구조 내보내기
DROP TABLE IF EXISTS `pop`;
CREATE TABLE IF NOT EXISTS `pop` (
  `popid` int(11) DEFAULT NULL,
  `location` int(11) DEFAULT NULL,
  `ideology` int(11) DEFAULT NULL,
  `primeissue` int(11) DEFAULT NULL,
  `secissue` int(11) DEFAULT NULL,
  `열 6` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 test.pop:~0 rows (대략적) 내보내기
DELETE FROM `pop`;
/*!40000 ALTER TABLE `pop` DISABLE KEYS */;
/*!40000 ALTER TABLE `pop` ENABLE KEYS */;


-- 테이블 test.province 구조 내보내기
DROP TABLE IF EXISTS `province`;
CREATE TABLE IF NOT EXISTS `province` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `prov_name` char(50) NOT NULL,
  `resource` char(50) NOT NULL,
  `life` int(11) NOT NULL DEFAULT '50',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 test.province:~0 rows (대략적) 내보내기
DELETE FROM `province`;
/*!40000 ALTER TABLE `province` DISABLE KEYS */;
/*!40000 ALTER TABLE `province` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
