window.addEventListener("load", function (){
  let counter 0;

  //camelCase
  function buttonClicked()
    {
      counter++;

      let clickedCounterElement = document.getElementById("clickcounter");

      clickedcounterElement.innerHTML = "Clicked " + ocunter + " times.";
    }
  let clickedButtonElement = document.getElementById("clickbutton");


clickedButtonElement.addEventListener("click", buttonClicked);
}
                      