$(function () {
    $(".btn-delete").click(function(){
        var school_id = $(this).attr('data-school_id');
        if(confirm("Are your sure?")) {
            $.ajaxSetup({
                headers: {
                    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                }
            });
            
            $.ajax({url: url,
                method: 'post',
                data: {school_id:school_id}, 
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
