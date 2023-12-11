import { postPatient } from "../api/apiRequests.js";
import { inputs } from "./uiVariables.js";
import { h2Element } from "./uiVariables.js";
/*
  --------------------------------------------------------------------------------------
  Função para coletar os inputs e realizar um Post Request para a API.
  --------------------------------------------------------------------------------------
*/

function collectInputValues() {
  const values = {};

  inputs.forEach((input) => {
    const inputName = input.getAttribute("name");
    if (input.type === "text" || input.type === "range") {
      values[inputName] = input.value;
    }
  });
  postPatient(values);
}

/*
  --------------------------------------------------------------------------------------
  Função para fazer a atualização de texto do resultado da predição na UI.
  --------------------------------------------------------------------------------------
*/

function updateDiagnosticText(targetValue) {
  if (targetValue === 1) {
    h2Element.textContent =
      "Resultado positivo para doença arterial coronária, recomendamos que procure auxílio médico imediatamente. ";
  } else if (targetValue === 0) {
    h2Element.textContent =
      "Resultado negativo para doença arterial coronária, porém, não deixe de checar com um médico a sua saúde cardiovascular!";
  }
}

export { collectInputValues, updateDiagnosticText };
