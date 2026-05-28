const modal = document.getElementById('modal')
const closeModalButton = document.querySelector('dialog button')
const modalContent = document.getElementById('modal-content')

closeModalButton.addEventListener('click', function () {
    modal.close()
})

export function openStoryModal(titulo, autor, historia) {
    modalContent.innerHTML = `
        <h2>${titulo}</h2>
        <h4><strong>Autor:</strong> ${autor}</h4>
        <p style="white-space: pre-wrap">${historia} </p>
    `

    modal.showModal();
}