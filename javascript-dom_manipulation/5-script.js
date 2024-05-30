const update_header = document.getElementById('update_header')

update_header.addEventListener('click', function(){
    const header = document.querySelector('header');

    header.textContent = "New Header!!!"
})
