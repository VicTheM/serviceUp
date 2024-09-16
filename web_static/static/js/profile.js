const profileInfoElement = document.getElementById("profile-info");
const hireBtn = document.getElementById("hire-btn");

const dialogElement = document.getElementById("dialog");

const handleHireBtnClick = () => {
    dialogElement.showModal();

    profileInfoElement.classList.add("show");
}

hireBtn.addEventListener("click", handleHireBtnClick);