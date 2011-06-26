$(ready);
function ready(){
    $("#mytags").tagit();
    $("#wmd-preview").hide();
    $('#lnkPreview').click(function(){
	toggle_preview();
    });
    $("#test").click(function(){
	test();
    });
}

function toggle_preview(){
    $("#wmd-preview").toggle();
}

function test(){
    var retval = null;
    $.ajax({
        type: "GET",
        url: "/testajax",
        dataType: "json",
        data: null,
        success: function (data, status) {
	    /*
            $("#result").html("ok");*/
            if (data == true) {
                $("#result").html("ok");
            } else {
                //window.location.reload();
                $("#result").html(data);
            }
	    $("#result").html(data.msg);

        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //$("#result").html(textStatus);
	    $("#result").html('shit, error?');
        },
        beforeSend: function () {
            $("#result").html("wait...");
        },
        complete: function () {
            //$("#result").html("");
        }
    });

    return retval;
}
