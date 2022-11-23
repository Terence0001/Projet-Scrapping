function alert2(){
    alert("appel dépuis une fonction");
}

export default function funcAlert(){
    alert2();
    return("la fonction est exporté");
}
