$(document).ready(function(){

    $("#floatShow").bind("click",function(){
    
        $("#onlineService").animate({width:"show", opacity:"show"}, "normal" ,function(){
            $("#onlineService").show();
        });
        
        $("#floatShow").attr("style","display:none");
        $("#floatHide").attr("style","display:block");
        
        return false;
    });
    
    $("#online_qq_tab").bind("click",function(){
    
        $("#onlineService").animate({width:"hide", opacity:"hide"}, "normal" ,function(){
            $("#onlineService").hide();
        });
        
        $("#floatShow").attr("style","display:block");
        $("#floatHide").attr("style","display:none");
        
        return false;
    });

    $("#recharge").click(function(event) {
        event.preventDefault();
        var url = $(this).attr('data-ajax-url')
        $.post(url,function(data,status){
            if (status == 'success') {
                var html = data['html'];
                $("#modal_div").html(html);
                $('#select_charge_amount_modal').modal('show')
            }
        });
    });

    $(".order_pay").click(function(event) {
        event.preventDefault();
        var url = $(this).attr('data-ajax-url')
        var order_id = $(this).attr('order-id')
        var ret = confirm('确认要付款吗?');
        if (ret) {
            $.post(
                url,
                {
                    order_id:order_id
                },
                function(data, status){
                    if(status == 'success'){
                        location.reload();
                    }
                });
        } 
    });

    //初始化显示哪个tab
    $('#myTab a:first').tab('show');      
        $('#myTab a').click(function (e) {
            e.preventDefault();
            $(this).tab('show');//显示当前选中的链接及关联的content
        });
  
});