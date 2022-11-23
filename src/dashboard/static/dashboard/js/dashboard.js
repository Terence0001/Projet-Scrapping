
let elemBoutonC = document.getElementsByTagName("button");
let boutonDéonnexion = elemBoutonC[0] ; 
boutonDéonnexion.addEventListener("click", maDéconnexion);
  
  function maDéconnexion() {
    window.open('http://127.0.0.1:8000/auth/logout/')
  }