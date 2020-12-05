//登入的彈跳視窗如果按下註冊，則會讓loginPop隱藏，RegisterPop出現
$('.callRegisterModal').on('click',function(){
    $('#loginPop').modal('hide')
    $('#RegisterPop').modal('show')
})
$(document).ready(function() {
    console.log($('#form_type').attr('action'))
    $("#send_but").click(function() {
        var value = $("#edit_name").val()
        if(value=="") {
            $("#error_message").children().remove()
            $("#error_message").append("<p style='color:red'>輸入的暱稱有誤!</p>")
        }
        else {
            $("#send_but").attr('type','submit')
        }
    })
    //監聽使用者修改種類
    $("#but_area").on("click",".edit_but", function() {
        var monitor = $(this)
        $("#error_message").children().remove()
        //if-else為各種修改種類的處理方式
        if(monitor.attr('value')=='edit_name') {
            $("#edit_content").children().remove()
            $("#form_type").attr('action','/edit_name')
            $("#edit_content").append('<div class="note">暱&emsp;&emsp;稱: <input id="edit_name" name="edit_name" class="input_bar"/></div><button id="edit_name_but" type="button" class="send_but">送出</button>')
            $('#edit_name_but').click(function() {
                var value = $("#edit_name").val() 
                if(value==""){
                    $("#error_message").children().remove()
                    $("#error_message").append("<p style='color:red'>輸入的暱稱有誤!</p>")
                }
                else{
                    $("#edit_name_but").attr('type','submit')
                }
            })
        }
        else if(monitor.attr('value')=='edit_pass') {
            $("#edit_content").children().remove()
            $("#form_type").attr('action','/edit_pass')
            $("#edit_content").append('<div class="note">密&emsp;&emsp;碼: <input id="edit_pass" class="input_bar" name="edit_pass" type="password"/></div><div class="note">確認密碼: <input id="check_edit_pass" class="input_bar" name="check_edit_pass" type="password"/></div><button id="edit_pass_but" class="send_but" type="button">送出</button>')
            $("#edit_pass_but").click(function() {
                var org = $("#edit_pass").val()
                var check = $("#check_edit_pass").val()
                if(org!=check | org=="") {
                    $("#error_message").children().remove()
                    $("#error_message").append("<p style='color:red'>輸入的密碼有誤!</p>")
                }
                else {
                    $("#edit_pass_but").attr('type','submit')
                }
            })
        }
        else {
            $("#edit_content").children().remove()
            $("#form_type").attr('action','/edit_all')
            $("#edit_content").append('<div class="note">暱&emsp;&emsp;稱: <input class="input_bar" name="edit_name"/></div><div class="note">密&emsp;&emsp;碼: <input id="edit_pass" class="input_bar" name="edit_pass" type="password"/></div><div class="note">確認密碼: <input id="check_edit_pass" class="input_bar" name="check_edit_pass" type="password"/></div><button id="edit_pass_but" class="send_but" type="button">送出</button>')
            $("#edit_pass_but").click(function() {
                var org = $("#edit_pass").val()
                var check = $("#check_edit_pass").val()
                if(org!=check | org=="") {
                    $("#error_message").children().remove()
                    $("#error_message").append("<p style='color:red'>輸入的暱稱或密碼有誤!</p>")
                }
                else {
                    $("#edit_pass_but").attr('type','submit')
                }
            })
        }
    })
})