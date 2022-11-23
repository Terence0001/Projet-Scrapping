
let elemBoutonC = document.getElementsByTagName("button");
let boutonDéonnexion = elemBoutonC[0] ; 
boutonDéonnexion.addEventListener("click", maDéconnexion);
  
  function maDéconnexion() {
    window.open('http://127.0.0.1:8000/auth/logout/')
  }

let elemBoutonH = document.getElementsByTagName("button");
let boutonHistorique = elemBoutonH[1] ; 
boutonHistorique.addEventListener("click", monHistorique);
  
  function monHistorique() {
    window.open('http://127.0.0.1:8000/historic')
  }

let elemBoutonG = document.getElementsByTagName("button");
let boutonGraphique = elemBoutonG[2] ; 
boutonGraphique.addEventListener("click", monGraphique);
  
  function monGraphique() {
    window.open('http://127.0.0.1:8000/graphic')
  }

let elemBoutonS = document.getElementsByTagName("button");
let boutonScrapping = elemBoutonS[3] ; 
boutonScrapping.addEventListener("click", monScrapping);
  
  function monScrapping() {
    window.open('http://127.0.0.1:8000/scrapping')
  }

let elemBoutonR = document.getElementsByTagName("button");
let boutonDernierReleve = elemBoutonR[4] ; 
boutonDernierReleve.addEventListener("click", monDernierReleve);
  
  function monDernierReleve() {
    window.open('http://127.0.0.1:8000/lastScrapping')
  }

// fonction qui se valide si l'authentification est True
let elemBoutonA = document.getElementsByTagName("button");
let boutonAuthentification = elemBoutonA[0] ; 
boutonAuthentification.addEventListener("click", monAuthentification);
    
  function monAuthentification() {
    window.open('http://127.0.0.1:8000/dashboard')
  }