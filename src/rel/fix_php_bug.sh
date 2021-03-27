#!/usr/bin/bash

sed 's/\|\| \(count\(\$analyzed_sql_results\[\'select_expr\'\] == 1\)/\|\| \(\(count\(\$analyzed_sql_results\[\'select_expr\'\]\) == 1\)/' /usr/share/phpmyadmin/libraries/sql.lib.php
