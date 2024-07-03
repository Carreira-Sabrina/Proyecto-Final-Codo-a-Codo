-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: hotel
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `excursion`
--

DROP TABLE IF EXISTS `excursion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `excursion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `descripcion` text COLLATE utf8mb3_spanish_ci NOT NULL,
  `destino` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `precio_por_persona` int NOT NULL,
  `url_imagen` varchar(300) COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `excursion`
--

LOCK TABLES `excursion` WRITE;
/*!40000 ALTER TABLE `excursion` DISABLE KEYS */;
INSERT INTO `excursion` VALUES (1,'Visita al Viñedo Sor Juana Inés de La Cruz','\rViñedo Sor Juana Inés de la Cruz: Un oasis de paz y sabor en Mendoza\r. Embárcate en un viaje sensorial inolvidable en el Viñedo Sor Juana Inés de la Cruz, ubicado en el corazón de la provincia de Mendoza, Argentina. Rodeado de un paisaje de ensueño, entre imponentes montañas y viñedos interminables, este oasis de paz te invita a descubrir la magia de la elaboración del vino y a deleitarte con sabores únicos.Recorre los viñedos: Pasea entre las hileras de vides cargadas de racimos de uvas, admira la belleza natural del lugar y aprende sobre el proceso de cultivo de la vid. Descubre los secretos de la elaboración del vino: Explora la bodega y presenciarás el proceso de vinificación de principio a fin, desde el prensado de las uvas hasta el añejamiento en barricas de roble. Degusta vinos excepcionales: Disfruta de una degustación guiada de los mejores vinos de Sor Juana Inés de la Cruz. Saborea la variedad de sabores y aromas que cada uno de ellos tiene para ofrecer.','Mendoza',15000,'https://images.unsplash.com/photo-1592783914986-a489c83c7aea?q=80&w=2114&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),(2,'Isla Victoria y Bosque de Arrayanes','Partiendo desde Puerto Pañuelo, en la imponente península de Llao Llao y tras una hora de navegación, se arriba a la península de Quetrihue, ubicada en el noreste del lago Nahuel Huapi, en donde se encuentra el legendario bosque de arrayanes. El arrayán (“quetrihue” en lengua mapuche) es un arbusto de exquisito color azafrán y flores blancas. En este lugar, único en el mundo, toma envergadura arbórea para formar un mágico e inusual bosque. \nLuego de recorrer este escenario incomparable, se navega hacia Puerto Anchorena, en la Isla Victoria, donde encontrarás una flora prolífica en especies de gran atractivo visual. \nRecorriendo los senderos de esta hermosa y milenaria isla se llega hasta Playa del Toro, en donde se pueden observar las pinturas rupestres hechas por los pueblos originarios que habitaban en esta zona, en el marco de una espléndida playa de arena volcánica. ¡Es una experiencia inolvidable!','Bariloche',45000,'https://images.unsplash.com/photo-1655282224856-7090df8a6286?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),(3,'Paseo de los Colorados','De aproximadamente 3 Km de largo, este circuito recorre parte del lecho del río Tumbaya (afluente del Purmamarca), a espaldas del Cerro de Siete Colores. De dificultad baja, y aproximadamente 1 hora de duración.\nSe puede realizar el circuito en cualquier momento del día pero se recomienda durante la tarde. Guías locales ofrecen caminatas nocturnas. especialmente atractivas en noches estrelladas.\nRecomendamos llevar agua, sombrero y anteojos de sol.','Jujuy',23000,'https://images.unsplash.com/photo-1630095854527-bde56777c63c?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
/*!40000 ALTER TABLE `excursion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-02 23:05:10
