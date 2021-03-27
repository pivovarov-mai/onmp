CREATE USER 'pivovar'@'localhost' IDENTIFIED BY 'gfctxybr';
CREATE USER 'onmp'@'localhost' IDENTIFIED BY 'dautova';
GRANT SELECT,INSERT,DELETE,UPDATE ON mp.* TO 'onmp'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'onmp'@'localhost';
