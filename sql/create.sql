CREATE USER 'mba'@'localhost' IDENTIFIED BY 'mba';
DROP DATABASE IF EXISTS multi_brand_automation;
CREATE DATABASE multi_brand_automation;
GRANT ALL PRIVILEGES ON multi_brand_automation.* TO 'mba'@'localhost';
