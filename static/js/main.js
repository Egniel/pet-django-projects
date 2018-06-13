$( document ).ready(function() {

    $(document).on({
        mouseenter: function(){
            $(this).addClass('active');
        },
        mouseleave: function(){
            $(this).removeClass('active');
        }
    }, '.list-group-item')
    $(document).on('click', '.btn-outline-success', function(event){
        $.ajax({
            url: '/api/v1/todos/' + $(this).attr('data-pk') + '/',
            type: 'PATCH',
            data: {
                done: true,
            },
            success: function(data) {
                $('#todos').html('').load('/todo/get-todos/');
            },
        });
    });
    $(document).on('click', '.btn-outline-primary', function(event){
        $.ajax({
            url: '/api/v1/todos/' + $(this).attr('data-pk') + '/',
            type: 'PATCH',
            data: {
                done: false,
            },
            success: function(data) {
                $('#todos').html('').load('/todo/get-todos/');
            },
        });
    });
    $(document).on('click', '.btn-outline-warning', function(){
        $.ajax({
            url: '/api/v1/todos/' + $(this).attr('data-pk') + '/',
            type: 'DELETE',

            success: function(data) {
                $('#todos').html('').load('/todo/get-todos/');
            }
        });
    });
    $(document).on('submit', '#addTodoForm', function (event) {
        event.preventDefault();
        data = {
            text: $('#addTodo').val(),
            done: false,
        };
        $.ajax({
            url: '/api/v1/todos/',
            type: 'POST',
            data: data,
            success: function(data) {
                $('#todos').html('').load('/todo/get-todos/');
                $('#addTodo').val('');
            }
        });
    });
});
