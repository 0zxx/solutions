#!/bin/bash

# Define o nome do arquivo ISO
iso_name="lubuntu_lobster.iso"

# Monta o sistema de arquivos raiz em um diretório temporário
tmp_dir=$(mktemp -d)
sudo mount /dev/sda1 $tmp_dir

# Cria o arquivo ISO com o sistema de arquivos raiz
sudo mkisofs -o $iso_name -r $tmp_dir

# Desmonta o sistema de arquivos raiz
sudo umount $tmp_dir
rmdir $tmp_dir

# Fim do script
