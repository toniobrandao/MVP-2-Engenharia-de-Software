//Importando as funções e variáveis utilizadas.
import { predictionButton } from "./ui/uiVariables.js";
import { collectInputValues } from "./ui/uiFunctions.js";

//Acidionando o event listener ao botão de realizar a predição.
predictionButton.addEventListener("click", collectInputValues);
