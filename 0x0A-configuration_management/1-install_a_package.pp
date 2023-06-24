# Install flask version 2.1.0 using puppet

package { 'pip3':
ensure => 'latest',
provider => 'pip',
}

package { 'flask':
ensure => '2.1.0',
provider => 'pip',
require => Package['pip3'],
}
