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
  
});