$(function () {
    $(".btn-delete").click(function(){
        var course_code = $(this).attr('data-course_id');
        if(confirm("Are your sure?")) {
            $.ajaxSetup({
                headers: {
                    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                }
            });
            
            $.ajax({url: url,
                method: 'post',
                data: {course_code:course_code}, 
                success: function(result){
                   console.log(result);
                   if(result.success) {
                        alert(result.message);
                       location.reload()
                   } else {
                       alert(result.message);
                   } 
                }});
        }
    });        
        
        
});