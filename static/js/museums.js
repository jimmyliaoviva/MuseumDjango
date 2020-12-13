$('.arrowBlock').on('click', '#goToMuseum', function () {
    var museumUrl = '/museum/'+ $(this).val()
    window.location.href = museumUrl
})