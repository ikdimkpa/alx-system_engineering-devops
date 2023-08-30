#puppet to install & configure Nginx
  2
  3 package { 'nginx':
  4   ensure => installed,
  5 }
  6
  7 file_line { 'server_config':
  8   ensure => 'present',
  9   path   => '/etc/nginx/sites-available/default',
 10   after  => 'listen 80 default_server;',
 11   line   => 'rewrite ^/redirect_me https://stackoverflow.com/ permanent;',
 12 }
 13
 14 file { '/var/www/html/index.html':
 15   content => 'Hello World!',
 16 }
 17
 18 service { 'nginx':
 19   ensure  => running,
 20   require => Package['nginx'],
 21 }
