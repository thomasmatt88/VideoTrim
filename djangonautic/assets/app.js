//now it doesn't matter where you add the script inside of the html page
document.addEventListener('DOMContentLoaded', function(){
  //delete books
  const list = document.querySelector('#book-list ul');
  list.addEventListener('click', function(e){ //have the event listener associated with the ul instead
    if(e.target.className == 'delete'){
      const li = e.target.parentElement;
      list.removeChild(li);
    }
  })

  //add book-list
  const addForm = document.forms['add-book'];
  const add = document.querySelector('#add');
  add.addEventListener('click', function(e){
    e.preventDefault();//prevent default behavior which is to refresh page
    const value = addForm.querySelector('input[type="text"]').value; //'input[type="text"]' is a valid css selector
    try {
      lastTrimPoint = parseFloat(list.lastElementChild.querySelector('.name').innerText) // value of last item in list
    }
    catch(error) {
      lastTrimPoint = 0;
    }

    //input has to be a number and greater than the previous input
    //in order to be appended to the list
    if(!isNaN(value) && (value >= lastTrimPoint)){
      //create elements
      const li = document.createElement('li');
      const bookName = document.createElement('span');
      const deleteBtn = document.createElement('span');

      //add content to elements
      deleteBtn.textContent = 'delete';
      bookName.textContent = value;

      //add classes to elements
      bookName.classList.add('name');
      deleteBtn.classList.add('delete');

      //append to document...order matters
      li.appendChild(bookName);
      li.appendChild(deleteBtn);
      li.innerHTML += "<input type='hidden' name='mylist' value='" + value + "'>";
      list.appendChild(li);
    }

  });

});
