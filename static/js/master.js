//登入的彈跳視窗如果按下註冊，則會讓loginPop隱藏，RegisterPop出現
$('.callRegisterModal').on('click',function(){
    $('#loginPop').modal('hide')
    $('#RegisterPop').modal('show')
})