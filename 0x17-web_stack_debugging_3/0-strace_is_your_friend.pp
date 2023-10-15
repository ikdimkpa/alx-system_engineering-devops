# Changes the wrong spelling 'phpp' extensions to 'php' the settings file 'wp-settings.php'.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin/'
}
