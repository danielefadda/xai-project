# Guida al Deployment del Sito XAI Project

Questa guida spiega come effettuare il deployment del sito web XAI Project su un server.

## Indice

1. [Prerequisiti](#prerequisiti)
2. [Configurazione Iniziale](#configurazione-iniziale)
3. [Metodi di Deployment](#metodi-di-deployment)
   - [Deployment su Server tramite SSH/FTP](#deployment-su-server-tramite-sshftp)
   - [Deployment con Docker](#deployment-con-docker)
   - [Deployment su GitHub Pages](#deployment-su-github-pages)
4. [Troubleshooting](#troubleshooting)

---

## Prerequisiti

Prima di procedere con il deployment, assicurati di avere installato:

- **Ruby** (versione 3.2.2 o superiore)
- **Bundler** (gem install bundler)
- **Jekyll** (verrà installato tramite bundle install)
- **Node.js e npm** (per PurgeCSS)
- **Git** (per gestione versioni)

### Installazione delle dipendenze

```bash
# Clona il repository
git clone https://github.com/danielefadda/xai-project.git
cd xai-project

# Installa le dipendenze Ruby
bundle install

# Installa PurgeCSS (opzionale, per ottimizzare i CSS)
# Opzione 1: Globale (non raccomandato)
npm install -g purgecss

# Opzione 2: Aggiungilo al progetto (raccomandato)
npm install --save-dev purgecss
# Poi usa: npx purgecss -c purgecss.config.js
```

---

## Configurazione Iniziale

### 1. Configurare URL e BaseURL

Prima di effettuare il deployment, è **fondamentale** configurare correttamente i parametri `url` e `baseurl` nel file `_config.yml`:

```yaml
# _config.yml

# Se il sito è accessibile da: https://tuodominio.com/
url: https://tuodominio.com
baseurl:  # lascia vuoto

# Se il sito è accessibile da: https://tuodominio.com/xai-project/
url: https://tuodominio.com
baseurl: /xai-project

# Esempio configurazione attuale (server CNR):
url: http://ut13.isti.cnr.it:81
baseurl:  # lascia vuoto perché il sito è alla root
```

**⚠️ Importante:** 
- Se il sito è ospitato alla root del dominio (es. `example.com`), lascia `baseurl` vuoto ma **non eliminarlo**
- Se il sito è in una sottocartella (es. `example.com/progetto`), imposta `baseurl: /progetto`

### 2. Variabili d'Ambiente

Imposta la variabile d'ambiente per la produzione:

```bash
export JEKYLL_ENV=production
```

---

## Metodi di Deployment

### Deployment su Server tramite SSH/FTP

Questo è il metodo attuale utilizzato per il deployment su `http://ut13.isti.cnr.it:81`.

#### Passo 1: Build del Sito

Genera i file statici del sito nella cartella `_site/`:

```bash
# Imposta l'ambiente di produzione
export JEKYLL_ENV=production

# Esegui il build
bundle exec jekyll build
```

Il comando genererà tutti i file statici nella directory `_site/`.

#### Passo 2: Ottimizzazione CSS (Opzionale)

Rimuovi le classi CSS non utilizzate per ridurre le dimensioni dei file:

```bash
# Usa npx se hai installato purgecss come dipendenza del progetto
npx purgecss -c purgecss.config.js

# Oppure se l'hai installato globalmente
purgecss -c purgecss.config.js
```

Questo sostituirà i file CSS in `_site/assets/css/` con versioni ottimizzate.

#### Passo 3: Trasferimento dei File

Trasferisci il contenuto della cartella `_site/` sul server tramite:

**Opzione A: SCP (SSH File Copy)**

```bash
# Copia l'intera cartella _site sul server
scp -r _site/* utente@ut13.isti.cnr.it:/percorso/directory/web/

# Esempio con porta specifica
scp -P 22 -r _site/* utente@server.com:/var/www/html/
```

**Opzione B: RSYNC (Sincronizzazione)**

```bash
# Sincronizza i file (più efficiente, trasferisce solo le modifiche)
# ⚠️ ATTENZIONE: --delete rimuove i file sul server che non esistono localmente!
# Verifica sempre il percorso di destinazione prima di usare --delete
rsync -avz --delete _site/ utente@ut13.isti.cnr.it:/percorso/directory/web/

# Con porta SSH personalizzata
rsync -avz -e "ssh -p 2222" --delete _site/ utente@server.com:/var/www/html/

# Opzione più sicura: prima fai un dry-run per vedere cosa cambierà
rsync -avz --delete --dry-run _site/ utente@server.com:/var/www/html/
```

**Opzione C: FTP/SFTP**

Puoi usare un client FTP come FileZilla o un comando da terminale:

```bash
# SFTP
sftp utente@ut13.isti.cnr.it
> cd /percorso/directory/web
> put -r _site/*
> exit
```

#### Passo 4: Verifica dei Permessi

Assicurati che i file abbiano i permessi corretti sul server:

```bash
# Connettiti via SSH
ssh utente@ut13.isti.cnr.it

# Imposta i permessi (esempio)
chmod -R 755 /percorso/directory/web
chown -R www-data:www-data /percorso/directory/web
```

#### Script di Deployment Automatico

Puoi creare uno script per automatizzare il processo:

```bash
#!/bin/bash
# deploy.sh

# Configurazione
SERVER_USER="tuoutente"
SERVER_HOST="ut13.isti.cnr.it"
SERVER_PATH="/percorso/directory/web/"

echo "🚀 Inizio deployment..."

# Build
echo "📦 Building sito..."
export JEKYLL_ENV=production
bundle exec jekyll build

# Ottimizzazione CSS
echo "🎨 Ottimizzazione CSS..."
npx purgecss -c purgecss.config.js

# Deploy
echo "📤 Trasferimento files..."
rsync -avz --delete _site/ ${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}

echo "✅ Deployment completato!"
```

Rendi lo script eseguibile e usalo:

```bash
chmod +x deploy.sh
./deploy.sh
```

---

### Deployment con Docker

Il progetto include già un Dockerfile e docker-compose per il deployment containerizzato.

#### Deployment Locale per Test

```bash
# Build e avvio con docker-compose
docker-compose up

# Il sito sarà disponibile su http://localhost:8080
```

#### Deployment su Server con Docker

**Passo 1: Build dell'Immagine Docker**

```bash
# Build dell'immagine personalizzata
docker build -t xai-project-site .

# Oppure usa l'immagine base al-folio (come definito in docker-compose.yml)
# Nota: l'immagine amirpourmand/al-folio:latest è l'immagine base del tema
docker pull amirpourmand/al-folio:latest
```

**Passo 2: Esegui il Container sul Server**

```bash
# Esegui il container
docker run -d \
  --name xai-project \
  -p 8080:8080 \
  -v $(pwd):/srv/jekyll \
  -e JEKYLL_ENV=production \
  xai-project-site

# Verifica che sia in esecuzione
docker ps
```

**Passo 3: Configurazione con Docker Compose (Produzione)**

Crea un `docker-compose.prod.yml`:

```yaml
version: "3"
services:
  jekyll:
    image: xai-project-site
    ports:
      - "80:8080"
    volumes:
      - .:/srv/jekyll
    environment:
      - JEKYLL_ENV=production
    restart: unless-stopped
```

Avvia in produzione:

```bash
docker-compose -f docker-compose.prod.yml up -d
```

---

### Deployment su GitHub Pages

Il repository è già configurato per il deployment automatico su GitHub Pages tramite GitHub Actions.

#### Configurazione Automatica (Già Attiva)

Il workflow `.github/workflows/deploy.yml` si attiva automaticamente:
- Ad ogni push sul branch `master` o `main`
- Quando vengono modificati file rilevanti (HTML, CSS, JS, Markdown, ecc.)

Il sito viene automaticamente deployato su GitHub Pages all'indirizzo:
- `https://danielefadda.github.io/xai-project/`

#### Attivazione Manuale di GitHub Pages

1. Vai su **Settings** → **Pages** nel repository GitHub
2. Seleziona **Source**: Deploy from a branch
3. Seleziona **Branch**: `gh-pages` e cartella `/ (root)`
4. Clicca **Save**

#### Deployment Manuale con Script

Puoi anche usare lo script `bin/deploy`:

```bash
# Esegui lo script di deployment
./bin/deploy

# Lo script:
# 1. Fa il build del sito
# 2. Crea un branch gh-pages
# 3. Ottimizza i CSS
# 4. Fa push su GitHub
```

**⚠️ Nota:** Assicurati di configurare correttamente `url` e `baseurl` in `_config.yml` per GitHub Pages:

```yaml
url: https://danielefadda.github.io
baseurl: /xai-project
```

---

## Troubleshooting

### Problema: Il sito non carica correttamente i CSS/JS

**Causa:** Configurazione errata di `url` e `baseurl`

**Soluzione:**
1. Verifica i valori in `_config.yml`
2. Se il sito è su `example.com/sottocartella/`, usa:
   ```yaml
   url: https://example.com
   baseurl: /sottocartella
   ```
3. Rifai il build e rideploy

### Problema: Errori durante il build

**Causa:** Dipendenze mancanti o non aggiornate

**Soluzione:**
```bash
# Aggiorna le dipendenze
bundle update

# Riprova il build
bundle exec jekyll build
```

### Problema: Immagini non vengono visualizzate

**Causa:** Percorsi relativi errati

**Soluzione:**
1. Assicurati che le immagini siano in `assets/img/`
2. Usa percorsi relativi al baseurl: `{{ '/assets/img/immagine.jpg' | relative_url }}`

### Problema: Il sito è lento

**Soluzione:**
1. Esegui PurgeCSS per ridurre i CSS:
   ```bash
   npx purgecss -c purgecss.config.js
   ```
2. Ottimizza le immagini prima del caricamento
3. Abilita la compressione sul server web (gzip/brotli)

### Problema: Errori di permessi sul server

**Soluzione:**
```bash
# Connettiti al server
ssh utente@server.com

# Imposta i permessi corretti
chmod -R 755 /percorso/sito
chown -R www-data:www-data /percorso/sito
```

### Problema: Modifiche non visibili dopo il deployment

**Soluzione:**
1. Svuota la cache del browser (Ctrl+F5)
2. Verifica che il build sia stato eseguito correttamente
3. Controlla i log del server web
4. Verifica che i file siano stati effettivamente trasferiti

---

## Build Locale per Test

Prima di deployare in produzione, testa sempre in locale:

```bash
# Avvia server di sviluppo
bundle exec jekyll serve --livereload

# Il sito sarà disponibile su http://localhost:4000
```

Oppure usa Docker:

```bash
docker-compose up

# Il sito sarà disponibile su http://localhost:8080
```

---

## Comandi Rapidi di Riferimento

```bash
# Build del sito
export JEKYLL_ENV=production
bundle exec jekyll build

# Build + ottimizzazione CSS
bundle exec jekyll build && npx purgecss -c purgecss.config.js

# Deploy con rsync (⚠️ usa --dry-run per testare prima!)
rsync -avz --delete --dry-run _site/ utente@server:/path/
rsync -avz --delete _site/ utente@server:/path/

# Deploy con scp
scp -r _site/* utente@server:/path/

# Test locale
bundle exec jekyll serve

# Docker test
docker-compose up
```

---

## Risorse Aggiuntive

- [Documentazione Jekyll](https://jekyllrb.com/docs/)
- [al-folio Theme](https://github.com/alshedivat/al-folio)
- [Jekyll Deploy Docs](https://jekyllrb.com/docs/deployment/)
- [GitHub Pages Docs](https://docs.github.com/en/pages)

---

## Supporto

Per problemi o domande relative al deployment, consulta:
1. Questo file README_DEPLOYMENT.md
2. Il file [INSTALL.md](INSTALL.md) per l'installazione
3. Il file [README.md](README.md) per informazioni generali sul progetto
