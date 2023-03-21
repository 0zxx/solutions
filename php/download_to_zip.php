<?php
// Defina a URL da pasta que deseja baixar
$url = 'http://exemplo.com/minha-pasta.zip';

// Defina o nome do arquivo zip
$nome_arquivo_zip = 'minha-pasta.zip';

// Defina o caminho do diretório de destino
$caminho_destino = '/caminho/para/destino/';

// Crie um novo objeto ZipArchive
$zip = new ZipArchive();

// Abra o arquivo zip para escrita
if ($zip->open($caminho_destino . $nome_arquivo_zip, ZIPARCHIVE::CREATE) !== true) {
    die('Não foi possível criar o arquivo zip');
}

// Faça o download da pasta zipada
$pasta_zipada = file_get_contents($url);

// Adicione o conteúdo da pasta zipada ao arquivo zip
$zip->addFromString('minha-pasta/', $pasta_zipada);

// Feche o arquivo zip
$zip->close();

// Verifique se não ocorreu nenhum erro durante o processo
if (!file_exists($caminho_destino . $nome_arquivo_zip)) {
    die('Não foi possível salvar o arquivo zip no servidor');
}

echo 'A pasta foi baixada e salva como ' . $caminho_destino . $nome_arquivo_zip;
?>
