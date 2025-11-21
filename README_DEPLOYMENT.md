# Guida al Deployment del Sito XAI Project

Questa guida spiega come effettuare il deployment del sito web XAI Project su un server tramite SSH/FTP.

## Indice

1. [Prerequisiti](#prerequisiti)
2. [Configurazione Iniziale](#configurazione-iniziale)
3. [Procedura di Deployment](#procedura-di-deployment)
4. [Script di Deployment Automatico](#script-di-deployment-automatico)
5. [Troubleshooting](#troubleshooting)

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

# Esempio configurazione per il tuo server:
url: http://tuoserver.com
baseurl:  # lascia vuoto se il sito è alla root
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

## Procedura di Deployment

Il deployment del sito avviene in tre fasi principali: build del sito statico, ottimizzazione (opzionale) e trasferimento dei file sul server.

### Passo 1: Build del Sito

Genera i file statici del sito nella cartella `_site/`:

```bash
# Imposta l'ambiente di produzione
export JEKYLL_ENV=production

# Esegui il build
bundle exec jekyll build
```

Il comando genererà tutti i file statici nella directory `_site/`.

### Passo 2: Ottimizzazione CSS (Opzionale)

Rimuovi le classi CSS non utilizzate per ridurre le dimensioni dei file:

```bash
# Usa npx se hai installato purgecss come dipendenza del progetto
npx purgecss -c purgecss.config.js

# Oppure se l'hai installato globalmente
purgecss -c purgecss.config.js
```

Questo sostituirà i file CSS in `_site/assets/css/` con versioni ottimizzate.

### Passo 3: Trasferimento dei File

Trasferisci il contenuto della cartella `_site/` sul server tramite:

**Opzione A: SCP (SSH File Copy)**

```bash
# Copia l'intera cartella _site sul server
scp -r _site/* utente@tuoserver.com:/percorso/directory/web/

# Con porta SSH specifica (se necessario)
scp -P 22 -r _site/* utente@tuoserver.com:/percorso/directory/web/
```

**Opzione B: RSYNC (Sincronizzazione)**

```bash
# Sincronizza i file (più efficiente, trasferisce solo le modifiche)
# ⚠️ ATTENZIONE: --delete rimuove i file sul server che non esistono localmente!
# Verifica sempre il percorso di destinazione prima di usare --delete

# Prima fai un dry-run per vedere cosa cambierà
rsync -avz --delete --dry-run _site/ utente@tuoserver.com:/percorso/directory/web/

# Se il dry-run è corretto, esegui il comando reale
rsync -avz --delete _site/ utente@tuoserver.com:/percorso/directory/web/

# Con porta SSH personalizzata (se necessario)
rsync -avz -e "ssh -p 2222" --delete _site/ utente@tuoserver.com:/percorso/directory/web/
```

**Opzione C: FTP/SFTP**

Puoi usare un client FTP come FileZilla o un comando da terminale:

```bash
# SFTP da linea di comando
sftp utente@tuoserver.com
> cd /percorso/directory/web
> put -r _site/*
> exit
```

### Passo 4: Verifica dei Permessi

Dopo il trasferimento, assicurati che i file abbiano i permessi corretti sul server:

```bash
# Connettiti via SSH al server
ssh utente@tuoserver.com

# Imposta i permessi corretti (esempio standard)
chmod -R 755 /percorso/directory/web
chown -R www-data:www-data /percorso/directory/web

# Verifica che i file siano accessibili
ls -la /percorso/directory/web
```

---

## Script di Deployment Automatico

Puoi creare uno script per automatizzare il processo:

```bash
#!/bin/bash
# deploy.sh

# Configurazione - Modifica questi valori per il tuo server
SERVER_USER="tuoutente"
SERVER_HOST="tuoserver.com"
SERVER_PATH="/percorso/directory/web/"

echo "🚀 Inizio deployment..."

# Build
echo "📦 Building sito..."
export JEKYLL_ENV=production
bundle exec jekyll build

# Ottimizzazione CSS (opzionale)
echo "🎨 Ottimizzazione CSS..."
if command -v npx &> /dev/null; then
    npx purgecss -c purgecss.config.js
elif command -v purgecss &> /dev/null; then
    purgecss -c purgecss.config.js
else
    echo "⚠️  PurgeCSS non installato, skip ottimizzazione CSS"
fi

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

## Test Locale

Prima di deployare in produzione, è consigliabile testare sempre il sito in locale:

```bash
# Avvia il server di sviluppo Jekyll
bundle exec jekyll serve --livereload

# Il sito sarà disponibile su http://localhost:4000
# Usa Ctrl+C per fermare il server
```

---

## Comandi Rapidi di Riferimento

```bash
# Build del sito per produzione
export JEKYLL_ENV=production
bundle exec jekyll build

# Build + ottimizzazione CSS (in un unico comando)
bundle exec jekyll build && npx purgecss -c purgecss.config.js

# Deploy con rsync (⚠️ usa --dry-run per testare prima!)
rsync -avz --delete --dry-run _site/ utente@tuoserver.com:/percorso/
rsync -avz --delete _site/ utente@tuoserver.com:/percorso/

# Deploy con scp
scp -r _site/* utente@tuoserver.com:/percorso/

# Test locale
bundle exec jekyll serve --livereload
```

---

## Risorse Aggiuntive

- [Documentazione Jekyll](https://jekyllrb.com/docs/)
- [al-folio Theme](https://github.com/alshedivat/al-folio)
- [Jekyll Deploy Docs](https://jekyllrb.com/docs/deployment/)

---

## Supporto

Per problemi o domande relative al deployment, consulta:
1. Questo file README_DEPLOYMENT.md
2. Il file [INSTALL.md](INSTALL.md) per l'installazione
3. Il file [README.md](README.md) per informazioni generali sul progetto
