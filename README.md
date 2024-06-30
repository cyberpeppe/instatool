# Instagram Unfollow Automation Tool

Questo repository contiene uno strumento Python per automatizzare l'azione di "unfollow" su Instagram utilizzando la libreria `instagrapi`. L'obiettivo principale è semplificare la gestione dei profili seguiti, consentendo agli utenti di rimuovere facilmente i profili che non desiderano più seguire.

## Caratteristiche principali

- **Autenticazione Sicura**: Utilizza le credenziali dell'account Instagram fornite dall'utente in modo sicuro e memorizzato localmente.
  
- **Gestione degli Errori**: Gestisce automaticamente gli errori durante il processo di "unfollow", inclusi problemi di connessione, richieste di "challenge" (come Captcha), e altre limitazioni imposte da Instagram.

- **Facilità d'Uso**: Una volta configurato con le credenziali appropriate, il tool esegue automaticamente l'azione di "unfollow" per tutti i profili che l'utente sta seguendo ma non lo seguono.

## Istruzioni per l'Utilizzo

### Configurazione Iniziale

1. Clona il repository sul tuo computer:

git clone https://github.com/cyberpeppe/instatool.git

2. Installa le dipendenze necessarie:
pip install -r requirements.txt
3. Rendi eseguibile lo script Bash:
chmod +x instatool.sh
### Esecuzione del Tool

4. Avvia lo script Python per eseguire l'automazione degli "unfollow":
./instatool.sh

5. Il programma si connetterà al tuo account Instagram, recupererà l'elenco dei tuoi seguaci e chi li segue, quindi eseguirà l'"unfollow" per gli utenti non reciprocamente seguiti.

### Contributi

Se desideri contribuire a questo progetto, sentiti libero di fare un fork del repository, aprire issue per segnalare problemi o suggerire miglioramenti, e proporre modifiche attraverso pull request. Le tue contribuzioni sono benvenute!

### Licenza

Questo progetto è rilasciato con la licenza . Vedi il file `LICENSE` per ulteriori dettagli.

---

© 2024 Nome del Progetto. Creato da cyberpeppe (https://github.com/cyberpeppe).
