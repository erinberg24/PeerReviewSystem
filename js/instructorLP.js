document.querySelector("#assessmentViewer").addEventListener("change", updateHref);


function updateHref(){
    let valueSelected = document.querySelector("#assessmentViewer").value;

    if (valueSelected === "create") {
        document.getElementById("pageSwitcher").href="createPeerAssessment.html"; 
    } else {
        document.getElementById("pageSwitcher").href="instructorResults.html"; 
    }


}