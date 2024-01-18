function addToCart(food_id, csrfToken) {
    fetch('http://' + window.location.host + '/cart/add/' + food_id + '/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({
          'quantity': 1,
          'update': false,
        },
        )
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }
        return response.json();
    })
    
    .then(data => {
      if (data.success === 'success') {

        updateCart(data.total_cart_price, data.total_quantity);

        const Toast = Swal.mixin({
            toast: true,
            position: "bottom-end",
            showConfirmButton: false,
            timer: 3000,
            customClass: {
              title: 'title__alert',
            },
            background: '#FAEDD4',
            color: '#FB3B2D',
            timerProgressBar: true,
            didOpen: (toast) => {
              toast.onmouseenter = Swal.stopTimer;
              toast.onmouseleave = Swal.resumeTimer;
            }
        });
          Toast.fire({
            icon: "success",
            title: data.food + " " + "added to your cart"
        });
      } else {
        Swal.fire({
          title: 'Ошибка!',
          text: 'Не удалось добавить товар в корзину.',
          icon: 'error',
          confirmButtonText: 'ОК'
        });
      }
    })
    .catch(error => {
        console.error(error);
    });
}

function updateCart(price, quantity) {
    const cart_total_element = document.getElementById('total_cart')
    cart_total_element.textContent = price;
    const cart_total_quantity = document.getElementById('total_quantity')
    cart_total_quantity.textContent = quantity;
}

document.querySelectorAll('.food__button').forEach(button => {
    button.addEventListener('click', (event) => {
        event.preventDefault();
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
        const food_id = event.target.closest('.food__form').getAttribute('data-food-id');
        addToCart(food_id, csrfToken);
    });
});

document.querySelectorAll('.window__button').forEach(button => {
    button.addEventListener('click', (event) => {
        event.preventDefault();
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
        const cart_food_id = event.target.closest('.food__form').getAttribute('data-food-id');
        addToCart(cart_food_id, csrfToken);
    });
});
