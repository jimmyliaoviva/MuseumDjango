$(document).ready(function () {

    // 抓取全部的留言
    $.ajax({
        type: 'POST',
        url: '/ajax_get_comment',
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            "museumId": pk
        },
        success: function (data) {
            appendComment(data)
            // for (var cid in data) {
            //     if (userId == data[cid].userId) {
            //         $('#commentBlock').prepend('<div id="two_layer" class="row comment"> <div class="imgWrapper headWrapper col-1"><img src="../static/img/owl.png" alt=""></div> <div id="test" class="col-10"> <div class="userName">' + data[cid].user + ' <button id="remove" class="remove" type="button"value="' + cid + '">刪除 </button> <button id="edit">修改</button> <span class="time">' + data[cid].commentTime + '</span> </div> <div class="commentContent">' + data[cid].comment + '</div> </div> </div>')
            //     } else {
            //         $('#commentBlock').prepend('<div id="two_layer" class="row comment"><div class="imgWrapper headWrapper col-1"><img src="../static/img/owl.png" alt=""></div><div id="test" class="col-10"><div class="userName">' + data[cid].user + '</div><div class="commentContent">' + data[cid].comment + '</div></div></div>')
            //
            //     }
            // }

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
                data == 'success' ? this_this.closest('#two_layer').remove() : console.log('comment remove fail')
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
                'comment_content': comment_content,
                'museumId': pk
            },
            success: function (data) {
                // 方法二
                $('div.commentBlock').children().remove()
                appendComment(data)
                // for (let cid in data) {
                //     if (userId == data[cid].userId) {
                //         $('#commentBlock').prepend('<div id="two_layer" class="row comment"><div class="imgWrapper headWrapper col-1"><img src="../static/img/owl.png" alt=""></div><div id="test" class="col-10"><div class="userName">' + data[cid].user + '</div><div class="commentContent">' + data[cid].comment + '</div></div><button id="remove" class="remove" type="button" value="' + cid + '">刪除</button></div>')
                //     } else {
                //         $('#commentBlock').prepend('<div id="two_layer" class="row comment"><div class="imgWrapper headWrapper col-1"><img src="../static/img/owl.png" alt=""></div><div id="test" class="col-10"><div class="userName">' + data[cid].user + '</div><div class="commentContent">' + data[cid].comment + '</div></div></div>')
                //
                //     }
                // }
            }
        })
    });

    //按下修改
    $('#commentBlock').on("click", "#editBtn", function () {
        $(this).closest("#test").hide()
        $(this).closest("#two_layer").children("#editBlock").show()
    })

    //修改後按下儲存
    $('#commentBlock').on("click", "#saveBtn", function () {
        comment_content = $(this).closest("#editBlock").children(".commentTextarea").val()
        commentId = $(this).val()
        $.ajax({
            type: 'POST',
            url: '/ajax_save_comment',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
                'comment_content': comment_content,
                'museumId': pk,
                'commentId': commentId
            },
            success: function (data) {
                $('div.commentBlock').children().remove()
                appendComment(data)
            }
        })
    })

});

function appendComment(data) {
    for (var cid in data) {
        if (userId == data[cid].userId) {
            $('#commentBlock').prepend(
                `<div id="two_layer" class="row comment">
                <div class="imgWrapper headWrapper col-1"><img src="../static/img/owl.png" alt=""></div>
                <div id="test" class="col-10">
                    <div class="userName">${data[cid].user}
                        <button id="remove" class="remove" type="button"
                                value="${cid}">刪除
                        </button>
                        <button id="editBtn" value="${cid}">修改</button>
                        <span class="time">${data[cid].commentTime}</span>
                    </div>
                    <div class="commentContent">${data[cid].comment}</div>
                </div>
<!--                修改block  預設是隱藏-->
                <div id="editBlock" class="edit col-10">
                    <div class="userName">${data[cid].user}
                    <button id="saveBtn" value="${cid}">儲存</button>
                    </div>
                <textarea class="commentContent commentTextarea">${data[cid].comment}</textarea>
            </div>
`)
        } else {
            $('#commentBlock').prepend('<div id="two_layer" class="row comment"><div class="imgWrapper headWrapper col-1"><img src="../static/img/owl.png" alt=""></div><div id="test" class="col-10"><div class="userName">' + data[cid].user + '</div><div class="commentContent">' + data[cid].comment + '</div></div></div>')

        }
    }
}