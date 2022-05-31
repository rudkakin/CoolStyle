const openPopUpReg = document.getElementById('open_pop_up_reg');
const closePopUpReg = document.getElementById('pop_up_reg_close');
const popUpReg = document.getElementById('pop_up_reg');

openPopUpReg.addEventListener('click', function(e) {
    e.preventDefault();
    popUpReg.classList.add('active');
})

closePopUpReg.addEventListener('click', () => {
    popUpReg.classList.remove('active');
})