# Fix "too many files open" error by setting the ULIMIT to a large enough value

file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='-n 2048'\n",
}
