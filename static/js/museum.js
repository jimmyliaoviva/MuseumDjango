$(document).ready(function () {

    // 抓取全部的留言


    $.ajax({
        type: 'POST',
        url: '/ajax_get_comment',
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
        },
        success: function (data) {
            for (var cid in data) {
                $('#commentBlock').prepend('<div id="two_layer" class="row comment"><div class="imgWrapper headWrapper col-1"><img src="../static/img/owl.png" alt=""></div><div id="test" class="col-10"><div class="userName">' + data[cid].user + '</div><div class="commentContent">' + data[cid].comment + '</div></div><button id="remove" class="remove" type="button" value="' + cid + '">刪除</button></div>')
            }

        },
    })
    // 按下刪除留言


    $("#commentBlock").on("click", ".remove", function () {
        var this_this = $(this)
        $.ajax({
            type: 'POST',
            url: '/ajax_delete_comment',
            data: {
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
                delete_cid: $(this).attr('value'),
            },
            success: function (data) {
                data == 'success' ? this_this.parent('div').remove() : console.log('comment remove fail')
            },
        })
    })

        // 按下送出留言


    $("#send").click(function () {
        var comment_content = $("#comment_content").val()
        $("#comment_content").val("")
        $.ajax({
            type: 'POST',
            url: '/ajax_add_comment',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
                'comment_content': comment_content
            },
            success: function (data) {
                // 方法二
                $('div.commentBlock').children().remove()
                for (let key in data) {
                    $('#commentBlock').prepend('<div id="two_layer" class="row comment"><div class="imgWrapper headWrapper col-1"><img src="../static/img/owl.png" alt=""></div><div id="test" class="col-10"><div class="userName">' + data[key].user + '</div><div class="commentContent">' + data[key].comment + '</div></div><button id="remove" class="remove" type="button" value="' + key + '">刪除</button></div>')
                }
            }
        })
    });
});