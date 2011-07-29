$(ready);
function ready(){
    $("#mytags").tagit({
		tagSource: "/testajax",
		allowSpaces: true,
		itemName: 'tags',
		fieldName: 'term'
    });
    $("#wmd-preview").hide();
    $('#lnkPreview').click(function(){
		toggle_preview();
    });
    $("#test").click(function(){
		test();
    });
    $("#hrefTest").click(function(){
	var tags = $("input[name='tags[term][]']");
	alert(tags);
	//alert('hey');
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
        data: {term: $(".ui-widget-content").val()},
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
