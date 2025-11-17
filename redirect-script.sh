#!/bin/bash
# Salva come generate_redirects.sh e rendilo eseguibile con: chmod +x generate_redirects.sh

# Directory di output di Jekyll
BUILD_DIR="_site"

# Cerca tutte le directory che potrebbero necessitare di reindirizzamenti
find "$BUILD_DIR/news" -type d -mindepth 1 | while read -r dir; do
  # Estrai il nome della directory
  name=$(basename "$dir")
  
  # Crea un file di reindirizzamento HTML se non esiste già
  if [ ! -f "$BUILD_DIR/news/$name.html" ]; then
    echo "Creazione reindirizzamento per $name"
    cat > "$BUILD_DIR/news/$name.html" << EOF
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Redirecting...</title>
    <meta http-equiv="refresh" content="0; URL=$name/">
    <link rel="canonical" href="$name/">
  </head>
  <body>
    <p>Redirecting to <a href="$name/">$name/</a>...</p>
  </body>
</html>
EOF
  fi
done
