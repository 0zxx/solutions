<?php
// URL do arquivo zip que você deseja baixar
$url = 'http://example.com/arquivo.zip';

// Nome do arquivo zip que será salvo localmente
$zipFile = 'arquivo.zip';

// Diretório onde o arquivo zip será salvo localmente
$localDir = '/var/www/html/';

// Baixa o arquivo zip e salva localmente
file_put_contents($localDir . $zipFile, file_get_contents($url));

// Cria um novo objeto ZipArchive
$zip = new ZipArchive;

// Abre o arquivo zip
if ($zip->open($localDir . $zipFile) === TRUE) {

    // Extrai os arquivos do arquivo zip para o diretório local
    $zip->extractTo($localDir);

    // Fecha o arquivo zip
    $zip->close();

    // Exibe uma mensagem informando que o arquivo foi extraído com sucesso
    echo 'Arquivo extraído com sucesso';

} else {

    // Exibe uma mensagem de erro se não foi possível abrir o arquivo zip
    echo 'Erro ao abrir o arquivo zip';

}
?>
