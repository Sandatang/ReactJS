const add = document.getElementById('add')
const close = document.getElementById('closeModal')
const modal = document.getElementById('addModal')

const mssg = document.getElementById('mssg')

const edit = document.getElementById('edit')
const editModal = document.getElementById('editModal')

const deleteActionForm = document.getElementById('deleteActionForm')
const editActionForm = document.getElementById('editActionForm')


setTimeout(() => {
    mssg.innerText = ""
}, 1000)

add.onclick = () => {
    modal.style.display = 'block'
}

close.onclick = () =>{
    modal.style.display = 'none'
}


function delConfirmation(event, idno){
    event.preventDefault()
    if(confirm("Do you want to delete this student?"+idno)){
        deleteActionForm.submit()
    }
}
