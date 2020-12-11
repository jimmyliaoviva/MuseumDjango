//登入的彈跳視窗如果按下註冊，則會讓loginPop隱藏，RegisterPop出現
$('.callRegisterModal').on('click',function(){
    $('#loginPop').modal('hide')
    $('#RegisterPop').modal('show')
})
$(document).ready(function() {
    $("#send_but").click(function() {
        var position = '/edit_name'
        var name = $("#edit_name").val()
        if(name=="") {
            $("#error_message").children().remove()
            $("#error_message").append("<p style='color:red'>輸入的暱稱有誤!</p>")
        }
        else {
            ajax_edit_account(position, name)
        }
    })
    //監聽使用者修改種類
    $("#but_area").on("click",".edit_but", function() {
        var monitor = $(this)
        $("#error_message").children().remove()
        //if-else為各種修改種類的處理方式
        if(monitor.attr('value')=='edit_name') {
            $("#edit_content").children().remove()
            $("#edit_content").append('<div class="note">暱&emsp;&emsp;稱: <input id="edit_name" name="edit_name" class="input_bar"/></div><button id="edit_name_but" type="button" class="send_but">送出</button>')
            $('#edit_name_but').click(function() {
                var position = '/edit_name'
                var name = $("#edit_name").val() 
                if(name==""){
                    $("#error_message").children().remove()
                    $("#error_message").append("<p style='color:red'>請輸入暱稱!</p>")
                }
                else{
                    ajax_edit_account(position, name)
                }
            })
        }
        else if(monitor.attr('value')=='edit_pass') {
            $("#edit_content").children().remove()
            $("#edit_content").append('<div class="note">密&emsp;&emsp;碼: <input id="edit_pass" class="input_bar" name="edit_pass" type="password"/></div><div class="note">確認密碼: <input id="check_edit_pass" class="input_bar" name="check_edit_pass" type="password"/></div><button id="edit_pass_but" class="send_but" type="button">送出</button>')
            $("#edit_pass_but").click(function() {
                var position = '/edit_pass'
                var org = $("#edit_pass").val()
                var check = $("#check_edit_pass").val()
                if(org!=check || org=="") {
                    $("#error_message").children().remove()
                    $("#error_message").append("<p style='color:red'>輸入的密碼有誤!</p>")
                }
                else {
                    ajax_edit_account(position, name, org)
                }
            })
        }
        else {
            $("#edit_content").children().remove()
            $("#edit_content").append('<div class="note">暱&emsp;&emsp;稱: <input id="edit_name" class="input_bar" name="edit_name"/></div><div class="note">密&emsp;&emsp;碼: <input id="edit_pass" class="input_bar" name="edit_pass" type="password"/></div><div class="note">確認密碼: <input id="check_edit_pass" class="input_bar" name="check_edit_pass" type="password"/></div><button id="edit_pass_but" class="send_but" type="button">送出</button>')
            $("#edit_pass_but").click(function() {
                var position = "/edit_all"
                var name = $("#edit_name").val()
                var org = $("#edit_pass").val()
                var check = $("#check_edit_pass").val()
                if(name=="" || org!=check || org=="") {
                    $("#error_message").children().remove()
                    $("#error_message").append("<p style='color:red'>輸入的暱稱或密碼有誤!</p>")
                }
                else {
                    ajax_edit_account(position, name, org)
                }
            })
        }
    })
    function ajax_edit_account(position=false,name=false,password=false) {
        $.ajax({
            type: 'POST',
            url: position,
            data: {
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
                name: name,
                password: password,
            },
            success: function (data) {
                if(data=='False') {
                    $("#error_message").children().remove()
                    if(name!=false && password!=false){
                        $("#error_message").append("<p style='color:red'>輸入的暱稱或密碼有誤!</p>")
                    }
                    else if(name!=false){
                        $("#error_message").append("<p style='color:red'>輸入的暱稱有誤!</p>")
                    }
                    else{
                        $("#error_message").append("<p style='color:red'>輸入的密碼有誤!</p>")
                    }
                }
                else {
                    window.location.reload()
                }
            },
        })
    }
})