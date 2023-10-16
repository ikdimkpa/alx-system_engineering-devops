# Changes the wrong spelling 'phpp' extensions to 'php' the settings file 'wp-settings.php'.

file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => inline_template('<%= File.read("/var/www/html/wp-settings.php").gsub(/\.phpp/, ".php")  %>')
}
