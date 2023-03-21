<?php

// Caminho absoluto da pasta que será protegida
$folder_path = '/caminho/para/pasta';

// ID da chave pública PGP
$key_id = '12345678';

// Configuração do objeto GnuPG
$gpg = new gnupg();
$gpg->seterrormode(gnupg::ERROR_EXCEPTION);

// Importa a chave pública PGP
$public_key = file_get_contents('caminho/para/chave_publica.asc');
$imported_keys = $gpg->import($public_key);
$imported_key_id = $imported_keys['fingerprint'];

// Verifica se a chave pública importada é a mesma que será utilizada
if ($imported_key_id != $key_id) {
    throw new Exception('A chave pública importada é diferente da chave pública especificada.');
}

// Obtém o conteúdo do arquivo que será protegido
$file_contents = file_get_contents($folder_path);

// Cria o arquivo criptografado utilizando a chave pública PGP
$encrypted_file = $gpg->encrypt($file_contents, $key_id);

// Escreve o arquivo criptografado na pasta protegida
file_put_contents($folder_path . '/arquivo_protegido.gpg', $encrypted_file);

// Remove o arquivo original
unlink($folder_path);

?>
