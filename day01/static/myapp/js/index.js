$(function() {
    $('#shousuo').on('click',function() {
        var csrf = $('input[name="csrfmiddlewaretoken"]').val()
        var value = $('.l_box #keyboard').get(0).value
        $.ajax({
            'url': '/api/myapp/art/' + '?keyword=' + value,
            'type': 'GET',
            'headers':{'X-CSRFToken':csrf},
            'dataType': 'json',
            'success':function(data) {
                    $.each(data.data.results, function(index,article){
                        var id = article.id;
                        var p = $('<p>').text(article.title);
//                        var url = '../myinfo/' + id + '/'
                        var url = '/myapp/myinfo/' + id + '/';
                        var a = $('<a>').attr('href',url)
                        a.append(p);
                        $('#seakeyword').append(a)
                    })
            },
            'error': function (data) {
                      console.log('删除失败')
					},
        })
    })
})