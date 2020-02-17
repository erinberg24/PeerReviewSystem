document.querySelector("#studentTeacherSelect").addEventListener("change", updateHref);


function updateHref(){
    let valueSelected = document.querySelector("#studentTeacherSelect").value;

    if (valueSelected === "student") {
        document.getElementById("switchingButton").href="studentLP.html"; 
    } else {
        document.getElementById("switchingButton").href="instructorLP.html"; 
    }


}
