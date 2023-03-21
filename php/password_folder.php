<?php
$htpasswd_file = '/caminho/para/arquivo/.htpasswd';
$htpasswd_users = array('usuario1' => 'senha1', 'usuario2' => 'senha2');

if (file_exists($htpasswd_file)) {
    unlink($htpasswd_file);
}

foreach ($htpasswd_users as $user => $password) {
    $hashed_password = password_hash($password, PASSWORD_BCRYPT);
    file_put_contents($htpasswd_file, "$user:$hashed_password\n", FILE_APPEND);
}

?>
