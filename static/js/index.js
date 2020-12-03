$(document).ready(function () {

})
$(".countrySearch").change(function () {
        if ($(this).val() == "") {
            $('.citySearch').children().remove()
            $('.citySearch').append('<option value=""></option>')
        } else {
            ajax_get_city($(this).val())
        }
    }
)

function ajax_get_city(nation) {
    $.ajax({
        type: 'GET',
        url: '/ajax_get_city',
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            nation: nation,
        },
        success: function (data) {
            $('.citySearch').children().remove()
            $('.citySearch').append('<option value=""></option>')
            for (var cid in data) {
                $('.citySearch').append('<option value=' + cid + '>' + data[cid].city + '</option>')
            }
        },
    })
}