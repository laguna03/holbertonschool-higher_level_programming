const add_item = document.getElementById('add_item')

add_item.addEventListener('click', function(){
    const element = document.createElement('li');

    element.textContent = "Item";

    const my_list = document.querySelector('.my_list');

    my_list.appendChild(element)
})
