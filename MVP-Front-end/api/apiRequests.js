import apiBaseURL from "./apiBaseURL.js";
import { updateDiagnosticText } from "../ui/uiFunctions.js";
/*
  --------------------------------------------------------------------------------------
  POST REQUEST: Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postPatient = async (inputJSON) => {
  const jsonData = JSON.stringify(inputJSON);

  let url = `${apiBaseURL}/patient`;
  fetch(url, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: jsonData,
  })
    .then((response) => response.json())
    .then((data) => {
      updateDiagnosticText(data.target);
      return data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

export { postPatient };
