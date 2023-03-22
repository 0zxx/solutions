#!/bin/bash

# Ask for the path of the browser profile
read -p "Enter the path of the browser profile: " profile_path

# Encrypt the specified files
cd "$profile_path"
tar -czvf profile.tar.gz containers.json cookies.sqlite places.sqlite prefs.js storage.sqlite
read -p "Do you want to encrypt using GPG or a password? [GPG/password]: " encryption_type

if [ "$encryption_type" == "GPG" ]; then
  # Ask if the user wants to create a new GPG key or use an existing one
  read -p "Do you want to create a new GPG key or use an existing one? [new/existing]: " gpg_key_choice

  if [ "$gpg_key_choice" == "new" ]; then
    # Create a new GPG key
    gpg --full-gen-key
    read -p "Enter your GPG key ID: " gpg_key_id
  else
    # Use an existing GPG key
    read -p "Enter your GPG key ID: " gpg_key_id
  fi

  # Encrypt the archive with the GPG key
  gpg -e -r "$gpg_key_id" profile.tar.gz
else
  # Encrypt the archive with a password
  read -s -p "Enter the password: " encryption_password
  echo "$encryption_password" | zip -P - profile.zip profile.tar.gz
fi

# Remove all logs of the operation
shred -u profile.tar.gz

# Move the encrypted file to the user's home directory
mv profile.tar.gz.gpg /home/$USER/
