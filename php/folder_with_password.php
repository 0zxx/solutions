<?php

// Pasta protegida por senha
$protected_folder = 'pasta_protegida';

// Nome de usuário e senha a serem adicionados
$username = 'usuario';
$password = 'senha';

// Caminho para o arquivo de senha
$password_file = '/caminho/para/arquivo/senha/.htpasswd';

// Executa o comando htpasswd para adicionar o usuário/senha ao arquivo
system('htpasswd -b ' . $password_file . ' ' . $username . ' ' . $password);

// Cria um arquivo .htaccess na pasta protegida
$htaccess_file = fopen($protected_folder . '/.htaccess', 'w');

// Escreve as regras do Apache no arquivo .htaccess
fwrite($htaccess_file, "AuthType Basic\n");
fwrite($htaccess_file, "AuthName 'Acesso restrito'\n");
fwrite($htaccess_file, "AuthUserFile " . $password_file . "\n");
fwrite($htaccess_file, "Require valid-user\n");

// Fecha o arquivo .htaccess
fclose($htaccess_file);

?>
